import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

import requests
import gettext
import math
import qrcode
import io

class View:

    @classmethod
    def main(cls):
        Gtk.main()

    @classmethod
    def main_quit(cls, w, e):
        Gtk.main_quit()

    # Función que muestra todos los elementos de una ventana

    def show_all(self):
        self.window.show_all()
        self.next.hide()   # Ocultamos la flecha dtextoe avanzamos

    def __init__(self):
        self.textoFallo = "No se puede conectar con la Base de Datos"


    # Función que crea la ventana donde incluiremos los elementos que se muestran por pantalla

    def create_window(self):

        # Creación de la ventana
        self.window = Gtk.Window()
        self.window.set_border_width(10)
        self.window.set_default_size(700,500)

        # Creación de la barra
        self.headerBar = Gtk.HeaderBar()
        self.headerBar.set_show_close_button(True)
        self.headerBar.props.title = "Rastreador Covid"

        # Creación elementos para ir para atrás o para delante
        self.navigationBox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)

        self.previous = Gtk.Button()        # Creación botón flecha para ir página anterior
        self.previous.add(Gtk.Arrow(Gtk.ArrowType.LEFT, Gtk.ShadowType.NONE))

        name = self.previous.get_accessible()       # Variable reutilizada por distintos objetos para asignar un nombre al botón
        name.set_name("Previous_Page")

        self.navigationBox.add(self.previous)

        self.next = Gtk.Button()            # Creación botón flecha para ir página siguiente (en principio estará oculto por defecto)
        self.next.add(Gtk.Arrow(Gtk.ArrowType.RIGHT, Gtk.ShadowType.NONE))

        name = self.next.get_accessible()
        name.set_name("Next_Page")

        self.navigationBox.add(self.next)

        self.headerBar.pack_start(self.navigationBox)

        self.homeButton = Gtk.Button()      # Creación botón home para retornar a la página inicial
        homeImage = Gtk.Image.new_from_file('home.png')

        self.homeButton.add(homeImage)

        name = self.homeButton.get_accessible()
        name.set_name("Home_Button")

        self.headerBar.pack_start(self.homeButton)

        # Creación de spinner que dará un feedback al usuario en el momento de cargar la visualización de una vista

        self.spinner = Gtk.Spinner()

        name = self.spinner.get_accessible()
        name.set_name("Spinner")

        self.headerBar.pack_start(self.spinner)

        self.window.set_titlebar(self.headerBar)

        self.window.set_icon_from_file('icon.png')      # Establecemos el icono de la app

        # Creación de caja que contendrá todos los elementos de dentro (se utilizará como caja global para las distintas vistas)
        self.parentBox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.parentBox.set_spacing(50)

        name = self.parentBox.get_accessible()       # Variable reutilizada por distintos objetos para asignar un nombre al botón
        name.set_name("Parent_Box")

        self.window.add(self.parentBox)

        self.window.show_all()


    # Función que inserta los elementos de la primera vista en la ventana

    def build_ventana_1(self, widget, dataPeople, value):

        # Creación de buscador y label
        searchName = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        searchName.set_spacing(10)

        self.labelName = Gtk.Label()
        self.labelName.set_markup("<big><b>Introduzca el nombre de la persona:</b></big>")       # Creación del texto
        self.labelName.set_xalign(0)
        self.labelName.set_justify(Gtk.Justification(0))

        name = self.labelName.get_accessible()       # Variable reutilizada por distintos objetos para asignar un nombre al botón
        name.set_name("Introducir_Persona_Label")

        searchName.add(self.labelName)

        self.entryBuffer_Name = Gtk.EntryBuffer()    # Creación del buffer para guardar la búsqueda

        self.searchEntry_Name = Gtk.Entry.new_with_buffer(self.entryBuffer_Name)  # Creación del buscador
        self.searchEntry_Name.set_placeholder_text("Nombre de la persona")
        Gtk.Widget.set_size_request(self.searchEntry_Name, 300,15)

        name = self.searchEntry_Name.get_accessible()       # Variable reutilizada por distintos objetos para asignar un nombre al botón
        name.set_name("Buscador_Nombre")

        self.entryBuffer_Surname = Gtk.EntryBuffer()    # Creación del buffer para guardar la búsqueda

        self.searchEntry_Surname = Gtk.Entry.new_with_buffer(self.entryBuffer_Surname)  # Creación del buscador
        self.searchEntry_Surname.set_placeholder_text("Apellido de la persona")
        Gtk.Widget.set_size_request(self.searchEntry_Surname, 400,15)

        name = self.searchEntry_Surname.get_accessible()       # Variable reutilizada por distintos objetos para asignar un nombre al botón
        name.set_name("Buscador_Apellido")

        self.searchButton = Gtk.Button(label="Buscar")
        Gtk.Widget.set_size_request(self.searchButton, 120,15)

        self.searchEntry_Name.get_style_context().add_class('error')
        self.searchEntry_Surname.get_style_context().add_class('error')
        self.searchButton.set_sensitive(False)


        self.entry_Name = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        self.entry_Name.set_spacing(5)

        self.entry_Name.add(self.searchEntry_Name)
        self.entry_Name.add(self.searchEntry_Surname)
        self.entry_Name.add(self.searchButton)

        searchName.add(self.entry_Name)

        self.parentBox.add(searchName)

        # Creación de la tabla para mostrar todas las personas encontradas

        self.listStore = Gtk.ListStore(str, str)    # Creación de la lista que va a contener pares de valores

        for item in dataPeople:
            self.listStore.append(list(item))

        self.boxPeople = Gtk.Box()

        name = self.boxPeople.get_accessible()       # Variable reutilizada por distintos objetos para asignar un nombre al botón
        name.set_name("box_TreeView_Nombres")

        self.treeView = Gtk.TreeView(self.listStore, headers_visible=True)  # Creación de la tabla

        name = self.treeView.get_accessible()       # Variable reutilizada por distintos objetos para asignar un nombre al botón
        name.set_name("treeView_Nombres")

        for i, typeData in enumerate(["Nombre", "Id"]):
            rendererText = Gtk.CellRendererText()
            treeViewColumn = Gtk.TreeViewColumn(typeData, rendererText, text=i)
            self.treeView.append_column(treeViewColumn)

        self.select = self.treeView.get_selection()
        self.boxPeople.pack_start(self.treeView, True, True, 0)

        self.parentBox.add(self.boxPeople)


    # Función que elimina todos los elementos de la caja genérica

    def remove_elements(self):
        boxElements = self.parentBox.get_children()
        for item in boxElements:
            self.parentBox.remove(item)

    # Función que crea los botones de la paginación

    def pagination(self, dataPeople, currentPage, totalPages):

        self.paginationBox = Gtk.Box(orientation= Gtk.Orientation.HORIZONTAL)
        self.parentBox.pack_end(self.paginationBox, False, True, 0)

        self.previousButton = Gtk.Button()      # Creación de botón para mostrar la página de datos anteriores
        self.previousButton.set_label("Anterior")

        name = self.previousButton.get_accessible()       # Variable reutilizada por distintos objetos para asignar un nombre al botón
        name.set_name("Previous_Button_Paginacion")

        self.paginationBox.add(self.previousButton)

        self.entryPositionPagination = Gtk.Entry()

        if len(dataPeople) != 0:
            self.entryPositionPagination.set_text(str(currentPage+1) + "/" + str(totalPages))        # Creación de entrada para saber en que página estamos y de cuantas
        else:
            self.entryPositionPagination.set_text("1/1")        # Creación de entrada en el caso de que no hayamos insertado nada en el buscador

        self.entryPositionPagination.set_width_chars(8)
        self.entryPositionPagination.set_editable(False)        # No permitimos que se cambie el valor de esa entrada
        self.paginationBox.add(self.entryPositionPagination)


        self.nextButton = Gtk.Button()      # Creación de botón para mostrar la página de datos siguientes
        self.nextButton.set_label("Siguiente")

        name = self.nextButton.get_accessible()       # Variable reutilizada por distintos objetos para asignar un nombre al botón
        name.set_name("Next_Button_Paginacion")

        self.paginationBox.add(self.nextButton)


    # Función que crea un diálogo de error
    def dialog_Error(self, texto_fallo):
        self.dialog = Gtk.MessageDialog()     # Creación del diálogo
        self.dialog.set_title("ERROR")
        self.dialog.set_markup(texto_fallo)   # Mensaje del diálogo
        self.dialog.add_button("OK", Gtk.ResponseType.OK)
        if self.dialog.run() == Gtk.ResponseType.OK:
            self.dialog.close()

    #Función que crea un diálogo de excepción
    def dialog_Exception(self):
        self.dialog = Gtk.MessageDialog(message_type=Gtk.MessageType.ERROR)
        self.dialog.set_markup("<b><span foreground='red'>DataBase Error</span></b>" + "\n\n" + self.textoFallo)
        self.dialog.add_button("OK", Gtk.ResponseType.OK)

        if self.dialog.run() == Gtk.ResponseType.OK:
            self.dialog.close()



    def update_view(self, **args):
        for name, value in args.items():
            if name == "search_enable":
                self.searchButton.set_sensitive(value)
            if name == "name_entry":
                self.update_entry_is_valid(self.searchEntry_Name, value)
            if name == "surname_entry":
                self.update_entry_is_valid(self.searchEntry_Surname, value)
            if name == "search_rastreador":
                self.button_BuscarRastreador.set_sensitive(value)
            if name == "rastreador_entry":
                self.update_entry_is_valid(self.fechaInicio, value)

    def update_entry_is_valid(self, entry, is_valid):
        if is_valid:
            entry.get_style_context().remove_class('error')
        else:
            entry.get_style_context().add_class('error')

    # CONNECTORS VENTANA 1:

    # Conectamos el cierre de la ventana

    def connect_delete_event(self, fun):
        self.window.connect("delete-event", fun)

    # Conectamos el home de la ventana

    def connect_home_button(self, fun):
        self.homeButton.connect("clicked", fun)

    # Conectamos la barra de búsqueda

    def connect_search_clicked(self, fun):
        self.searchButton.connect("clicked", fun)


    # Conectamos el entry por si cambia su valores
    def connect_name_changed(self, fun):
        self.searchEntry_Name.connect("changed", fun)

    def connect_surname_changed(self, fun):
        self.searchEntry_Surname.connect("changed", fun)

    #Conectamos la selección de un nombre

    def connect_selection_clicked(self, fun):
        self.select.connect("changed", fun)

    # Conectamos el botón para ir a la vista anterior

    def connect_previous_clicked_1(self, fun):
        self.previous.connect("clicked", fun)
    # END CONNECTORS VENTANA 1


    # Función que inserta los elementos de la segunda vista en la ventana

    def build_ventana_2(self, datosUsuario, dataActividadReciente):

        # Creación de una box para organizar la primera mitad de la página
        self.boxPeopleInfo = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.boxPeopleInfo.set_spacing(10)
        self.parentBox.add(self.boxPeopleInfo)

        # Creación de una box para los datos de la persona buscada

        self.labelDataTitle = Gtk.Label()
        self.labelDataTitle.set_markup("<big><b>Datos personales:</b></big>")    # Creación de un campo de texto
        self.labelDataTitle.set_xalign(0)

        name = self.labelDataTitle.get_accessible()       # Variable reutilizada por distintos objetos para asignar un nombre al botón
        name.set_name("Datos_Personales_label")

        self.boxPeopleInfo.add(self.labelDataTitle)

        self.boxPersonalData = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        self.boxPersonalData.set_spacing(50)

        name = self.boxPersonalData.get_accessible()       # Variable reutilizada por distintos objetos para asignar un nombre al botón
        name.set_name("Datos_Personales_Box")

        self.boxPeopleInfo.add(self.boxPersonalData)

        qr_data = "Nombre: \n" + datosUsuario[0].get("name") + " " + datosUsuario[0].get("surname") + "\n\n" + "Uuid: \n" + datosUsuario[0].get("uuid")     # Datos utilizados para elaborar el QR
        self.generar_qr(qr_data, True)
        self.qrImage = Gtk.Image.new_from_file('myqr.png')

        name = self.qrImage.get_accessible()
        name.set_name("QR")

        self.boxPersonalData.add(self.qrImage)

        boxPersonalData_aux = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        boxPersonalData_aux.set_spacing(10)

        self.boxPersonalData.add(boxPersonalData_aux)

        self.labelNombre = Gtk.Label()
        self.labelNombre.set_markup("<b>Nombre: </b>" + datosUsuario[0].get("name") + " " + datosUsuario[0].get("surname"))      # Insertamos el nombre y apellido de la persona buscada
        self.labelNombre.set_xalign(0)

        name = self.labelName.get_accessible()       # Variable reutilizada por distintos objetos para asignar un nombre al botón
        name.set_name("Nombre_Label")

        boxPersonalData_aux.add(self.labelNombre)

        self.labelUuid = Gtk.Label()
        self.labelUuid.set_markup("<b>Uuid: </b>" + datosUsuario[0].get("uuid"))     # Insertamos el uuid de la persona buscada
        self.labelUuid.set_xalign(0)

        name = self.labelUuid.get_accessible()       # Variable reutilizada por distintos objetos para asignar un nombre al botón
        name.set_name("Uuid_Label")

        boxPersonalData_aux.add(self.labelUuid)

        self.labelCorreo = Gtk.Label()
        self.labelCorreo.set_markup("<b>Dirección de Correo: </b>" + datosUsuario[0].get("email"))       # Insertamos el email de la persona buscada
        self.labelCorreo.set_xalign(0)

        name = self.labelCorreo.get_accessible()       # Variable reutilizada por distintos objetos para asignar un nombre al botón
        name.set_name("Correo_Label")

        boxPersonalData_aux.add(self.labelCorreo)

        boxPersonalData_aux2 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        boxPersonalData_aux2.set_spacing(10)
        self.boxPersonalData.add(boxPersonalData_aux2)

        self.labelVacunado = Gtk.Label()
        self.labelVacunado.set_markup("<b>Vacunado: </b>" + str(datosUsuario[0].get("is_vaccinated")))       # Insertamos si está o no vacunado la persona buscada

        name = self.labelVacunado.get_accessible()       # Variable reutilizada por distintos objetos para asignar un nombre al botón
        name.set_name("Vacunado_Label")
        self.labelVacunado.set_xalign(0)

        boxPersonalData_aux2.add(self.labelVacunado)

        self.labelTelefono = Gtk.Label()
        self.labelTelefono.set_markup("<b>Teléfono: </b>" + datosUsuario[0].get("phone"))        # Insertamos el contacto de la persona buscada
        self.labelTelefono.set_xalign(0)

        name = self.labelTelefono.get_accessible()       # Variable reutilizada por distintos objetos para asignar un nombre al botón
        name.set_name("Telefono_Label")

        boxPersonalData_aux2.add(self.labelTelefono)

        # Creación de una box para organizar los datos en la mitad de abajo de la pantalla

        boxActividadRastreador = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        boxActividadRastreador.set_spacing(10)
        self.parentBox.add(boxActividadRastreador)

        # Creación de una box para organizar los datos de actividad reciente

        self.boxActividad = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.boxActividad.set_spacing(10)

        name = self.boxActividad.get_accessible()       # Variable reutilizada por distintos objetos para asignar un nombre al botón
        name.set_name("Actividad_Box")

        boxActividadRastreador.add(self.boxActividad)

        self.labelActividad = Gtk.Label()
        self.labelActividad.set_markup("<big><b>Actividad Reciente:</b></big>")      # Creación de un campo de texto
        self.labelActividad.set_xalign(0)
        self.labelActividad.set_line_wrap(True)

        name = self.labelActividad.get_accessible()       # Variable reutilizada por distintos objetos para asignar un nombre al botón
        name.set_name("Actividad_Label")

        self.boxActividad.add(self.labelActividad)

        # Creación de una box para los datos a mostrar en la tabla de Actividad Reciente

        self.boxTablaActividad = Gtk.Box()
        self.boxActividad.add(self.boxTablaActividad)

        listActividad  = Gtk.ListStore(str,str,str, str)     # Creación de una lista de tríos de valores

        for item in dataActividadReciente:
            listActividad.append(list(item))

        self.treeView = Gtk.TreeView(listActividad, headers_visible=True)

        name = self.treeView.get_accessible()       # Variable reutilizada por distintos objetos para asignar un nombre al botón
        name.set_name("treeView_ActividadReciente")

        for i, typeData in enumerate(["Nombre del Centro", "Temperatura", "Fecha y Hora", "Tipo"]):      # Creamos las cabeceras de la tabla
            rendererText = Gtk.CellRendererText()
            treeViewColumn = Gtk.TreeViewColumn(typeData, rendererText, text=i)
            self.treeView.append_column(treeViewColumn)

        self.boxTablaActividad.pack_start(self.treeView, True, True, 0)

        self.button_MostrarTodoActividad = Gtk.Button(label="Mostrar Todo")         # Creamos el botón que nos llevará a la vista_3 (muestra toda la actividad de una persona)

        name = self.button_MostrarTodoActividad.get_accessible()       # Variable reutilizada por distintos objetos para asignar un nombre al botón
        name.set_name("button_MostrarTodoActividad")

        self.boxActividad.add(self.button_MostrarTodoActividad)

        # Creación de una box para organizar el formulario de Rastreador

        self.boxRastreador = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.boxRastreador.set_spacing(10)

        name = self.boxRastreador.get_accessible()       # Variable reutilizada por distintos objetos para asignar un nombre al botón
        name.set_name("Rastreador_Box")

        boxActividadRastreador.add(self.boxRastreador)

        self.labelTituloRastreador = Gtk.Label()
        self.labelTituloRastreador.set_markup("<big><b>Rastreador:</b></big>")           # Creación de un campo de texto
        self.labelTituloRastreador.set_xalign(0)

        name = self.labelTituloRastreador.get_accessible()       # Variable reutilizada por distintos objetos para asignar un nombre al botón
        name.set_name("RastreadorTitulo_Label")

        self.boxRastreador.add(self.labelTituloRastreador)

        self.labelFechaInicio = Gtk.Label(label= "Introduzca la fecha y hora desde la que desea rastrear:", xalign=0)

        name = self.labelFechaInicio.get_accessible()       # Variable reutilizada por distintos objetos para asignar un nombre al botón
        name.set_name("FechaInicio_Label")

        self.boxRastreador.add(self.labelFechaInicio)

        self.bufferFInicio=Gtk.EntryBuffer()
        self.fechaInicio = Gtk.Entry.new_with_buffer(self.bufferFInicio)        # Creación de entrada con buffer para escribir el valor de la fecha inicial de la búsqueda
        self.fechaInicio.set_placeholder_text("aaaa/mm/dd hh:mm:ss")

        name = self.fechaInicio.get_accessible()       # Variable reutilizada por distintos objetos para asignar un nombre al botón
        name.set_name("FechaInicio_Entry")

        self.fechaInicio.get_style_context().add_class('error')

        self.boxRastreador.add(self.fechaInicio)

        self.labelFechaFinal = Gtk.Label(label= "Introduzca la fecha y hora hasta la que desea rastrear:", xalign=0)

        name = self.labelFechaFinal.get_accessible()       # Variable reutilizada por distintos objetos para asignar un nombre al botón
        name.set_name("FechaFinal_Label")

        self.boxRastreador.add(self.labelFechaFinal)

        self.bufferFFinal=Gtk.EntryBuffer()
        self.fechaFinal = Gtk.Entry.new_with_buffer(self.bufferFFinal)          # Creación de entrada con buffer para escribir el valor de la fecha final de la búsqueda
        self.fechaFinal.set_placeholder_text("aaaa/mm/dd hh:mm:ss")

        name = self.fechaFinal.get_accessible()       # Variable reutilizada por distintos objetos para asignar un nombre al botón
        name.set_name("FechaFinal_Entry")

        self.boxRastreador.add(self.fechaFinal)

        self.button_BuscarRastreador = Gtk.Button(label="Buscar")       # Creación del botón que nos llevará a la vista_4 en el caso de que la búsqueda tenga los parámetros correctos
        self.button_BuscarRastreador.set_sensitive(False)
        name = self.button_BuscarRastreador.get_accessible()       # Variable reutilizada por distintos objetos para asignar un nombre al botón
        name.set_name("button_BuscarRastreador")

        self.boxRastreador.add(self.button_BuscarRastreador)

    # Función que genera el código qr a partir de los datos pasados en myData

    def generar_qr(self, myData, qrPersonaBuscada):
        qr = qrcode.QRCode(
            version=1,
            box_size=3,
            border=1)

        qr.add_data(myData)
        qr.make(fit=True)

        try:
            img = qr.make_image(fill='black', back_color='white')
            if(qrPersonaBuscada):
                img.save('myqr.png')
            else:
                img.save('contacto.png')

        except IOError:
            print("cannot create thumbnail for", "myqr.png")


    # CONNECTORS VENTANA 2:

    # Conectamos el botón de mostrar toda la actividad de la persona buscada

    def connect_show_all(self, fun):
        self.button_MostrarTodoActividad.connect("clicked", fun)

    # Conectamos el botón para realizar la búsqueda entre dos parámetros (fecha inicio y fecha fin) de los contactos de una persona

    def connect_search(self, fun):
        self.button_BuscarRastreador.connect("clicked", fun)

    # Conectamos el botón para ir a la vista anterior

    def connect_previous_clicked_2(self, fun):
        self.previous.connect("clicked", fun)

    # Conectamos la entrada de la fecha de inicio para saber cuando se producen cambios

    def connect_fechaInicio_changed(self, fun):
        self.fechaInicio.connect("changed", fun)


    # END CONNECTORS VENTANA 2


    # Función que inserta los elementos de la tercera vista en la ventana

    def build_ventana_3(self, dataActividadRecienteTotal, currentPage, totalPages):

        # Creación de box para la tabla

        self.labelHistorialActividad = Gtk.Label()
        self.labelHistorialActividad.set_markup("<big><b>Historial Actividad:</b></big>")        # Creación de campo texto
        self.labelHistorialActividad.set_xalign(0)

        name = self.labelHistorialActividad.get_accessible()       # Variable reutilizada por distintos objetos para asignar un nombre al botón
        name.set_name("historialActividad_label")

        self.parentBox.add(self.labelHistorialActividad)

        self.listActividadTotal = Gtk.ListStore(str, str, str, str, str)        # Creación de una lista de quintetos de valores

        for x in range(currentPage*10, currentPage*10 + 10):
            if (x<len(dataActividadRecienteTotal)):
                self.listActividadTotal.append(dataActividadRecienteTotal[x])

        self.treeView = Gtk.TreeView(self.listActividadTotal, headers_visible=True)

        name = self.treeView.get_accessible()       # Variable reutilizada por distintos objetos para asignar un nombre al botón
        name.set_name("treeView_HistorialActividad")

        for i, typeData in enumerate(["Id_Centro", "Nombre de centro", "Temperatura", "Fecha y hora", "Tipo"]):      # Establecemos las cabeceras de la tabla
            rendererText = Gtk.CellRendererText()
            treeViewColumn = Gtk.TreeViewColumn(typeData, rendererText, text=i)
            self.treeView.append_column(treeViewColumn)

        self.select_Ubicacion = self.treeView.get_selection()

        self.parentBox.pack_start(self.treeView, True, True, 0)

        self.pagination(self.listActividadTotal, currentPage, totalPages)


    def show_dataUbicacion(self, datosUbicacion):

        dialog = Gtk.MessageDialog(
                            message_type = Gtk.MessageType.INFO,
                            buttons = Gtk.ButtonsType.OK)


        dialog.set_markup("<b>Nombre: </b>" + datosUbicacion[0].get("name") +
                            "\n<b>Id: </b>" + str(datosUbicacion[0].get("id")) +
                            "\n<b>Dirección: </b>" + datosUbicacion[0].get("address") +
                            "\n<b>Capacidad Máxima: </b>" + str(datosUbicacion[0].get("max_capacity")) +
                            "\n<b>Porcentaje de capacidad permitida: </b>" + str(datosUbicacion[0].get("percentage_capacity_allowed")) + "%")

        mapaUbicacion = Gtk.Image.new_from_file('ubicacion.jpg')

        dialog.set_image(mapaUbicacion)
        dialog.show_all()
        dialog.run()
        dialog.destroy()
    # CONNECTORS VENTANA 3:

    # Conectamos el botón para ir a la vista anterior

    def connect_previous_clicked_3(self, fun):
        self.previous.connect("clicked", fun)

    def connect_next_page_clicked_3(self, fun):
        self.nextButton.connect("clicked", fun)

    def connect_previous_page_clicked_3(self, fun):
        self.previousButton.connect("clicked", fun)

    #Conectamos la selección de un nombre
    def connect_selection_clickedUbicacion(self, fun):
        self.select_Ubicacion.connect("changed", fun)

    # END CONNECTORS VENTANA 3


    # Función que inserta los elementos de la cuarta vista en la ventana

    def build_ventana_4(self, nombreContactoDe, contactosUsuario, currentPage, totalPages):

        # Creación de box para la tabla

        self.labelHistorialRastreado = Gtk.Label()
        #self.labelHistorialRastreado.set_markup("<big><b>Contactos de " + datosUsuario[0].get("name") + " " + datosUsuario[0].get("surname") + ":</b></big>")    # Creación de campo texto con los datos del usuario buscado
        #self.labelHistorialRastreado.set_markup("<big><b>Contactos de " + datosUsuario[0][0] + ":</b></big>")    # Creación de campo texto con los datos del usuario buscado
        self.labelHistorialRastreado.set_markup("<big><b>Contactos de " + nombreContactoDe + ":</b></big>")    # Creación de campo texto con los datos del usuario buscado

        self.labelHistorialRastreado.set_xalign(0)

        name = self.labelHistorialRastreado.get_accessible()       # Variable reutilizada por distintos objetos para asignar un nombre al botón
        name.set_name("label_HistorialRastreado")

        self.parentBox.add(self.labelHistorialRastreado)

        self.list_Rastreado = Gtk.ListStore(str, str, str)      # Creación de una lista de heptetos

        #contactosUsuario.pop(0)
        for x in range(currentPage*10, currentPage*10 + 10):
            if (x<len(contactosUsuario)):
                self.list_Rastreado.append(contactosUsuario[x])

        self.treeView = Gtk.TreeView(self.list_Rastreado, headers_visible=True)

        name = self.treeView.get_accessible()       # Variable reutilizada por distintos objetos para asignar un nombre al botón
        name.set_name("treeView_Rastreado")

        for i, typeData in enumerate(["Nombre Ap1 Ap2", "Uuid", "Contacto"]):    # Establecemos las cabeceras de la tabla
            rendererText = Gtk.CellRendererText()
            treeViewColumn = Gtk.TreeViewColumn(typeData, rendererText, text=i)
            self.treeView.append_column(treeViewColumn)

        self.select_Contacto = self.treeView.get_selection()
        self.parentBox.pack_start(self.treeView, True, True, 0)

        self.pagination(self.list_Rastreado, currentPage, totalPages)


    def show_qr_Contacto(self, datosContacto):
        qr_data = "Nombre: \n" + datosContacto[0].get("name") + " " + datosContacto[0].get("surname") + "\n\n" + "Uuid: \n" + datosContacto[0].get("uuid")     # Datos utilizados para elaborar el QR
        self.generar_qr(qr_data, False)
        qrContacto = Gtk.Image.new_from_file('contacto.png')

        dialog = Gtk.MessageDialog(
                            message_type = Gtk.MessageType.INFO,
                            buttons = Gtk.ButtonsType.OK)


        dialog.set_markup("<b>Nombre: </b>" + datosContacto[0].get("name") + " " + datosContacto[0].get("surname") +
                            "\n<b>Uuid: </b>" + datosContacto[0].get("uuid") +
                            "\n<b>Dirección de Correo: </b>" + datosContacto[0].get("email") +
                            "\n<b>Vacunado: </b>" + str(datosContacto[0].get("is_vaccinated")) +
                            "\n<b>Teléfono: </b>" + datosContacto[0].get("phone"))

        dialog.set_image(qrContacto)
        dialog.show_all()
        dialog.run()
        dialog.destroy()



    # CONNECTORS VENTANA 4:

    # Conectamos el botón para ir a la vista anterior

    def connect_previous_clicked_4(self, fun):
        self.previous.connect("clicked", fun)

    def connect_next_page_clicked_4(self, fun):
        self.nextButton.connect("clicked", fun)

    def connect_previous_page_clicked_4(self, fun):
        self.previousButton.connect("clicked", fun)

    #Conectamos la selección de un nombre

    def connect_selection_clickedContacto(self, fun):
        self.select_Contacto.connect("changed", fun)

    # END CONNECTORS VENTANA 4

view = View()
