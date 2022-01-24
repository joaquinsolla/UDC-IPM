---
layout: generic
title: "Tarea 4: Concurrencia"
banner:
  src: "img/pexels-burak-kebapci-63505.jpg"
  copy_url: "https://www.pexels.com/es-es/foto/autobus-blanco-y-negro-durante-el-dia-63505/"
  copy: "Burak Kebapci"
---

En esta tarea tienes añadir una característica _sine qua non_ para
completar el desarrollo de la aplicación: la interface de usuaria no
se bloquea durante las operaciones de E/S.

> Recuerda: El desarrollo software es un proceso iterativo. Durante la
> realización de esta tendrás que modificar partes del diseño sw y del
> diseño de la interface. No te olvides de actualizar los ficheros
> correspondendientes.

Recuerda que, tal y como explicamos en clase, para que la interface no
se bloquee durante las operaciones de E/S, tienes que adaptar el
código para que realize estas operaciones de forma concurrente.

De la misma forma, tienes que incorporar los mecanismos de feedback,
cancelación de operaciones, ... adecuados para este tipo de
operaciones de E/S.

Finalmente, escribie al menos un test que compruebe que,
efectivamente, la interface no se bloquea durante las operaciones de
E/S. Por ejemplo, puedes considerar los casos en que el servidor tarda
mucho en responder o, simplemente, está caido.


## Requisitos

Los requisitos son los mismos que en las tareas anteriores.
  

## Autoevaluación

Para realizar una autoevaluación de esta tarea, puedes guiarte por las
tablas de las tareas anteriores y la siguiente tabla:


| Criterios | Nivel ||
|-----------| ----- |-|
|           |  Bueno | Inadecuado |
| Cumple los requisitos | Cumple todos los requisitos | No cumple algún requisito |
| La interface no se bloqua durante la E/S | La usuaria puede interactuar con la interface durante una operación de E/S | La interface deja de responder durante la E/S |
| El diseño de la interface está completo | Incluyen los elementos añadidos en esta tarea | No incluye todos los elementos añadidos |
| El diseño sw está completo | Incluyen diagramas para la operación concurrente | No incluye la parte de concurrencia |
| La interface es amigable | Proporciona el feedback adecuado durante las operaciones de E/S | No proporciona feedback |
| Las pruebas son completas | Incluyen pruebas para la operación concurrente | No se prueba el no bloqueo de la interface |


> Recuerda que el profesor sólo evaluará los ficheros que están en tu
> repositorio de _github classroom_. Es más seguro que tú también
> autoevalues tu trabajo sobre un _clone_ de ese repositorio.


## Recursos

- ¿ Cómo comprobar si la interface sigue respondiendo ?

  Es sencillo, cuando no responde a los eventos de la usuaria tampoco
  responde a las peticiones por `at-spi`.  Así, por ejemplo, podemos
  escribir:
  
  ```python
  def step_la_interface_sigue_respondiendo(app: Atspi.Object) -> None:
      # ELiminamos el timeout de arrancar la app
      atspi.Atspi.set_timeout(800, -1)
      assert app.get_name() != "", "La interface no responde"
  ```
  
