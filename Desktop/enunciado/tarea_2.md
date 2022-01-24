---
layout: generic
title: "Tarea 2: Diseño sw e implementación"
banner:
  src: "img/pexels-thisisengineering-3861958.jpg"
  copy_url: "https://www.pexels.com/es-es/foto/mujer-codificacion-en-computadora-3861958/"
  copy: "ThisIsEngineering"
---

En esta tarea tienes que realizar la parte central del desarrollo
software: el diseño software y su implementación.


> Recuerda: El desarrollo software es un proceso iterativo. Es normal
> que durante la realización de esta tarea decidas añadir, eliminar o
> modificar partes del diseño de la interface. Si es el caso, no te
> olvides de actualizar los ficheros correspondendientes.


No olvides basar tu diseño software en el patrón _MVC_ (_Model View
Controller_) en caulquiera de sus formas/variantes. Bajo ningún
concepto puedes romper el principio fundamental de separar el modelo
de la vista.

Al contrario de lo que ocurre con el diseño de la interface, para el
diseño sw sí que existe un estándar establecido: UML. Emplea este
lenguaje para crear los diagramas tanto estáticos como
dinámicos. Basándote en tu diseño sw, implementa la aplicación.


No olvides que tu implementación no se limita al _happy path_, también
tiene que gestionar los posibles errores. Por ejemplo, teniendo en
cuenta que la aplicación tiene que conectarse con la BD, algunos
errores esperables son:

  - No es posible conectarse con el servidor.
  
  - El servidor no responde.
  
  - El servidor devuelve un mensaje de error.


## Requisitos

Además de lo indicado en el apartado anterior y en las tareas
anteriores, tienes que cumplir los siguientes requisitos:

  - Los resultados de esta tarea incluyen los diagramas UML y el
    código de la aplicación.
	
  - Los diagramas siguen el estándar UML y se entregan, al menos, en
    formato pdf. Los diagramas pueden estar distribuidos en cualquier
    número de ficheros.
	
  - La aplicación se lanza con el comando `ipm-p1.py`. P.e.:
  
    ```
	$ ./imp-p1.py
	```
	
  - El diseño de la interface está actualizado.

  - Si usas librerías adicionales a Gtk+, incluye la información
    necesaria para su instalación.
  

## Autoevaluación

Para realizar una autoevaluación de esta tarea, puedes guiarte por las
tablas de las tareas anteriores y la siguiente tabla:


| Criterios | Nivel ||
|-----------| ----- |-|
|           |  Bueno | Inadecuado |
| Cumple los requisitos de la lista proporcionada | Cumple todos los requisitos | No cumple algún requisito |
| El diseño sw está bien expresado | Se ajusta al estándar UML y cada artefacto se usa según su significado | No sigue el estándar UML |
| El diseño sw separa modelo e interface | Aplica alguna de las variantes del MVC, o equivalente, para separar modelo e interface | Existen dependencias entre el modelo y la interface |
| El diseño sw incluye diagramas estáticos y dinámicos | Existen diagramas tanto estáticos (p.e diagrama de clases) como dinámicos (p.e. diagrama de secuencia) | Faltan los diagramas estáticos o los dinámicos |
| El diseño sw es suficiente | El diseño incluye todos los elementos necesarios para realizar la implementación | La implementación incluye elementos que no se corresponden con el diseño sw |
| La implementación sigue el diseño de la interface | La interface de la aplicación implementada coincide con el diseño de la interface  | Existen discrepancias entre el diseño de la interface y la implementación |
| La aplicación gestiona los errores | La aplicación captura los errores e informa convenientemente a la usuaria | Los errores provoca mal funcionamiento de la aplicación, son ignorados o no se informa convenientemente a la usuaria |
| La implementación es correcta | Se ejecuta sin fallos en todos los casos | La ejecución falla para algún caso |


> Recuerda que el profesor sólo evaluará los ficheros que están en tu
> repositorio de _github classroom_. Es más seguro que tú también
> autoevalues tu trabajo sobre un _clone_ de ese repositorio.


## Recursos

Necesitas una instalación de
[`python`](https://www.python.org/). Normalmente tu S.O. o
distribución ya tendrá una versión de python instalada por defecto.
Simplemente asegurate de usar una versión reciente. Ahora mismo la
última versión par es la `3.8`, y la impar la `3.9`.

> La siguiente versión `3.10` está en _release candidate_ 1 desde el 3
> de agosto de 2021. No esperes que llegue una versión oficial antes
> de acabar la práctica.

La librería gráfica que tienes que usar para la interface es [Gtk+
3](https://www.gtk.org/). Lo normal es encontrarla empaquetada en casi
cualquier distribución de linux, así que no deberías tener ningún
problema para instalarla. Algunos escritorios como Gnome, Mate, LXDE,
Xfce, ... están basados en Gtk+. Si estás usando alguno de esos
escritorios, ya tendrás instaladas las librerías de Gtk+.

> La última versión mayor de Gtk+ es la 4. Sin embargo, muchas
> distribuciones todavía no lo empaquetan, por eso hemos decidido
> postponer su uso durante este curso.

> BTW, si estás buscando la documentación del api de Gtk+ en python,
> la tienes
> [aquí](https://lazka.github.io/pgi-docs/Gtk-3.0/index.html)


A continuación necesitaras los
[_bindings_](https://en.wikipedia.org/wiki/Language_binding)
correspondientes para poder usar la librería Gtk+ desde tu código
python. Lo más sencillo es usar el [mecanismo
oficial](https://www.gtk.org/docs/language-bindings/): _GObject
Introspection_ (_GI_). Para ellos necesitas el módulo de Gtk+ para GI
y la libería GI para python. De nuevo, lo habitual es que estén
empaquetados en tu distribución de linux. Por ejemplo en debian:

```
$ sudo apt install gir1.2-gtk-3.0 python3-gi
```

Para generar los códigos QR, puedes usar la librería que consideres
oportuna.  Por ejemplo
[python-qrcode](https://github.com/lincolnloop/python-qrcode) está
escrita totalmente en python y está empaquetada en debian como
`python3-qrcode`. Pero también hay otras como `python3-pyqrcode` o
`python3-qrcodegen`.


Por último, pero no menos importante, necesitas un despliegue del
servidor y la base de datos del sistema. Durante la realización de la
práctica, lo más conveniente es que uses tu propio despliegue. El
[repositorio del
servidor](https://github.com/nbarreira/ipm2122-server) incluye toda la
información que necesitas: instrucciones de instalación y ejecución, y
documentación del api.

  
<a href="{{page.url|baseUrl}}tarea_3" class="button big">Siguiente: Tarea 3</a>
