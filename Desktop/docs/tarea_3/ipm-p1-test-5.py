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
# TEST 5 - Rastreo Contactos Persona
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
    print("TEST 5: " + Fore.RED + "FAILED" + Fore.RESET)
    assert False, f"La aplicación no se muestra en el escritorio"

# Se introduce el nombre
for obj in tree_walk(app):
    if (obj.get_role_name() == 'text' and
        obj.get_name() == 'Buscador_Nombre'):
        break
else:
    process and process.kill()
    print("TEST 5: " + Fore.RED + "FAILED" + Fore.RESET)
    assert False, "No se puede encontrar el Entry nombre de búsqueda de persona"
obj.set_text_contents("Pilar")

# Se introduce el apellido
for obj in tree_walk(app):
    if (obj.get_role_name() == 'text' and
        obj.get_name() == 'Buscador_Apellido'):
        break
else:
    process and process.kill()
    print("TEST 5: " + Fore.RED + "FAILED" + Fore.RESET)
    assert False, "No se puede encontrar el Entry nombre de búsqueda de persona"
obj.set_text_contents("Campos")

# Se busca el botón 'Buscar'
for obj in tree_walk(app):
    if (obj.get_role_name() == 'push button' and
        obj.get_name() == 'Buscar'):
        break
else:
    process and process.kill()
    print("TEST 5: " + Fore.RED + "FAILED" + Fore.RESET)
    assert False, "No se pudo encontrar el botón 'Buscar'"

# Accionamos el boton 'Buscar'
for idx in range(obj.get_n_actions()):
    if obj.get_action_name(idx) == 'click':
        break
else:
    process and process.kill()
    print("TEST 5: " + Fore.RED + "FAILED" + Fore.RESET)
    assert False, "No se puede hacer 'click' en el boton 'Buscar'"
obj.do_action(idx)

time.sleep(1.1)

# Seleccionar la fila del usuario
for obj in tree_walk(app):
    if (obj.get_role_name() == 'table'):
        break
else:
    process and process.kill()
    print("TEST 5: " + Fore.RED + "FAILED" + Fore.RESET)
    assert False, "No se puede acceder a la tabla"

if (obj.add_row_selection(0) == False):
	print("TEST 5: " + Fore.RED + "FAILED" + Fore.RESET)
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
    print("TEST 5: " + Fore.RED + "FAILED" + Fore.RESET)
    assert False, "No se encuentra el Entry para buscar fecha"

obj.set_text_contents("2020/09/09 00:00:00")

# Se busca el botón 'Buscar'
for obj in tree_walk(app):
    if (obj.get_role_name() == 'push button' and
        obj.get_name() == 'button_BuscarRastreador'):
        break
else:
    process and process.kill()
    print("TEST 5: " + Fore.RED + "FAILED" + Fore.RESET)
    assert False, "No se pudo encontrar el botón 'Buscar'"

# Accionamos el boton 'Buscar'
for idx in range(obj.get_n_actions()):
    if obj.get_action_name(idx) == 'click':
        break
else:
    process and process.kill()
    print("TEST 5: " + Fore.RED + "FAILED" + Fore.RESET)
    assert False, "No se puede hacer 'click' en el boton 'Buscar'"
obj.do_action(idx)

time.sleep(2)

# Se busca el label de contactos
for obj in tree_walk(app):
    if (obj.get_role_name() == 'label' and
        obj.get_text(0, -1).startswith("Contactos de")):
        break
else:
    #process and process.kill()
    print("TEST 5: " + Fore.RED + "FAILED" + Fore.RESET)
    assert False, "No se encuentra el Label 'Contactos de Pilar Campos:'"

# Se busca el treeView
for obj in tree_walk(app):
    if (obj.get_role_name() == 'table' and obj.get_column_description(0)=="Nombre Ap1 Ap2" and obj.get_column_description(1)=="Uuid" and obj.get_column_description(2)=="Contacto"):
        break
else:
    process and process.kill()
    print("TEST 5: " + Fore.RED + "FAILED" + Fore.RESET)
    assert False, "No se pudo encontrar el treeView"

# Comprobamos las filas de la tabla de Contactos de la página 1
list = [['Angela Soler', '6e2d45ec-7efe-4000-b6cf-9d717ca18519', '916-741-412'],
        ['Valentin Montero', '66ad5cd5-6876-4036-bde5-d71ffd85a317', '976-613-662'],
        ['Juana Gutierrez', '60ddc0c0-b27d-4ba4-9633-422471b2d26e', '966-533-367'],
        ['Domingo Ferrer', '411dbf55-74c7-4f9b-b6cb-a16d094f9fa1', '990-145-414'],
        ['Concepcion Leon', '6db30ef9-008b-4464-9726-6e223fe44dab', '962-618-846'],
        ['Jorge Jimenez', '7c851991-3615-414c-80fd-0709a877f5f8', '984-126-887'],
        ['Nieves Vargas', '5faf6c72-da4b-45a5-a17d-659121c4e4bf', '990-350-465'],
        ['Emilio Rodriguez', '7ef662ea-eff7-41a8-af0b-684dd67883de', '966-034-268'],
        ['Gema Vidal', '7248b52d-e49b-4c05-a75e-278a821b69f6', '996-867-896'],
        ['Jose Ruiz', '36ee964a-fff7-49aa-927f-d9881ad0f68c', '912-649-849']]

for i in range (10):
    for j in range (3):
        if (obj.get_accessible_at(i, j).get_text(0,-1) != list[i][j]):
            process and process.kill()
            print("TEST 5: " + Fore.RED + "FAILED" + Fore.RESET)
            assert False, "No se pudo cargar los datos del treeView de Contactos"

# Se busca el Entry de número de página
for obj in tree_walk(app):
    if (obj.get_role_name() == 'text' and
        obj.get_text(0, -1) == "1/7"):
        break
else:
    process and process.kill()
    print("TEST 5: " + Fore.RED + "FAILED" + Fore.RESET)
    assert False, "No se encuentra el Entry de número de página"

# Se busca el botón 'Siguiente'
for obj in tree_walk(app):
    if (obj.get_role_name() == 'push button' and
        obj.get_name() == 'Next_Button_Paginacion'):
        break
else:
    process and process.kill()
    print("TEST 5: " + Fore.RED + "FAILED" + Fore.RESET)
    assert False, "No se pudo encontrar el botón 'Siguiente'"

# Accionamos el boton 'Siguiente'
for idx in range(obj.get_n_actions()):
    if obj.get_action_name(idx) == 'click':
        break
else:
    process and process.kill()
    print("TEST 5: " + Fore.RED + "FAILED" + Fore.RESET)
    assert False, "No se puedo hacer 'click' en el boton 'Siguiente'"
obj.do_action(idx)

# Se busca el Entry de número de página
for obj in tree_walk(app):
    if (obj.get_role_name() == 'text' and
        obj.get_text(0, -1) == "2/7"):
        break
else:
    process and process.kill()
    print("TEST 5: " + Fore.RED + "FAILED" + Fore.RESET)
    assert False, "No se encuentra el Entry de número de página"

# Se busca el treeView
for obj in tree_walk(app):
    if (obj.get_role_name() == 'table' and obj.get_column_description(0)=="Nombre Ap1 Ap2" and obj.get_column_description(1)=="Uuid" and obj.get_column_description(2)=="Contacto"):
        break
else:
    process and process.kill()
    print("TEST 5: " + Fore.RED + "FAILED" + Fore.RESET)
    assert False, "No se pudo encontrar el treeView de la página 2"

# Comprobamos las filas de la tabla de Contactos de la página 1
list2 = [['Aitor Calvo', '210fa7fc-f3d9-42db-a717-edb793d4b9f0', '981-714-646'],
         ['Vanesa Vicente', '0e7b45d7-4e21-4243-a3f2-5b78c7cd8682', '994-554-298'],
         ['Marco Vazquez', 'c9852e70-46af-41d0-bbff-ce72643fbc53', '984-837-876'],
         ['Miguel Ferrer', '90cc9686-714b-4b80-b0a7-0b6f2b618242', '971-822-978'],
         ['Mario Montero', 'b09de819-4c9e-4b89-b131-03136e0bba7c', '924-918-261'],
         ['Lidia Esteban', '788834e3-fbc5-44af-94f7-790c2a9e0b28', '936-224-312'],
         ['Eugenio Guerrero', '726b0c5a-12e8-42c0-98bf-11ed980f830b', '920-125-419'],
         ['Carmelo Alvarez', '9ba2d2f0-a7b6-42cb-80d0-ac0e398db4a7', '965-234-531'],
         ['Diego Marquez', 'e10120d7-06b7-48c3-bbbf-44f71fd77235', '962-580-604'],
         ['Angeles Molina', 'b1b606fb-1124-40f4-9c32-44e2c42216a8', '938-338-022']]

for i in range (10):
    for j in range (3):
        if (obj.get_accessible_at(i, j).get_text(0,-1) != list2[i][j]):
            process and process.kill()
            print("TEST 5: " + Fore.RED + "FAILED" + Fore.RESET)
            assert False, "No se pudo recargar los datos del treeView de Contactos, es decir no se actualiza de manera de correcta"


# Se busca el botón 'Anterior'
for obj in tree_walk(app):
    if (obj.get_role_name() == 'push button' and
        obj.get_name() == 'Previous_Button_Paginacion'):
        break
else:
    process and process.kill()
    print("TEST 5: " + Fore.RED + "FAILED" + Fore.RESET)
    assert False, "No se pudo encontrar el botón 'Anterior'"

# Accionamos el boton 'Anterior'
for idx in range(obj.get_n_actions()):
    if obj.get_action_name(idx) == 'click':
        break
else:
    process and process.kill()
    print("TEST 5: " + Fore.RED + "FAILED" + Fore.RESET)
    assert False, "No se puedo hacer 'click' en el boton 'Anterior'"
obj.do_action(idx)

# Se busca el Entry de número de página
for obj in tree_walk(app):
    if (obj.get_role_name() == 'text' and
        obj.get_text(0, -1) == "1/7"):
        break
else:
    process and process.kill()
    print("TEST 5: " + Fore.RED + "FAILED" + Fore.RESET)
    assert False, "No se encuentra el Entry de número de página"

# Se busca el treeView
for obj in tree_walk(app):
    if (obj.get_role_name() == 'table' and obj.get_column_description(0)=="Nombre Ap1 Ap2" and obj.get_column_description(1)=="Uuid" and obj.get_column_description(2)=="Contacto"):
        break
else:
    process and process.kill()
    print("TEST 5: " + Fore.RED + "FAILED" + Fore.RESET)
    assert False, "No se pudo encontrar el treeView de la página 1"

for i in range (10):
    for j in range (3):
        if (obj.get_accessible_at(i, j).get_text(0,-1) != list[i][j]):
            process and process.kill()
            print("TEST 5: " + Fore.RED + "FAILED" + Fore.RESET)
            assert False, "No se pudo recargar los datos del treeView de Contactos, es decir no se actualiza de manera de correcta"


# EL TEST 5 TERMINA
# Cerramos todo
print("   TEST 5: OK")
f = open("test_regist.txt", "w")
f.write("5 OK")
f.close()
process and process.kill()
