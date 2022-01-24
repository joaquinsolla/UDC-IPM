---
layout: generic
title: ¿ Cómo realizar la práctica ?
banner:
  src: "/img/pexels-christina-morillo-1181622.jpg"
  copy_url: "https://www.pexels.com/es-es/foto/seis-mujeres-de-pie-y-sentadas-dentro-de-la-habitacion-1181622/"
  copy: "Christina Morillo"
---

## Objetivo

En esta práctica tienes que desarrollar una aplicación gráfica de
escritorio, aplicando los conocimientos adquiridos sobre el desarrollo
de interfaces gráficas de usuaria.


## Metodología

La práctica se compone de una serie de tareas que tendrás que realizar
en la secuencia indicada.

Aunque la práctica está dividida en una secuencia de tareas, no hemos
entrado en una máquina del tiempo para viajar a la prehistoria de la
informática y usar una metodología _waterfall_. Durante la realización
de cada una de las tareas es más que probable que tengamos que
actualizar, corregir y/o mejorar algunos de los artefactos
desarrollados en tareas previas.


## Control de versiones

Usaremos un [control de
versiones](https://en.wikipedia.org/wiki/Version_control) durante todo
el desarrollo de la práctica.

Esto quiere decir que, en nuestro directorio de trabajo, de ninguna
manera puede haber distintos ficheros con distintas versiones del
mismo elemento.


## Repositorio

Si estas leyendo esta documentación debería ser porque has creado el
_assignment_ correspondiente en _github classroom_ y por tanto ya
tienes el repositorio necesario para realizar la práctica. Si no es
así, ve al campus virtual y, en la asignatura, sigue el enlace
correspondiente.


## Planificación

A _grosso modo_ la práctica consta de cuatro tareas y tiene estimada
una duración de cuatro semanas. Por tanto la primera aproximación es
de una tarea por semana.

Como parte de los aspectos que se valoran en la realización de la
práctica se encuentra la capacidad para ajustarse a los plazos
establecidos.


Las tareas en que se estructura la práctica son las siguientes:

  * Diseño de la interface
  * Diseño software e implementación
  * Testing
  * Concurrencia
  
  
## Autoevaluación

Cada tarea incluye un apartado con una tabla de guía para la
autoevaluación del trabajo que has realizado. Utiliza esas tablas para
detectar las carencias y fortalezas de tu trabajo.

Estas tablas no son excluyentes. Cada tarea puede incluir aspectos de
las tareas anteriores. Por ejemplo, en la tarea 4, modificarás los
diagramas UML de la tarea 2. Utiliza las tablas de las tareas
anteriores para autoevaluar dichos aspectos.


## Descripción de la aplicación

La aplicación que tienes que desarrollar forma parte de un sistema de
control de accesos covid-19. El sistema consta de los siguientes
contenedores:

- Una B.D. donde se almacena información de las instalaciones,
  entidades, miembros de las entidades, fechas de acceso a las
  instalaciones, etc.
  
- Un servidor que proporciona acceso a la B.D. mediante un api tipo
  REST.
  
- Una aplicación web que permite a las usuarias del sistema las
  operaciones habituales de alta en el sistema, consulta y
  modificación de información personal, etc.
  
- Una aplicación móbil que permite el registro de los accesos a las
  instalaciones mediante códigos QR.
  
- La aplicación de escritorio que desarrollas en esta práctica.

La aplicación realiza consultas directamente a la B.D. y muestra los
resultados, todo a través de una interface gráfica.
 
 
### Usuaria objetivo
    
	Usuaria: IT admin novata.
	
	Una admin experta preferire usar las herramientas CLI y, cuando sea
    necesario, un poco de scripting. Pero los admins novatos se
    sienten más seguros con una herramienta con interface gráfica
    mientras no consoldian su experiencia. Podemos pensar que esta
    herramienta es análoga a los ruedines de una bicicleta.


### Requisitos no funcionales

	Plataforma de ejecución: linux + atspi
	
    Lenguaje de programación: python3
	
	Librería gráfica: Gtk+3
	
	Protocolo para testing: AT-SPI


### Requisitos funcionales

La aplicación incluye los siguientes casos de uso:

	Ver información de una persona
		Permite consultar la información personal: Nombre, Apellidos, Código QR, ... y
		la información de sus accesos a las instalaciones (fecha, horas, tempertura, ...)
		
	Rastrear altertas covid-19
        Permite obtener la lista de personas que compartieron instalación con una determinada
		persona en un período de tiempo (normalmente hasta la fecha actual).
		
Los códigos QR están asociados a una persona e incluyen la siguiente
información: nombre, apellidos, uuid de su entrada en la BD.

    La información incluida en el QR es común para todos los componentes del sistema.
	Es un string con el siguiente formato: "{nombre},{apellidos},{uuid}"
	

<a href="{{page.url|baseUrl}}tarea_1" class="button big">Siguiente: Tarea 1</a>
