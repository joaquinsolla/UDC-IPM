import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GLib, GObject

import math
#import time
import requests

class Controller:

    def set_model(self, model):
        self.model = model

    def set_view(self, view):
        self.view = view
        self.view.create_window()
        self.build_window_1([])

    def main(self):
        self.view.show_all()
        self.view.main()

    def __init__(self):
        self.currentPage = 2
        self.busquedaUsuario = []
        self.datosUsuario = []
        self.actividadRecienteUsuario = []
        self.historialActividadUsuario = []
        self.currentUUID = None
        self.nombreContactoDe = None
        self.contactosUsuario = []
        self.datosContacto = []
        self.datosUbicacion = []


    #Función que inicializa la vista

    def build_window_1(self, vector):
        self.view.remove_elements()
        self.view.build_ventana_1(None, vector, self.currentPage)
        self.view.show_all()
        self.view.connect_delete_event(self.view.main_quit)
        self.view.connect_home_button(self.home_window)
        self.view.connect_search_clicked(self.searchClicked)
        self.view.connect_selection_clicked(self.personClicked)
        self.view.connect_name_changed(self.update_view1)
        self.view.connect_surname_changed(self.update_view1)
        self.view.connect_previous_clicked_1(self.home_window)
        self.currentPage=0

    def searchClicked(self, widget):
        self.window_1()

    def window_1(self):
        try:
            self.searchPeople()
        except requests.exceptions.RequestException:
            self.view.dialog_Exception()

            return

        if self.busquedaUsuario==[]:
            self.view.dialog_Error("No se encuentra ningún resultado con este parámetro de búsqueda")

        else:
            self.build_window_1(self.busquedaUsuario)


    def searchPeople(self):
        self.busquedaUsuario = self.model.busquedaUsuario(self.view.entryBuffer_Name.get_text().strip(),self.view.entryBuffer_Surname.get_text().strip())

    def home_window(self, widget):
        self.build_window_1([])


    def personClicked(self, widget):
        self.window_2()

    def window_2(self):
        try:
            self.dataUsuario()

        except requests.exceptions.RequestException:
            self.view.dialog_Exception()

            return

        self.build_window_2()

    def dataUsuario(self):
        conjunto, seleccionado = self.view.treeView.get_selection().get_selected()  # Nos permite saber lo que hemos seleccionado
        if seleccionado is not None:
            self.currentUUID = conjunto[seleccionado][1]
            self.datosUsuario = self.model.datosUsuario(self.currentUUID)
            self.actividadRecienteUsuario = self.model.actividadRecienteUsuario(self.currentUUID)


    def update_view1(self, widget, **kwargs):
        name = self.view.entryBuffer_Name.get_text().strip() != ""
        surname = self.view.entryBuffer_Surname.get_text().strip() != ""
        enabled_button = name and surname
        self.view.update_view(search_enable=enabled_button, name_entry = name, surname_entry = surname, **kwargs)

    def build_window_2(self):
        self.view.remove_elements()
        self.view.build_ventana_2(self.datosUsuario, self.actividadRecienteUsuario)
        self.view.show_all()
        self.view.connect_show_all(self.mostrar_Todo)
        self.view.connect_search(self.rastrear_Persona)
        self.view.connect_previous_clicked_2(self.previous_View_1)
        self.view.connect_fechaInicio_changed(self.update_view2)
        self.currentPage=0

    def update_view2(self, widget, **kwargs):
        fechaInicio = self.view.bufferFInicio.get_text().strip() != ""
        enabled_button = fechaInicio
        self.view.update_view(search_rastreador=enabled_button, rastreador_entry = fechaInicio, **kwargs)

    def previous_View_1(self, widget):
        self.build_window_1(self.busquedaUsuario)

    def mostrar_Todo(self, widget):
        self.window_3()

    def window_3(self):
        try:
            self.historialUsuario()
            self.build_window_3()
        except requests.exceptions.RequestException:
            self.view.dialog_Exception()


    def historialUsuario(self):
        if self.currentUUID is not None:
            self.historialActividadUsuario = self.model.historialActividadUsuarios(self.currentUUID)
        else:
            print("currentUUID is None")

    def next_page_3(self, widget):
        if(self.currentPage < (math.ceil(len(self.historialActividadUsuario)/10))-1):
            self.currentPage = self.currentPage+1
            self.build_window_3()

    def previous_page_3(self, widget):
        if(self.currentPage > 0):
            self.currentPage = self.currentPage-1
            self.build_window_3()

    def build_window_3(self):
        self.view.remove_elements()
        self.view.build_ventana_3(self.historialActividadUsuario, self.currentPage, math.ceil(len(self.historialActividadUsuario)/10))
        self.view.show_all()
        self.view.connect_next_page_clicked_3(self.next_page_3)
        self.view.connect_previous_page_clicked_3(self.previous_page_3)
        self.view.connect_previous_clicked_3(self.previous_View_2)
        self.view.connect_selection_clickedUbicacion(self.show_dataUbicacion)

    def previous_View_2(self, widget):
        self.build_window_2()


    def show_dataUbicacion(self, widget):
        self.build_dialog_ubicacion()

    def obtenerDatosUbicacion(self):
        conjunto, seleccionado = self.view.treeView.get_selection().get_selected()  # Nos permite saber lo que hemos seleccionado
        if seleccionado is not None:
            self.datosUbicacion = self.model.dataUbicacion(conjunto[seleccionado][0])

    def build_dialog_ubicacion(self):
        try:
            self.obtenerDatosUbicacion()
            self.view.show_dataUbicacion(self.datosUbicacion)

        except requests.exceptions.RequestException:
            self.view.dialog_Exception()




    def rastrear_Persona(self, widget):
        self.window_4()


    def window_4(self):
        try:
            if self.rastreador():
                self.view.dialog_Error("Las fechas introducidas no son correctas")

            else:
                self.build_window_4()
        except requests.exceptions.RequestException:
            self.view.dialog_Exception()

    def rastreador(self):
        fechaI= self.view.bufferFInicio.get_text().strip()
        fechaF= self.view.bufferFFinal.get_text().strip()
        errorFechas= self.checkFechaS(fechaI, fechaF)
        if errorFechas:
            return errorFechas
        else:
            if self.currentUUID is not None:
                self.contactosUsuario = self.model.contactos(self.currentUUID, fechaI, fechaF)
                self.nombreContactoDe = self.datosUsuario[0].get("name") + " " + self.datosUsuario[0].get("surname")

            else:
                print("currentUUID is None")
        return errorFechas

    def checkFechaS(self, fechaI, fechaF):
        error = False
		# Comprobamos las fechas:
        if (self.comprobarFormatoFecha(fechaI)==0):
            error = True

        if fechaF != "":
            if (self.comprobarFormatoFecha(fechaF)==0):
                error = True
            if (fechaI>=fechaF):
                error = True
        return error

    # Función que comprueba que el formato de la fecha introducida es correcta
    def comprobarFormatoFecha(self, fechaOriginal):

        numbers = fechaOriginal[0:4].isnumeric() and fechaOriginal[5:7].isnumeric() and fechaOriginal[8:10].isnumeric() and fechaOriginal[11:13].isnumeric() and fechaOriginal[14:16].isnumeric() and fechaOriginal[17:19].isnumeric()
        symbols = fechaOriginal[4:5]=="/" and fechaOriginal[7:8]=="/" and fechaOriginal[10:11]==" " and fechaOriginal[13:14]==":" and fechaOriginal[16:17]==":"
        longitud = len(fechaOriginal)==19
        dateLimits = fechaOriginal[0:4]>="2000" and fechaOriginal[5:7]<="12" and fechaOriginal[5:7]>="01" and fechaOriginal[8:10]>="01" and fechaOriginal[8:10]<="31"
        hourLimits = fechaOriginal[11:13]<="23" and fechaOriginal[11:13]>="00" and fechaOriginal[14:16]<="59" and fechaOriginal[14:16]>="00" and fechaOriginal[17:19]>="00" and fechaOriginal[17:19]<="59"

        return (numbers and symbols and longitud and dateLimits and hourLimits)		# Devuelve True si es correcta


    def next_page_4(self, widget):
        if(self.currentPage < (math.ceil(len(self.contactosUsuario)/10))-1):
            self.currentPage = self.currentPage+1
            self.build_window_4()


    def previous_page_4(self, widget):
        if(self.currentPage > 0):
            self.currentPage = self.currentPage-1
            self.build_window_4()


    def build_window_4(self):
        self.view.remove_elements()
        self.view.build_ventana_4(self.nombreContactoDe, self.contactosUsuario, self.currentPage, math.ceil(len(self.contactosUsuario)/10))
        self.view.show_all()
        self.view.connect_next_page_clicked_4(self.next_page_4)
        self.view.connect_previous_page_clicked_4(self.previous_page_4)
        self.view.connect_previous_clicked_4(self.previous_View_22)
        self.view.connect_selection_clickedContacto(self.show_qr_Contacto)


    def previous_View_22(self, widget):
        self.build_window_2()

    def show_qr_Contacto(self, widget):
        self.build_dialog_contacto()

    def obtenerDatosContacto(self):
        conjunto, seleccionado = self.view.treeView.get_selection().get_selected()  # Nos permite saber lo que hemos seleccionado
        if seleccionado is not None:
            self.datosContacto = self.model.usuarioQR(conjunto[seleccionado][1])

    def build_dialog_contacto(self):
        try:
            self.obtenerDatosContacto()
            self.view.show_qr_Contacto(self.datosContacto)

        except requests.exceptions.RequestException:
            self.view.dialog_Exception()
