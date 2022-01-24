import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

import requests
import datetime
from datetime import datetime

class Model:

	# Funcion que devuleve una lista con las cincidencias de nombre y apellidos
	def busquedaUsuario(self, nombre, apellidos):
		# Consulta a la base de datos
		try:
			r_user = requests.get("http://localhost:8080/api/rest/user?name=" + nombre + "&surname=" + apellidos, headers={"x-hasura-admin-secret":"myadminsecretkey"})

			# Lectura de la consulta
			dicionarioUsuarios = r_user.json()
			listaUsuarios = dicionarioUsuarios.get('users')

			# Inicializacion de la lista
			resultadoBusqueda = []

			# Obtencion del uuid, nombre y apellidos
			for aux in listaUsuarios:
			    resultadoBusqueda.append((aux.get("name") + " " + aux.get("surname"), aux.get("uuid")))

			return resultadoBusqueda

		except requests.exceptions.RequestException:
		    raise requests.exceptions.RequestException




	# Funcion que devuelve los datos de un usuario pasandole un uuid
	def datosUsuario(self, uuid):
		# Consulta datos usuario
		try:
			r_users = requests.get("http://localhost:8080/api/rest/users/" + uuid, headers={"x-hasura-admin-secret":"myadminsecretkey"})
			# Lectura consulta
			dicionarioDatosUsuario = r_users.json()
			datosUsuario = dicionarioDatosUsuario.get('users')

			return datosUsuario

		except requests.exceptions.RequestException:
		    raise requests.exceptions.RequestException



	# Funcion que devuelve la actividad reciente de un usuario
	def actividadRecienteUsuario(self, uuid):
		# Consulta actividad reciente (reducida)
		try:
			r_user_access_log = requests.get("http://localhost:8080/api/rest/user_access_log/" + uuid + "?limit=5", headers={"x-hasura-admin-secret":"myadminsecretkey"})

			# Lectura consulta
			dicionarioActividadReciente = r_user_access_log.json()
			listaActividadReciente = dicionarioActividadReciente.get('access_log')

			# Inicializacion de la lista
			actividadReciente = []

			# Obtencion del nombre del centro, temperatura del usuario, fecha de acceso y estado del acceso
			for aux in listaActividadReciente:
			    actividadReciente.append((aux.get("facility").get("name"), str(aux.get("temperature")), self.formatoVista(aux.get("timestamp")), aux.get("type")))

			return actividadReciente

		except requests.exceptions.RequestException:
		    raise requests.exceptions.RequestException


	# Función que devuelve el historial de actividad de un usuario
	def historialActividadUsuarios(self, uuid):
		# Consulta historial de actividad
		try:
			r_user_access_log = requests.get("http://localhost:8080/api/rest/user_access_log/" + uuid, headers={"x-hasura-admin-secret":"myadminsecretkey"})

			dicionarioHistorialActividad = r_user_access_log.json()
			listaHistorialActividad = dicionarioHistorialActividad.get('access_log')

			historialActividad = []
			for aux in listaHistorialActividad:
				historialActividad.append((str(aux.get("facility").get("id")), aux.get("facility").get("name"), str(aux.get("temperature")), self.formatoVista(aux.get("timestamp")), aux.get("type")))

			return historialActividad

		except requests.exceptions.RequestException:
		    raise requests.exceptions.RequestException

	def dataUbicacion(self, id):

		# Consulta historial de actividad
		try:
			r_facilities = requests.get("http://localhost:8080/api/rest/facilities/" + id, headers={"x-hasura-admin-secret":"myadminsecretkey"})
			diccionarioDataUbicacion = r_facilities.json()
			datosUbicacion = diccionarioDataUbicacion.get('facilities')

			return datosUbicacion

		except requests.exceptions.RequestException:
			raise requests.exceptions.RequestException


	def accesosCentroHoras(self, id, fechaInicial, fechaFinal):
		# Consulta accesos de un centro por horas
		try:
			r = requests.get("http://localhost:8080/api/rest/facility_access_log/"+ str(id) +"/daterange",
			headers={"x-hasura-admin-secret":"myadminsecretkey"},
			json={"startdate": fechaInicial, "enddate": fechaFinal})

			# Lectura consulta

			dicionario = r.json()
			lista = dicionario.get("access_log")

			return lista

		except requests.exceptions.RequestException:
		    raise requests.exceptions.RequestException


	# Funcion que devuelve los contactos de un usuario
	def contactos(self, uuid, fechaI, fechaF):

		if fechaF == "":
			fechaF = datetime.now()
			fechaF = fechaF.strftime("%Y/%m/%d %H:%M:%S")

		fechaInicio = self.formatoBaseDatos(fechaI)
		fechaFin = self.formatoBaseDatos(fechaF)

		#Obtenemos el nombre de la persona a la que se le buscan sus contactos
		contactosDe = self.datosUsuario(uuid)
		nombrePersona = contactosDe[0].get("name") + " " + contactosDe[0].get("surname")

		# Realizamos la consulta
		# Consulta accesos usuario
		try:
			r_user_access_log = requests.get("http://localhost:8080/api/rest/user_access_log/" + uuid + "/daterange",
			headers={"x-hasura-admin-secret":"myadminsecretkey"},
			json={"startdate": fechaInicio, "enddate": fechaFin})

			# Lectura consulta
			dicionarioAccesos = r_user_access_log.json()
			listaAccesos = dicionarioAccesos.get('access_log')
			# Inicializacion de la lista
			contactos = []

			# Obtencion de lista con contactos
			for aux in listaAccesos:
				# Se busca una entrada en un centro
				if aux.get("type") == "IN":
					# Se busca la salida de ese centro
					for aux2 in listaAccesos:
						if aux.get("facility").get("id") == aux2.get("facility").get("id") and aux.get("timestamp") < aux2.get("timestamp") and aux2.get("type") == "OUT":
							# Lista de accesos de un centro entre dos fechas
							lista_aux = self.accesosCentroHoras(aux.get("facility").get("id"), aux.get("timestamp"), aux2.get("timestamp"))

							# Eliminacion de los que coincidan con uuid y los repetidos
							for aux3 in lista_aux:
								if aux3.get("user").get("uuid") != uuid and (aux3.get("user").get("name") + " " + aux3.get("user").get("surname"), aux3.get("user").get("uuid"), aux3.get("user").get("phone")) not in contactos:
									contactos.append((aux3.get("user").get("name") + " " + aux3.get("user").get("surname"), aux3.get("user").get("uuid"), aux3.get("user").get("phone")))
							break # Salir del bucle aux2

			return contactos

		except requests.exceptions.RequestException:
		    raise requests.exceptions.RequestException

	# Cambiar formato fecha vista a formato fecha base de datos
	def formatoBaseDatos(self, fechaOriginal):
	    auxFecha = ""
	    auxFecha = auxFecha + fechaOriginal[0:4]
	    auxFecha = auxFecha + "-"
	    auxFecha = auxFecha + fechaOriginal[5:7]
	    auxFecha = auxFecha + "-"
	    auxFecha = auxFecha + fechaOriginal[8:10]
	    auxFecha = auxFecha + "T"
	    auxFecha = auxFecha + fechaOriginal[11:19]
	    auxFecha = auxFecha + ".277923+00:00"

	    return auxFecha					# Retorna la fecha

	# Cambiar formato fecha base de datos a formato fecha vista
	def formatoVista(self, fechaOriginal):
	    auxFecha = ""
	    auxFecha = auxFecha + fechaOriginal[0:4]
	    auxFecha = auxFecha + "/"
	    auxFecha = auxFecha + fechaOriginal[5:7]
	    auxFecha = auxFecha + "/"
	    auxFecha = auxFecha + fechaOriginal[8:10]
	    auxFecha = auxFecha + " "
	    auxFecha = auxFecha + fechaOriginal[11:19]

	    return auxFecha					# Retorna la fecha

	# Funcion que devuelve los datos de un usuario pasandole un uuid
	def usuarioQR(self, uuid):
		# Consulta datos usuario
		try:
			r_users = requests.get("http://localhost:8080/api/rest/users/" + uuid, headers={"x-hasura-admin-secret":"myadminsecretkey"})
			# Lectura consulta
			dicionarioDatosUsuario = r_users.json()
			datosUsuario = dicionarioDatosUsuario.get('users')

			return datosUsuario

		except requests.exceptions.RequestException:
		    raise requests.exceptions.RequestException

model = Model()
