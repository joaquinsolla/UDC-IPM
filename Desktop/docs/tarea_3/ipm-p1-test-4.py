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
# TEST 4 - Historial de Actividad de una persona
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
    print("TEST 4: " + Fore.RED + "FAILED" + Fore.RESET)
    assert False, f"La aplicación no se muestra en el escritorio"

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

# Se busca el botón mostrar todo de la actividad reciente
for obj in tree_walk(app):
    if (obj.get_role_name() == 'push button'
        and obj.get_name() == "button_MostrarTodoActividad"):
        break
else:
    process and process.kill()
    print("TEST 4: " + Fore.RED + "FAILED" + Fore.RESET)
    assert False, "No se encuentra el botón 'Mostrar Todo'"

# Accionamos el boton 'Mostrar Todo'
for idx in range(obj.get_n_actions()):
    if obj.get_action_name(idx) == 'click':
        break
else:
    process and process.kill()
    print("TEST 4: " + Fore.RED + "FAILED" + Fore.RESET)
    assert False, "No se puedo hacer 'click' en el boton 'Mostrar Todo'"
obj.do_action(idx)

time.sleep(1.1)

# Se busca el label de "Historial Actividad:"
for obj in tree_walk(app):
    if (obj.get_role_name() == 'label' and
        obj.get_text(0, -1) == "Historial Actividad:"):
        break
else:
    process and process.kill()
    print("TEST 4: " + Fore.RED + "FAILED" + Fore.RESET)
    assert False, "No se encuentra el Label 'Historial Actividad:'"

# Se busca el treeView
for obj in tree_walk(app):
    if (obj.get_role_name() == 'table' and obj.get_column_description(0)=="Id_Centro" and obj.get_column_description(1)=="Nombre de centro" and obj.get_column_description(2)=="Temperatura" and obj.get_column_description(3)=="Fecha y hora" and obj.get_column_description(4)=="Tipo"):
        break
else:
    process and process.kill()
    print("TEST 4: " + Fore.RED + "FAILED" + Fore.RESET)
    assert False, "No se pudo encontrar el treeView"

# Comprobamos las filas de la tabla de Historial actividad
list = [['120', 'Polideportivo Milagros Crespo', '35.0', '2021/08/18 05:30:20', 'IN'],
        ['120', 'Polideportivo Milagros Crespo', '35.0', '2021/08/18 06:42:41', 'OUT'],
        ['119', 'Centro comercial Blanca Carmona', '35.2', '2021/09/06 16:25:53', 'IN'],
        ['119', 'Centro comercial Blanca Carmona', '35.2', '2021/09/06 20:47:13', 'OUT'],
        ['118', 'Polideportivo Andres Ibañez', '35.3', '2021/09/01 04:33:25', 'IN'],
        ['118', 'Polideportivo Andres Ibañez', '35.3', '2021/09/01 12:13:28', 'OUT'],
        ['111', 'Biblioteca Lorenzo Guerrero', '37.0', '2021/09/08 20:15:13', 'IN'],
        ['111', 'Biblioteca Lorenzo Guerrero', '37.0', '2021/09/09 01:40:52', 'OUT'],
        ['122', 'Centro comercial Esther Marquez', '37.4', '2021/08/30 00:39:39', 'IN'],
        ['122', 'Centro comercial Esther Marquez', '37.4', '2021/08/30 06:49:12', 'OUT']]


for i in range (10):
    for j in range (5):
        if (obj.get_accessible_at(i, j).get_text(0,-1) != list[i][j]):
            process and process.kill()
            print("TEST 4: " + Fore.RED + "FAILED" + Fore.RESET)
            assert False, "No se pudo cargar los datos del treeView de Historial Reciente de manera correcta"

# Se busca el Entry de número de página
for obj in tree_walk(app):
    if (obj.get_role_name() == 'text' and
        obj.get_text(0, -1) == "1/3"):
        break
else:
    process and process.kill()
    print("TEST 4: " + Fore.RED + "FAILED" + Fore.RESET)
    assert False, "No se encuentra el Entry de número de página"

# Se busca el botón 'Siguiente'
for obj in tree_walk(app):
    if (obj.get_role_name() == 'push button' and
        obj.get_name() == 'Next_Button_Paginacion'):
        break
else:
    process and process.kill()
    print("TEST 4: " + Fore.RED + "FAILED" + Fore.RESET)
    assert False, "No se pudo encontrar el botón 'Siguiente'"

# Accionamos el boton 'Siguiente', pasando a la página 2
for idx in range(obj.get_n_actions()):
    if obj.get_action_name(idx) == 'click':
        break
else:
    process and process.kill()
    print("TEST 4: " + Fore.RED + "FAILED" + Fore.RESET)
    assert False, "No se puedo hacer 'click' en el boton 'Siguiente'"
obj.do_action(idx)

# Se busca el treeView actualizado
for obj in tree_walk(app):
    if (obj.get_role_name() == 'table' and obj.get_column_description(0)=="Id_Centro" and obj.get_column_description(1)=="Nombre de centro" and obj.get_column_description(2)=="Temperatura" and obj.get_column_description(3)=="Fecha y hora" and obj.get_column_description(4)=="Tipo"):
        break
else:
    process and process.kill()
    print("TEST 4: " + Fore.RED + "FAILED" + Fore.RESET)
    assert False, "No se pudo encontrar el treeView"

# Comprobamos las filas de la tabla de Historial actividad de la página 2, es decir vemos que se actualice y que lo haga con los datos correctos
list2 = [['123', 'Centro cultural Claudia Marquez', '36.9', '2021/09/08 07:56:35', 'IN'],
         ['123', 'Centro cultural Claudia Marquez', '36.9', '2021/09/08 13:42:07', 'OUT'],
         ['112', 'Centro cultural Hector Martin', '36.4', '2021/08/12 17:50:36', 'IN'],
         ['112', 'Centro cultural Hector Martin', '36.4', '2021/08/13 01:26:42', 'OUT'],
         ['113', 'Centro cultural Valentin Vega', '36.5', '2021/09/09 11:15:19', 'IN'],
         ['113', 'Centro cultural Valentin Vega', '36.5', '2021/09/09 18:35:41', 'OUT'],
         ['127', 'Polideportivo Ana Hernandez', '35.3', '2021/09/07 09:45:39', 'IN'],
         ['127', 'Polideportivo Ana Hernandez', '35.3', '2021/09/07 16:33:10', 'OUT'],
         ['115', 'Biblioteca Claudia Alonso', '37.3', '2021/08/17 09:40:08', 'IN'],
         ['115', 'Biblioteca Claudia Alonso', '37.3', '2021/08/17 15:48:58', 'OUT']]


for i in range (10):
    for j in range (5):
        if (obj.get_accessible_at(i, j).get_text(0,-1) != list2[i][j]):
            process and process.kill()
            print("TEST 4: " + Fore.RED + "FAILED" + Fore.RESET)
            assert False, "No se pudo recargar los datos del treeView de Historial Actividad, es decir no se ha actualizado la página"

# Se busca el Entry de número de página
for obj in tree_walk(app):
    if (obj.get_role_name() == 'text' and
        obj.get_text(0, -1) == "2/3"):
        break
else:
    process and process.kill()
    print("TEST 4: " + Fore.RED + "FAILED" + Fore.RESET)
    assert False, "No se encuentra el Entry de número de página"

# Se busca el botón 'Anterior'
for obj in tree_walk(app):
    if (obj.get_role_name() == 'push button' and
        obj.get_name() == 'Previous_Button_Paginacion'):
        break
else:
    process and process.kill()
    print("TEST 4: " + Fore.RED + "FAILED" + Fore.RESET)
    assert False, "No se pudo encontrar el botón 'Anterior'"

# Accionamos el boton 'Anterior'
for idx in range(obj.get_n_actions()):
    if obj.get_action_name(idx) == 'click':
        break
else:
    process and process.kill()
    print("TEST 4: " + Fore.RED + "FAILED" + Fore.RESET)
    assert False, "No se puedo hacer 'click' en el boton 'Anterior'"
obj.do_action(idx)

# Se busca el treeView actualizado
for obj in tree_walk(app):
    if (obj.get_role_name() == 'table' and obj.get_column_description(0)=="Id_Centro" and obj.get_column_description(1)=="Nombre de centro" and obj.get_column_description(2)=="Temperatura" and obj.get_column_description(3)=="Fecha y hora" and obj.get_column_description(4)=="Tipo"):
        break
else:
    process and process.kill()
    print("TEST 4: " + Fore.RED + "FAILED" + Fore.RESET)
    assert False, "No se pudo encontrar el treeView"

# Comprobamos las filas de la tabla de Historial actividad de la página 1, es decir vemos que se actualice y que lo haga con los datos correctos

for i in range (10):
    for j in range (5):
        if (obj.get_accessible_at(i, j).get_text(0,-1) != list[i][j]):
            process and process.kill()
            print("TEST 4: " + Fore.RED + "FAILED" + Fore.RESET)
            assert False, "No se pudo recargar los datos del treeView de Historial Actividad, es decir no se ha actualizado la página"


# Se busca el Entry de número de página
for obj in tree_walk(app):
    if (obj.get_role_name() == 'text' and
        obj.get_text(0, -1) == "1/3"):
        break
else:
    process and process.kill()
    print("TEST 4: " + Fore.RED + "FAILED" + Fore.RESET)
    assert False, "No se encuentra el Entry de número de página"


# EL TEST 4 TERMINA
# Cerramos todo
print("   TEST 4: OK")
f = open("test_regist.txt", "w")
f.write("4 OK")
f.close()
process and process.kill()
