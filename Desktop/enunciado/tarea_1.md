---
layout: generic
title: "Tarea 1: Diseño de la interface"
banner:
  src: "img/pexels-picjumbocom-196644.jpg"
  copy_url: "https://www.pexels.com/es-es/foto/cuaderno-junto-al-iphone-en-la-mesa-196644/"
  copy: "picjumbo.com"
---

Tu primera tarea es diseñar la interface gráfica de la aplicación que
vas a desarrollar.


Como ya hemos visto en clase, no existe ningún standard ni oficial, ni
_de facto_ para representar el diseño de una interface gráfica. Para
esta ocasión vamos a continuar con las pautas definidas en clase.

Aunque en esta tarea no tienes que realizar un diseño de UX completo,
sí que tienes que tener el cuenta la _usuaria objetivo_ a la hora de
realizar el diseño.

También tienes que tener en cuenta que la principal operación que
realizará la usuaria es la consulta a la base de datos. Como ya
sabemos una base de datos suele almacenar una cantidad de datos
enormes, lo que provoca que muchas veces el resultado de una consulta:

  - No se puede almacenar en memoria. Esta limitación ya sabemos
    resolverla con el uso de _cursores_ o mecanismos equivalentes.
	
  - No es posible mostrar todos los datos a la vez en la interface
    gráfica.
	
Para el segundo problema tienes que plantear una solución y aplicarla
al diseño de la interface:

  - Documéntate (google es tu amigo) para conocer las distintas
    opciones que existen: paginación, scroll infinito, ...
	
  - Escribe una lista con las distintas opciones que encuentres, sus
    ventajas e inconvenientes.
	
  - Selecciona la opción que consideres más adecuada, justifícala y
    aplicala al diseño.


## Requisitos

Recopilando lo visto hasta ahora, el diseño tiene que cumplir los
siguientes requisitos:

  - Representación esquemática, _sketches_, de cada una de las
    ventanas.
	
  - Diseño de baja fidelidad en blanco y negro, o escala de
    grises. Puede estar realizado a mano, empleando un software de
    dibujo, ... En ningún caso pueden estar formado por pantallazos
    (_screenshots_) de la aplicación, o representaciones "realistas"
    de los componentes de la interface.
	
  - El diseño debe incluir las anotaciones necesarias para mostrar
    cómo se realiza la interacción para cada una de las historias
    incluidas en los requisitos de la aplicación.

  - El diseño debe incluir un documento/lista adicional donde se
    enumeran las distintas soluciones al problema descrito para
    mostrar los resultados de las consultas a la BD, junto con sus
    _pros_ y _contras_, y la justificación para la opción seleccionada
    y aplicada al diseño.

  - El diseño se entregará, al menos, en un documento en formato pdf.


## Autoevaluación

Para realizar una autoevaluación de esta tarea, puedes guiarte por la
siguiente tabla:


| Criterios | Nivel ||
|-----------| ----- |-|
|           |  Bueno | Inadecuado |
| Cumple los requisitos de la lista proporcionada | Cumple todos los requisitos | No cumple algún requisito |
| Tiene en cuenta la usuaria objetivo | La complejidad de los componentes y su interacción es adecuada para la experiencia de la usuaria y como contrapartida facilita la interacción en cada una de las historias de usuaria | Los componentes son sencillos, pero no son eficaces, o son demasiado complejos |
| Resuelve el problema de la cantidad de datos | Cuando no se pueden mostrar todos los datos al mismo tiempo, existe una forma satisfactoria de navegar entre ellos | La forma de navegar entre los datos no es eficaz, no permite una visión global o no permite recuperar la información fácilmente |


> Recuerda que el profesor sólo evaluará los ficheros que están en tu
> repositorio de _github classroom_. Es más seguro que tú también
> autoevalues tu trabajo sobre un _clone_ de ese repositorio.


<a href="{{page.url|baseUrl}}tarea_2" class="button big">Siguiente: Tarea 2</a>
