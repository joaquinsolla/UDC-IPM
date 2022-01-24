import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

import random
import subprocess
import time
from typing import Any, Iterator, NamedTuple, Optional, Union
from colorama import Fore

import gi
gi.require_version('Atspi', '2.0')
from gi.repository import Atspi

def tree_walk(obj: Atspi.Object) -> Iterator[Atspi.Object]:
    yield obj
    for i in range(obj.get_child_count()):
        yield from tree_walk(obj.get_child_at_index(i))

#-------------------------------------------------------------------------------
# TEST 6 - Navegación de ventana
#-------------------------------------------------------------------------------

# Ejecutar la aplicación en un proceso del S.O.
appPath = "./ipm-p1.py"
appName = f"{appPath}-test-{str(random.randint(0, 100000000))}"
process = subprocess.Popen([appPath, '--name', appName])
assert process is not None, f"No se puede ejecuar la aplicación"

# Se espera hasta que la aplicación aparezca en el escritorio
# Pasado un timeout se abandona la espera
desktop = Atspi.get_desktop(0)
start = time.time()
timeout = 5
app = None
while app is None and (time.time() - start) < timeout:
    gen = filter(lambda child: child and child.get_name() == appName,
                 (desktop.get_child_at_index(i) for i in range(desktop.get_child_count())))
    app = next(gen, None)
    if app is None:
        time.sleep(0.5)

# Se comprueba que el arranque de la app fue exitoso
if app is None:
    process and process.kill()
    print("TEST 6: " + Fore.RED + "FAILED" + Fore.RESET)
    assert False, f"La aplicación no se muestra en el escritorio"

# VISTA-1-----------------------------------------------------------------------

# PREVIOUS
# Se busca el botón 'Previous' (flecha para ir a página anterior)
for obj in tree_walk(app):
    if (obj.get_role_name() == 'push button' and
        obj.get_name() == 'Previous_Page'):
        break
else:
    process and process.kill()
    print("TEST 6: " + Fore.RED + "FAILED" + Fore.RESET)
    assert False, "No se pudo encontrar el botón 'Previous_Page'"

# Accionamos el boton 'Previous'
for idx in range(obj.get_n_actions()):
    if obj.get_action_name(idx) == 'click':
        break
else:
    process and process.kill()
    print("TEST 6: " + Fore.RED + "FAILED" + Fore.RESET)
    assert False, "No se puedo hacer 'click' en el boton 'Previous'"
obj.do_action(idx)

# Comprobamos que estamos en la Vista 1 leyendo el label de inicio
for obj in tree_walk(app):
    if (obj.get_role_name() == 'label' and
        obj.get_text(0, -1) == "Introduzca el nombre de la persona:"):
        break
else:
    process and process.kill()
    print("TEST 6: " + Fore.RED + "FAILED" + Fore.RESET)
    assert False, "No se encuentra el Label 'Introduzca el nombre de la persona:'"

# HOME
# Se busca el botón 'Home' (botón nos lleva a la página de inicio)
for obj in tree_walk(app):
    if (obj.get_role_name() == 'push button' and
        obj.get_name() == 'Home_Button'):
        break
else:
    process and process.kill()
    print("TEST 6: " + Fore.RED + "FAILED" + Fore.RESET)
    assert False, "No se pudo encontrar el botón 'Home_Button'"

# Accionamos el boton 'Home'
for idx in range(obj.get_n_actions()):
    if obj.get_action_name(idx) == 'click':
        break
else:
    process and process.kill()
    print("TEST 6: " + Fore.RED + "FAILED" + Fore.RESET)
    assert False, "No se puedo hacer 'click' en el boton 'Home'"
obj.do_action(idx)

# Comprobamos que estamos en la Vista 1 leyendo el label de inicio
for obj in tree_walk(app):
    if (obj.get_role_name() == 'label' and
        obj.get_text(0, -1) == "Introduzca el nombre de la persona:"):
        break
else:
    process and process.kill()
    print("TEST 6: " + Fore.RED + "FAILED" + Fore.RESET)
    assert False, "No se encuentra el Label 'Introduzca el nombre de la persona:'"

# VISTA-2-----------------------------------------------------------------------

# Accedemos a la vista 2
# Se introduce el nombre
for obj in tree_walk(app):
    if (obj.get_role_name() == 'text' and
        obj.get_name() == 'Buscador_Nombre'):
        break
else:
    process and process.kill()
    print("TEST 6: " + Fore.RED + "FAILED" + Fore.RESET)
    assert False, "No se puede encontrar el Entry nombre de búsqueda de persona"
obj.set_text_contents("Pilar")

# Se introduce el apellido
for obj in tree_walk(app):
    if (obj.get_role_name() == 'text' and
        obj.get_name() == 'Buscador_Apellido'):
        break
else:
    process and process.kill()
    print("TEST 6: " + Fore.RED + "FAILED" + Fore.RESET)
    assert False, "No se puede encontrar el Entry nombre de búsqueda de persona"
obj.set_text_contents("Campos")

# Se busca el botón 'Buscar'
for obj in tree_walk(app):
    if (obj.get_role_name() == 'push button' and
        obj.get_name() == 'Buscar'):
        break
else:
    process and process.kill()
    print("TEST 6: " + Fore.RED + "FAILED" + Fore.RESET)
    assert False, "No se pudo encontrar el botón 'Buscar'"

# Accionamos el boton 'Buscar'
for idx in range(obj.get_n_actions()):
    if obj.get_action_name(idx) == 'click':
        break
else:
    process and process.kill()
    print("TEST 6: " + Fore.RED + "FAILED" + Fore.RESET)
    assert False, "No se puede hacer 'click' en el boton 'Buscar'"
obj.do_action(idx)

time.sleep(1.1)

# Seleccionar la fila del usuario
for obj in tree_walk(app):
    if (obj.get_role_name() == 'table'):
        break
else:
    process and process.kill()
    print("TEST 6: " + Fore.RED + "FAILED" + Fore.RESET)
    assert False, "No se puede acceder a la tabla"

if (obj.add_row_selection(0) == False):
	print("TEST 6: " + Fore.RED + "FAILED" + Fore.RESET)
	assert False, "No se puede acceder a la fila de la tabla"

time.sleep(1.1)

# PREVIOUS
# Se busca el botón 'Previous' (flecha para ir a página anterior)
for obj in tree_walk(app):
    if (obj.get_role_name() == 'push button' and
        obj.get_name() == 'Previous_Page'):
        break
else:
    process and process.kill()
    print("TEST 6: " + Fore.RED + "FAILED" + Fore.RESET)
    assert False, "No se pudo encontrar el botón 'Previous_Page'"

# Accionamos el boton 'Previous'
for idx in range(obj.get_n_actions()):
    if obj.get_action_name(idx) == 'click':
        break
else:
    process and process.kill()
    print("TEST 6: " + Fore.RED + "FAILED" + Fore.RESET)
    assert False, "No se puedo hacer 'click' en el boton 'Previous'"
obj.do_action(idx)

# Comprobamos que estamos en la Vista 1 leyendo el label de inicio
for obj in tree_walk(app):
    if (obj.get_role_name() == 'label' and
        obj.get_text(0, -1) == "Introduzca el nombre de la persona:"):
        break
else:
    process and process.kill()
    print("TEST 6: " + Fore.RED + "FAILED" + Fore.RESET)
    assert False, "No se encuentra el Label 'Introduzca el nombre de la persona:'"

# Accedemos a la vista 2
# Se introduce el nombre
for obj in tree_walk(app):
    if (obj.get_role_name() == 'text' and
        obj.get_name() == 'Buscador_Nombre'):
        break
else:
    process and process.kill()
    print("TEST 4: " + Fore.RED + "FAILED" + Fore.RESET)
    assert False, "No se puede encontrar el Entry nombre de búsqueda de persona"
obj.set_text_contents("Pilar")

# Se introduce el apellido
for obj in tree_walk(app):
    if (obj.get_role_name() == 'text' and
        obj.get_name() == 'Buscador_Apellido'):
        break
else:
    process and process.kill()
    print("TEST 4: " + Fore.RED + "FAILED" + Fore.RESET)
    assert False, "No se puede encontrar el Entry nombre de búsqueda de persona"
obj.set_text_contents("Campos")

# Se busca el botón 'Buscar'
for obj in tree_walk(app):
    if (obj.get_role_name() == 'push button' and
        obj.get_name() == 'Buscar'):
        break
else:
    process and process.kill()
    print("TEST 4: " + Fore.RED + "FAILED" + Fore.RESET)
    assert False, "No se pudo encontrar el botón 'Buscar'"

# Accionamos el boton 'Buscar'
for idx in range(obj.get_n_actions()):
    if obj.get_action_name(idx) == 'click':
        break
else:
    process and process.kill()
    print("TEST 4: " + Fore.RED + "FAILED" + Fore.RESET)
    assert False, "No se puede hacer 'click' en el boton 'Buscar'"
obj.do_action(idx)

time.sleep(1.1)

# Seleccionar la fila del usuario
for obj in tree_walk(app):
    if (obj.get_role_name() == 'table'):
        break
else:
    process and process.kill()
    print("TEST 4: " + Fore.RED + "FAILED" + Fore.RESET)
    assert False, "No se puede acceder a la tabla"

if (obj.add_row_selection(0) == False):
	print("TEST 4: " + Fore.RED + "FAILED" + Fore.RESET)
	assert False, "No se puede acceder a la fila de la tabla"

time.sleep(1.1)

# HOME
# Se busca el botón 'Home' (botón nos lleva a la página de inicio)
for obj in tree_walk(app):
    if (obj.get_role_name() == 'push button' and
        obj.get_name() == 'Home_Button'):
        break
else:
    process and process.kill()
    print("TEST 6: " + Fore.RED + "FAILED" + Fore.RESET)
    assert False, "No se pudo encontrar el botón 'Home_Button'"

# Accionamos el boton 'Home'
for idx in range(obj.get_n_actions()):
    if obj.get_action_name(idx) == 'click':
        break
else:
    process and process.kill()
    print("TEST 6: " + Fore.RED + "FAILED" + Fore.RESET)
    assert False, "No se puedo hacer 'click' en el boton 'Home'"
obj.do_action(idx)

# Comprobamos que estamos en la Vista 1 leyendo el label de inicio
for obj in tree_walk(app):
    if (obj.get_role_name() == 'label' and
        obj.get_text(0, -1) == "Introduzca el nombre de la persona:"):
        break
else:
    process and process.kill()
    print("TEST 6: " + Fore.RED + "FAILED" + Fore.RESET)
    assert False, "No se encuentra el Label 'Introduzca el nombre de la persona:'"

# VISTA-3-----------------------------------------------------------------------
# Accedemos a la vista 2
# Se introduce el nombre
for obj in tree_walk(app):
    if (obj.get_role_name() == 'text' and
        obj.get_name() == 'Buscador_Nombre'):
        break
else:
    process and process.kill()
    print("TEST 4: " + Fore.RED + "FAILED" + Fore.RESET)
    assert False, "No se puede encontrar el Entry nombre de búsqueda de persona"
obj.set_text_contents("Pilar")

# Se introduce el apellido
for obj in tree_walk(app):
    if (obj.get_role_name() == 'text' and
        obj.get_name() == 'Buscador_Apellido'):
        break
else:
    process and process.kill()
    print("TEST 4: " + Fore.RED + "FAILED" + Fore.RESET)
    assert False, "No se puede encontrar el Entry nombre de búsqueda de persona"
obj.set_text_contents("Campos")

# Se busca el botón 'Buscar'
for obj in tree_walk(app):
    if (obj.get_role_name() == 'push button' and
        obj.get_name() == 'Buscar'):
        break
else:
    process and process.kill()
    print("TEST 4: " + Fore.RED + "FAILED" + Fore.RESET)
    assert False, "No se pudo encontrar el botón 'Buscar'"

# Accionamos el boton 'Buscar'
for idx in range(obj.get_n_actions()):
    if obj.get_action_name(idx) == 'click':
        break
else:
    process and process.kill()
    print("TEST 4: " + Fore.RED + "FAILED" + Fore.RESET)
    assert False, "No se puede hacer 'click' en el boton 'Buscar'"
obj.do_action(idx)

time.sleep(1.1)

# Seleccionar la fila del usuario
for obj in tree_walk(app):
    if (obj.get_role_name() == 'table'):
        break
else:
    process and process.kill()
    print("TEST 4: " + Fore.RED + "FAILED" + Fore.RESET)
    assert False, "No se puede acceder a la tabla"

if (obj.add_row_selection(0) == False):
	print("TEST 4: " + Fore.RED + "FAILED" + Fore.RESET)
	assert False, "No se puede acceder a la fila de la tabla"

time.sleep(1.1)

# Accedemos a la vista 3
# Buscamos el boton 'Mostrar Todo'
for obj in tree_walk(app):
    if (obj.get_role_name() == 'push button' and
        obj.get_name() == 'button_MostrarTodoActividad'):

        break
else:
    process and process.kill()
    print("TEST 6: " + Fore.RED + "FAILED" + Fore.RESET)
    assert False, "No se pudo encontrar el botón 'Mostrar Todo'"

# Accionamos el boton 'Mostrar Todo'
for idx in range(obj.get_n_actions()):
    if obj.get_action_name(idx) == 'click':
        break
else:
    process and process.kill()
    print("TEST 6: " + Fore.RED + "FAILED" + Fore.RESET)
    assert False, "No se puedo hacer 'click' en el boton 'Mostrar Todo'"
obj.do_action(idx)

time.sleep(1.1)

# PREVIOUS
# Se busca el botón 'Previous' (flecha para ir a página anterior)
for obj in tree_walk(app):
    if (obj.get_role_name() == 'push button' and
        obj.get_name() == 'Previous_Page'):
        break
else:
    process and process.kill()
    print("TEST 6: " + Fore.RED + "FAILED" + Fore.RESET)
    assert False, "No se pudo encontrar el botón 'Previous_Page'"

# Accionamos el boton 'Previous'
for idx in range(obj.get_n_actions()):
    if obj.get_action_name(idx) == 'click':
        break
else:
    process and process.kill()
    print("TEST 6: " + Fore.RED + "FAILED" + Fore.RESET)
    assert False, "No se puedo hacer 'click' en el boton 'Previous'"
obj.do_action(idx)

# Comprobamos que estamos en la Vista 2
# Se busca el label de los datos personales

for obj in tree_walk(app):
    if (obj.get_role_name() == 'label'
        and obj.get_text(0, -1) == "Datos personales:"):
        break
else:
    process and process.kill()
    print("TEST 6: " + Fore.RED + "FAILED" + Fore.RESET)
    assert False, "No se encuentra el Label 'Datos personales:'"

# Accedemos a la vista 3
# Buscamos el boton 'Mostrar Todo'
for obj in tree_walk(app):
    if (obj.get_role_name() == 'push button' and
        obj.get_name() == 'button_MostrarTodoActividad'):

        break
else:
    process and process.kill()
    print("TEST 6: " + Fore.RED + "FAILED" + Fore.RESET)
    assert False, "No se pudo encontrar el botón 'Mostrar Todo'"

# Accionamos el boton 'Mostrar Todo'
for idx in range(obj.get_n_actions()):
    if obj.get_action_name(idx) == 'click':
        break
else:
    process and process.kill()
    print("TEST 6: " + Fore.RED + "FAILED" + Fore.RESET)
    assert False, "No se puedo hacer 'click' en el boton 'Mostrar Todo'"
obj.do_action(idx)

time.sleep(1.1)

# HOME
# Se busca el botón 'Home' (botón nos lleva a la página de inicio)
for obj in tree_walk(app):
    if (obj.get_role_name() == 'push button' and
        obj.get_name() == 'Home_Button'):
        break
else:
    process and process.kill()
    print("TEST 6: " + Fore.RED + "FAILED" + Fore.RESET)
    assert False, "No se pudo encontrar el botón 'Home_Button'"

# Accionamos el boton 'Home'
for idx in range(obj.get_n_actions()):
    if obj.get_action_name(idx) == 'click':
        break
else:
    process and process.kill()
    print("TEST 6: " + Fore.RED + "FAILED" + Fore.RESET)
    assert False, "No se puedo hacer 'click' en el boton 'Home'"
obj.do_action(idx)

# Comprobamos que estamos en la Vista 1 leyendo el label de inicio
for obj in tree_walk(app):
    if (obj.get_role_name() == 'label' and
        obj.get_text(0, -1) == "Introduzca el nombre de la persona:"):
        break
else:
    process and process.kill()
    print("TEST 6: " + Fore.RED + "FAILED" + Fore.RESET)
    assert False, "No se encuentra el Label 'Introduzca el nombre de la persona:'"

# VISTA-4-----------------------------------------------------------------------

# Accedemos a la vista 2
# Se introduce el nombre
for obj in tree_walk(app):
    if (obj.get_role_name() == 'text' and
        obj.get_name() == 'Buscador_Nombre'):
        break
else:
    process and process.kill()
    print("TEST 4: " + Fore.RED + "FAILED" + Fore.RESET)
    assert False, "No se puede encontrar el Entry nombre de búsqueda de persona"
obj.set_text_contents("Pilar")

# Se introduce el apellido
for obj in tree_walk(app):
    if (obj.get_role_name() == 'text' and
        obj.get_name() == 'Buscador_Apellido'):
        break
else:
    process and process.kill()
    print("TEST 4: " + Fore.RED + "FAILED" + Fore.RESET)
    assert False, "No se puede encontrar el Entry nombre de búsqueda de persona"
obj.set_text_contents("Campos")

# Se busca el botón 'Buscar'
for obj in tree_walk(app):
    if (obj.get_role_name() == 'push button' and
        obj.get_name() == 'Buscar'):
        break
else:
    process and process.kill()
    print("TEST 4: " + Fore.RED + "FAILED" + Fore.RESET)
    assert False, "No se pudo encontrar el botón 'Buscar'"

# Accionamos el boton 'Buscar'
for idx in range(obj.get_n_actions()):
    if obj.get_action_name(idx) == 'click':
        break
else:
    process and process.kill()
    print("TEST 4: " + Fore.RED + "FAILED" + Fore.RESET)
    assert False, "No se puede hacer 'click' en el boton 'Buscar'"
obj.do_action(idx)

time.sleep(1.1)

# Seleccionar la fila del usuario
for obj in tree_walk(app):
    if (obj.get_role_name() == 'table'):
        break
else:
    process and process.kill()
    print("TEST 4: " + Fore.RED + "FAILED" + Fore.RESET)
    assert False, "No se puede acceder a la tabla"

if (obj.add_row_selection(0) == False):
	print("TEST 4: " + Fore.RED + "FAILED" + Fore.RESET)
	assert False, "No se puede acceder a la fila de la tabla"

time.sleep(1.1)

# Accedemos a la vista 4
# Se busca el Entry para buscar por fecha
for obj in tree_walk(app):
    if (obj.get_role_name() == 'text' and
        obj.get_name() == 'FechaInicio_Entry' and
        obj.get_text(0, -1) == ""):    #Inicialmente vacío
        break
else:
    process and process.kill()
    print("TEST 6: " + Fore.RED + "FAILED" + Fore.RESET)
    assert False, "No se encuentra el Entry para buscar fecha"

obj.set_text_contents("2020/09/09 00:00:00")

# Se busca el botón 'Buscar'
for obj in tree_walk(app):
    if (obj.get_role_name() == 'push button' and
        obj.get_name() == 'button_BuscarRastreador'):
        break
else:
    process and process.kill()
    print("TEST 6: " + Fore.RED + "FAILED" + Fore.RESET)
    assert False, "No se pudo encontrar el botón 'Buscar'"

# Accionamos el boton 'Buscar'
for idx in range(obj.get_n_actions()):
    if obj.get_action_name(idx) == 'click':
        break
else:
    process and process.kill()
    print("TEST 6: " + Fore.RED + "FAILED" + Fore.RESET)
    assert False, "No se puede hacer 'click' en el boton 'Buscar'"
obj.do_action(idx)

time.sleep(2)

# PREVIOUS
# Se busca el botón 'Previous' (flecha para ir a página anterior)
for obj in tree_walk(app):
    if (obj.get_role_name() == 'push button' and
        obj.get_name() == 'Previous_Page'):
        break
else:
    process and process.kill()
    print("TEST 6: " + Fore.RED + "FAILED" + Fore.RESET)
    assert False, "No se pudo encontrar el botón 'Previous_Page'"

# Accionamos el boton 'Previous'
for idx in range(obj.get_n_actions()):
    if obj.get_action_name(idx) == 'click':
        break
else:
    process and process.kill()
    print("TEST 6: " + Fore.RED + "FAILED" + Fore.RESET)
    assert False, "No se puedo hacer 'click' en el boton 'Previous'"
obj.do_action(idx)

time.sleep(2)

# Comprobamos que estamos en la Vista 2
# Se busca el label de los datos personales

for obj in tree_walk(app):
    if (obj.get_role_name() == 'label'
        and obj.get_text(0, -1) == "Datos personales:"):
        break
else:
    process and process.kill()
    print("TEST 6: " + Fore.RED + "FAILED" + Fore.RESET)
    assert False, "No se encuentra el Label 'Datos personales:'"

# Accedemos a la vista 4
# Se busca el Entry para buscar por fecha
for obj in tree_walk(app):
    if (obj.get_role_name() == 'text' and
        obj.get_name() == 'FechaInicio_Entry' and
        obj.get_text(0, -1) == ""):    #Inicialmente vacío
        break
else:
    process and process.kill()
    print("TEST 6: " + Fore.RED + "FAILED" + Fore.RESET)
    assert False, "No se encuentra el Entry para buscar fecha"

obj.set_text_contents("2020/09/09 00:00:00")

# Se busca el botón 'Buscar'
for obj in tree_walk(app):
    if (obj.get_role_name() == 'push button' and
        obj.get_name() == 'button_BuscarRastreador'):
        break
else:
    process and process.kill()
    print("TEST 6: " + Fore.RED + "FAILED" + Fore.RESET)
    assert False, "No se pudo encontrar el botón 'Buscar'"

# Accionamos el boton 'Buscar'
for idx in range(obj.get_n_actions()):
    if obj.get_action_name(idx) == 'click':
        break
else:
    process and process.kill()
    print("TEST 6: " + Fore.RED + "FAILED" + Fore.RESET)
    assert False, "No se puede hacer 'click' en el boton 'Buscar'"
obj.do_action(idx)

time.sleep(3)

# HOME
# Se busca el botón 'Home' (botón nos lleva a la página de inicio)
for obj in tree_walk(app):
    if (obj.get_role_name() == 'push button' and
        obj.get_name() == 'Home_Button'):
        break
else:
    process and process.kill()
    print("TEST 6: " + Fore.RED + "FAILED" + Fore.RESET)
    assert False, "No se pudo encontrar el botón 'Home_Button'"

# Accionamos el boton 'Home'
for idx in range(obj.get_n_actions()):
    if obj.get_action_name(idx) == 'click':
        break
else:
    process and process.kill()
    print("TEST 6: " + Fore.RED + "FAILED" + Fore.RESET)
    assert False, "No se puedo hacer 'click' en el boton 'Home'"
obj.do_action(idx)

time.sleep(3)

# Comprobamos que estamos en la Vista 1 leyendo el label de inicio
for obj in tree_walk(app):
    if (obj.get_role_name() == 'label' and
        obj.get_text(0, -1) == "Introduzca el nombre de la persona:"):
        break
else:
    process and process.kill()
    print("TEST 6: " + Fore.RED + "FAILED" + Fore.RESET)
    assert False, "No se encuentra el Label 'Introduzca el nombre de la persona:'"

# EL TEST 6 TERMINA
# Cerramos todo
print("   TEST 6: OK")
f = open("test_regist.txt", "w")
f.write("6 OK")
f.close()
process and process.kill()
