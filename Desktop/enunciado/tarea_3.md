---
layout: generic
title: "Tarea 3: Testing"
banner:
  src: "img/automation.jpg"
  copy_url: ""
  copy: "unkown"
---

En esta tarea tienes que escribir pruebas automatizadas _e2e_ (_end to
end_) para tu aplicación. Implementa las pruebas usando el api
[_AT-SPI_](https://en.wikipedia.org/wiki/Assistive_Technology_Service_Provider_Interface).

> Recuerda: El desarrollo software es un proceso iterativo. Si alguna
> de las pruebas detecta un error en la aplicación, no te olvides de
> corregirlo.

Puedes usar una herramienta de ejecución de pruebas como `unittest` o
`pytest`, o implementar las pruebas desde cero.

Recuerda que una característica necesaria de una prueba es ser
independiente. Eso quiere decir que cada prueba tiene que arrancar y
terminar la aplicación, dejando el sistema en el estado en que estaba
antes de la prueba.

Otra característica necesaria de una prueba es ser válida para las
futuras versiones de la aplicación. Como vimos en clase, eso quiere
decir que tienes que evitar implementaciones como la siguiente:

```python
obj = app.get_child_at(0).get_child_at(2).get_child_at(1)
```

porque la prueba dejará de ser válida en cuanto cambie el
diseño/implementación de la interface. Recuerda que ese cambio,
probablemente, implica un cambio en el árbol de widgets.


## Requisitos

Además de lo indicado en el apartado anterior y en las tareas
anteriores, tienes que cumplir los siguientes requisitos:

  - Los resultados de esta tarea incluyen el
    código de las pruebas.
	
  - Las pruebas con el comando `run-tests.sh`. P.e.:
  
    ```
	$ ./run-tests.sh
	```
	
  - Si se detecto algún error, la implementación está corregida.
  

## Autoevaluación

Para realizar una autoevaluación de esta tarea, puedes guiarte por las
tablas de las tareas anteriores y la siguiente tabla:


| Criterios | Nivel ||
|-----------| ----- |-|
|           |  Bueno | Inadecuado |
| Cumple los requisitos de la lista proporcionada | Cumple todos los requisitos | No cumple algún requisito |
| Las pruebas son completas | Incluyen pruebas positivas y negativas | Sólo se incluyen pruebas positivas |
| Las pruebas son completas | Se prueban todas las historias de usuaria indicadas | No hay pruebas para alguna de las historias de usuaria |
| Las pruebas son resistentes | No inluyen código que se rompa con versiones posteriores de la interface | El código es quebradizo y romperá cuando cambie el árbol de widgets de la interface |
| Las pruebas usan el api adecuado | Usan el api indicado en el enunciado (at-spi) | Se usan otros api/herramientas para simular la interación de la usuaria |


> Recuerda que el profesor sólo evaluará los ficheros que están en tu
> repositorio de _github classroom_. Es más seguro que tú también
> autoevalues tu trabajo sobre un _clone_ de ese repositorio.


## Recursos

Necesitas tener funcionando el [servicio
_AT-SPI_](https://www.freedesktop.org/wiki/Accessibility/AT-SPI2/) en
tu S.O. La manera de conseguirlo dependerá de tu distribución. Por
ejemplo, si estás usando _Gnome_, ya debería estar funcionando. Sino,
por ejemplo en debian tendrías que instalar el paquete correspondiente:

```
$ sudo apt install at-spi2-core
```

También necesitarás usar el api de AT-SPI directamente desde
python. Al igual que ocurre con _Gtk+_, lo más sencillo es usar
_GObject Introspection_ (_GI_). Para ellos necesitas el módulo de
AT-SPI para GI y la libería GI para python. Por ejemplo en debian:

```
$ sudo apt install gir1.2-atspi-2.0 python3-gi
```

Puedes consultar la documentación del api de AT-SPI
[aquí](https://lazka.github.io/pgi-docs/Atspi-2.0/index.html).

Si no quieres usar directamente el api "desnudo" de AT-SPI, puedes
usar una librería que proporcione una api de más alto nivel como:

  - [pyatpsi2](https://github.com/GNOME/pyatspi2). 
    Empaquetado en debian como `python3-pyatspi`
	
  - [ldtp](https://ldtp.freedesktop.org/wiki/)

  - [dogtail](https://gitlab.com/dogtail/dogtail). 
    Empaquetado en debian como `python3-dogtail`

  - La librería que usamos en clase: [ipm_e2e](https://github.com/cabrero/ipm_e2e). 
    Disponible en [PyPI](https://pypi.org/project/ipm-e2e/0.0.1/).
	
	> Si vas a instalar librerías desde PyPI, asegúrate primero de
	> concocer el [proceso y las distintas
	> opciones](https://packaging.python.org/tutorials/installing-packages/):
	> global, user, virtual env
  

<a href="{{page.url|baseUrl}}tarea_4" class="button big">Siguiente: Tarea 4</a>
