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
# TEST 7 - Diálogo
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
    print("TEST 7: " + Fore.RED + "FAILED" + Fore.RESET)
    assert False, f"La aplicación no se muestra en el escritorio"

# CASO 1: INTRODUCIMOS "xxxxx" -------------------------------------------------
# Se introduce el nombre
for obj in tree_walk(app):
    if (obj.get_role_name() == 'text' and
        obj.get_name() == 'Buscador_Nombre'):
        break
else:
    process and process.kill()
    print("TEST 7: " + Fore.RED + "FAILED" + Fore.RESET)
    assert False, "No se puede encontrar el Entry nombre de búsqueda de persona"
obj.set_text_contents("xxx")

# Se introduce el apellido
for obj in tree_walk(app):
    if (obj.get_role_name() == 'text' and
        obj.get_name() == 'Buscador_Apellido'):
        break
else:
    process and process.kill()
    print("TEST 7: " + Fore.RED + "FAILED" + Fore.RESET)
    assert False, "No se puede encontrar el Entry nombre de búsqueda de persona"
obj.set_text_contents("xxx")

# Se busca el botón 'Buscar'
for obj in tree_walk(app):
    if (obj.get_role_name() == 'push button' and
        obj.get_name() == 'Buscar'):
        break
else:
    process and process.kill()
    print("TEST 7: " + Fore.RED + "FAILED" + Fore.RESET)
    assert False, "No se pudo encontrar el botón 'Buscar'"

# Accionamos el boton 'Buscar'
for idx in range(obj.get_n_actions()):
    if obj.get_action_name(idx) == 'click':
        break
else:
    process and process.kill()
    print("TEST 7: " + Fore.RED + "FAILED" + Fore.RESET)
    assert False, "No se puede hacer 'click' en el boton 'Buscar'"
obj.do_action(idx)

time.sleep(1.1)

# Se comprueba que se volvio a la ventana desde donde salto el error
# Campo nombre
for obj in tree_walk(app):
    if (obj.get_role_name() == 'text' and
        obj.get_name() == 'Buscador_Nombre' and
        obj.get_text(0, -1) == "xxx"):
        break
else:
    process and process.kill()
    print("TEST 7: " + Fore.RED + "FAILED" + Fore.RESET)
    assert False, "No se puede encontrar el Entry nombre de búsqueda de persona"
obj.set_text_contents("xxx")

# Campo apellido
for obj in tree_walk(app):
    if (obj.get_role_name() == 'text' and
        obj.get_name() == 'Buscador_Apellido' and
        obj.get_text(0, -1) == "xxx"):
        break
else:
    process and process.kill()
    print("TEST 7: " + Fore.RED + "FAILED" + Fore.RESET)
    assert False, "No se puede encontrar el Entry nombre de búsqueda de persona"
obj.set_text_contents("xxx")

# treeView
for obj in tree_walk(app):
    if (obj.get_role_name() == 'table' and obj.get_column_description(0)=="Nombre" and obj.get_column_description(1)=="Id"):
        break
else:
    process and process.kill()
    print("TEST 2: " + Fore.RED + "FAILED" + Fore.RESET)
    assert False, "No se pudo encontrar el treeView"

# Comprobamos la búsqueda
for obj in tree_walk(app):
    #No debería haber ninguna entrada en treeView, así que si existe alguna, el test falla
    if (obj.get_role_name() == 'table cell'):
        process and process.kill()
        print("TEST 2: " + Fore.RED + "FAILED" + Fore.RESET)
        assert False, "El resultado no coincide con la búsqueda"

# CASO 2: INTRODUCIMOS "2021/20/09 00:00:00" -------------------------------------------------
# Se introduce el nombre
for obj in tree_walk(app):
    if (obj.get_role_name() == 'text' and
        obj.get_name() == 'Buscador_Nombre'):
        break
else:
    process and process.kill()
    print("TEST 7: " + Fore.RED + "FAILED" + Fore.RESET)
    assert False, "No se puede encontrar el Entry nombre de búsqueda de persona"
obj.set_text_contents("Pilar")

# Se introduce el apellido
for obj in tree_walk(app):
    if (obj.get_role_name() == 'text' and
        obj.get_name() == 'Buscador_Apellido'):
        break
else:
    process and process.kill()
    print("TEST 7: " + Fore.RED + "FAILED" + Fore.RESET)
    assert False, "No se puede encontrar el Entry nombre de búsqueda de persona"
obj.set_text_contents("Campos")

# Se busca el botón 'Buscar'
for obj in tree_walk(app):
    if (obj.get_role_name() == 'push button' and
        obj.get_name() == 'Buscar'):
        break
else:
    process and process.kill()
    print("TEST 7: " + Fore.RED + "FAILED" + Fore.RESET)
    assert False, "No se pudo encontrar el botón 'Buscar'"

# Accionamos el boton 'Buscar'
for idx in range(obj.get_n_actions()):
    if obj.get_action_name(idx) == 'click':
        break
else:
    process and process.kill()
    print("TEST 7: " + Fore.RED + "FAILED" + Fore.RESET)
    assert False, "No se puede hacer 'click' en el boton 'Buscar'"
obj.do_action(idx)

time.sleep(1.1)

# Seleccionar la fila del usuario
for obj in tree_walk(app):
    if (obj.get_role_name() == 'table'):
        break
else:
    process and process.kill()
    print("TEST 7: " + Fore.RED + "FAILED" + Fore.RESET)
    assert False, "No se puede acceder a la tabla"

if (obj.add_row_selection(0) == False):
	print("TEST 7: " + Fore.RED + "FAILED" + Fore.RESET)
	assert False, "No se puede acceder a la fila de la tabla"

time.sleep(1.1)

# Se busca el Entry para buscar por fecha
for obj in tree_walk(app):
    if (obj.get_role_name() == 'text' and
        obj.get_name() == 'FechaInicio_Entry' and
        obj.get_text(0, -1) == ""):    #Inicialmente vacío
        break
else:
    process and process.kill()
    print("TEST 7: " + Fore.RED + "FAILED" + Fore.RESET)
    assert False, "No se encuentra el Entry para buscar fecha"

obj.set_text_contents("2021/20/09 00:00:00")

# Se busca el botón 'Buscar'
for obj in tree_walk(app):
    if (obj.get_role_name() == 'push button' and
        obj.get_name() == 'button_BuscarRastreador'):
        break
else:
    process and process.kill()
    print("TEST 7: " + Fore.RED + "FAILED" + Fore.RESET)
    assert False, "No se pudo encontrar el botón 'Buscar'"

# Accionamos el boton 'Buscar'
for idx in range(obj.get_n_actions()):
    if obj.get_action_name(idx) == 'click':
        break
else:
    process and process.kill()
    print("TEST 7: " + Fore.RED + "FAILED" + Fore.RESET)
    assert False, "No se puede hacer 'click' en el boton 'Buscar'"
obj.do_action(idx)

time.sleep(2)

# Comprobamos que se queda en la misma página
# Se busca el label de los datos personales

for obj in tree_walk(app):
    if (obj.get_role_name() == 'label'
        and obj.get_text(0, -1) == "Datos personales:"):
        break
else:
    process and process.kill()
    print("Test 7: " + Fore.RED + "FAILED" + Fore.RESET)
    assert False, "No se encuentra el Label 'Datos personales:'"

# Se busca el qr
for obj in tree_walk(app):
    if (obj.get_role_name() == 'icon' and obj.get_name() == "QR"):
        break
else:
    process and process.kill()
    print("Test 7: " + Fore.RED + "FAILED" + Fore.RESET)
    assert False, "No se encuentra el qr"

# Se busca el label de campo nombre
for obj in tree_walk(app):
    if (obj.get_role_name() == 'label' and
        obj.get_text(0, -1) == ("Nombre: Pilar Campos")):
        break
else:
    process and process.kill()
    print("Test 7 : " + Fore.RED + "FAILED" + Fore.RESET)
    assert False, "No se encuentra el Label 'Nombre: Pilar Campos'"

# Se busca el label de campo uuid
for obj in tree_walk(app):
    if (obj.get_role_name() == 'label' and
        obj.get_text(0, -1) == "Uuid: 03438aad-71af-4774-bbca-7ba409bcac20"):
        break
else:
    process and process.kill()
    print("Test 7 : " + Fore.RED + "FAILED" + Fore.RESET)
    assert False, "No se encuentra el Label 'Uuid: 03438aad-71af-4774-bbca-7ba409bcac20'"

# Se busca el label de campo dirección de correo
for obj in tree_walk(app):
    if (obj.get_role_name() == 'label' and
        obj.get_text(0, -1) == "Dirección de Correo: pilar.campos@example.com"):
        break
else:
    process and process.kill()
    print("Test 7 : " + Fore.RED + "FAILED" + Fore.RESET)
    assert False, "No se encuentra el Label 'Dirección de Correo: pilar.campos@example.com'"

# Se busca el label de campo vacunado
for obj in tree_walk(app):
    if (obj.get_role_name() == 'label' and
        obj.get_text(0, -1) == "Vacunado: False"):
        break
else:
    process and process.kill()
    print("Test 7 : " + Fore.RED + "FAILED" + Fore.RESET)
    assert False, "No se encuentra el Label 'Vacunado: False'"

# Se busca el label de campo teléfono
for obj in tree_walk(app):
    if (obj.get_role_name() == 'label' and
        obj.get_text(0, -1) == "Teléfono: 989-550-930"):
        break
else:
    process and process.kill()
    print("Test 7 : " + Fore.RED + "FAILED" + Fore.RESET)
    assert False, "No se encuentra el Label 'Teléfono: 989-550-930'"

# Se busca el label de la actividad reciente

for obj in tree_walk(app):
    if (obj.get_role_name() == 'label'
        and obj.get_text(0, -1) == "Actividad Reciente:"):
        break
else:
    process and process.kill()
    print("Test 7: " + Fore.RED + "FAILED" + Fore.RESET)
    assert False, "No se encuentra el Label 'Actividad Reciente:'"

# Se busca el treeView actividad reciente
for obj in tree_walk(app):
    if (obj.get_role_name() == 'table' and obj.get_column_description(0)=="Nombre del Centro" and obj.get_column_description(1)=="Temperatura"
        and obj.get_column_description(2)=="Fecha y Hora" and obj.get_column_description(3)=="Tipo"):
        break
else:
    process and process.kill()
    print("Test 7: " + Fore.RED + "FAILED" + Fore.RESET)
    assert False, "No se pudo encontrar el treeView de Actividad Reciente"

# Comprobamos las filas de la tabla de Actividad Reciente
mycell = obj.get_accessible_at(0,0)
list = [["Polideportivo Milagros Crespo","35.0","2021/08/18 05:30:20", "IN"],
        ["Polideportivo Milagros Crespo","35.0","2021/08/18 06:42:41", "OUT"],
        ["Centro Comercial Blanca Carmona", "35.2", "2021/09/06 16:25:53", "IN"],
        ["Centro Comercial Blanca Carmona", "35.2", "2021/09/06 20:47:13", "OUT"],
        ["Polideportivo Andres Ibañez","35.3","2021/09/01 04:33:25", "IN"]]

for i in range (2):
    for j in range (4):
        if (obj.get_accessible_at(i, j).get_text(0,-1) != list[i][j]):
            print(list[i][j])
            print(obj.get_accessible_at(i, j).get_text(0,-1))
            process and process.kill()
            print("Test 7: " + Fore.RED + "FAILED" + Fore.RESET)
            assert False, "No se pudo encontrar el treeView de Actividad Reciente"

# Se busca el botón mostrar todo de la actividad reciente

for obj in tree_walk(app):
    if (obj.get_role_name() == 'push button'
        and obj.get_name() == "button_MostrarTodoActividad"):
        break
else:
    process and process.kill()
    print("Test 7: " + Fore.RED + "FAILED" + Fore.RESET)
    assert False, "No se encuentra el botón 'Mostrar Todo'"

# Se busca el label del rastreador

for obj in tree_walk(app):
    if (obj.get_role_name() == 'label'
        and obj.get_text(0, -1) == "Rastreador:"):
        break
else:
    process and process.kill()
    print("Test 7: " + Fore.RED + "FAILED" + Fore.RESET)
    assert False, "No se encuentra el Label 'Rastreador:'"

# Se busca el label de la fecha inicial del rastreador

for obj in tree_walk(app):
    if (obj.get_role_name() == 'label'
        and obj.get_text(0, -1) == "Introduzca la fecha y hora desde la que desea rastrear:"):
        break
else:
    process and process.kill()
    print("Test 7: " + Fore.RED + "FAILED" + Fore.RESET)
    assert False, "No se encuentra el Label 'Introduzca la fecha y hora desde la que desea rastrear:'"

# Se busca el Entry para la fecha inicial del rastreador
for obj in tree_walk(app):
    if (obj.get_role_name() == 'text' and
        obj.get_name() == 'FechaInicio_Entry'):    #Inicialmente vacío
        break
else:
    process and process.kill()
    print("Test 7: " + Fore.RED + "FAILED" + Fore.RESET)
    assert False, "No se encuentra el Entry para la fecha inicial"

# Se busca el label de la fecha final del rastreador

for obj in tree_walk(app):
    if (obj.get_role_name() == 'label'
        and obj.get_text(0, -1) == "Introduzca la fecha y hora hasta la que desea rastrear:"):
        break
else:
    process and process.kill()
    print("Test 7: " + Fore.RED + "FAILED" + Fore.RESET)
    assert False, "No se encuentra el Label 'Introduzca la fecha y hora desde la que desea rastrear:'"

# Se busca el Entry para la fecha final del rastreador
for obj in tree_walk(app):
    if (obj.get_role_name() == 'text' and
        obj.get_name() == 'FechaFinal_Entry' and
        obj.get_text(0, -1) == "") :    #Inicialmente vacío
        break
else:
    process and process.kill()
    print("Test 7: " + Fore.RED + "FAILED" + Fore.RESET)
    assert False, "No se encuentra el Entry para la fecha inicial"

# Se busca el botón buscar del rastreador
for obj in tree_walk(app):
    if (obj.get_role_name() == 'push button'
        and obj.get_name() == "button_BuscarRastreador"):
        break
else:
    process and process.kill()
    print("Test 7: " + Fore.RED + "FAILED" + Fore.RESET)
    assert False, "No se encuentra el botón 'Buscar'"


# EL TEST 7 TERMINA
# Cerramos todo
print("   TEST 7: OK")
f = open("test_regist.txt", "w")
f.write("7 OK")
f.close()
process and process.kill()
