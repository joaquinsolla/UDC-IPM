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
# TEST 2 - Búsqueda de persona
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
    print("TEST 2: " + Fore.RED + "FAILED" + Fore.RESET)
    assert False, f"La aplicación no se muestra en el escritorio"

# CASO 1: INTRODUCIMOS "Pilar" -------------------------------------------------
# Se introduce el nombre
for obj in tree_walk(app):
    if (obj.get_role_name() == 'text' and
        obj.get_name() == 'Buscador_Nombre'):
        break
else:
    process and process.kill()
    print("TEST 2: " + Fore.RED + "FAILED" + Fore.RESET)
    assert False, "No se puede encontrar el Entry nombre de búsqueda de persona"
obj.set_text_contents("Pilar")

# Se introduce el apellido
for obj in tree_walk(app):
    if (obj.get_role_name() == 'text' and
        obj.get_name() == 'Buscador_Apellido'):
        break
else:
    process and process.kill()
    print("TEST 2: " + Fore.RED + "FAILED" + Fore.RESET)
    assert False, "No se puede encontrar el Entry nombre de búsqueda de persona"
obj.set_text_contents("Campos")

# Se busca el botón 'Buscar'
for obj in tree_walk(app):
    if (obj.get_role_name() == 'push button' and
        obj.get_name() == 'Buscar'):
        break
else:
    process and process.kill()
    print("TEST 2: " + Fore.RED + "FAILED" + Fore.RESET)
    assert False, "No se pudo encontrar el botón 'Buscar'"

# Accionamos el boton 'Buscar'
for idx in range(obj.get_n_actions()):
    if obj.get_action_name(idx) == 'click':
        break
else:
    process and process.kill()
    print("TEST 2: " + Fore.RED + "FAILED" + Fore.RESET)
    assert False, "No se puede hacer 'click' en el boton 'Buscar'"
obj.do_action(idx)

time.sleep(1.1)

# Buscamos el Entry nombre tras la búsqueda
for obj in tree_walk(app):
    if (obj.get_role_name() == 'text' and
        obj.get_name() == 'Buscador_Nombre' and
        obj.get_text(0, -1) == ''):
        break
else:
    process and process.kill()
    print("TEST 2: " + Fore.RED + "FAILED" + Fore.RESET)
    assert False, "No se puede encontrar el Entry nombre de búsqueda de persona tras la búsqueda"

# Buscamos el Entry apellido tras la búsqueda
for obj in tree_walk(app):
    if (obj.get_role_name() == 'text' and
        obj.get_name() == 'Buscador_Apellido' and
        obj.get_text(0, -1) == ''):
        break
else:
    process and process.kill()
    print("TEST 2: " + Fore.RED + "FAILED" + Fore.RESET)
    assert False, "No se puede encontrar el Entry apellido de búsqueda de persona tras la búsqueda"

# Se busca el treeView
for obj in tree_walk(app):
    if (obj.get_role_name() == 'table' and obj.get_column_description(0)=="Nombre" and obj.get_column_description(1)=="Id"):
        break
else:
    process and process.kill()
    print("TEST 2: " + Fore.RED + "FAILED" + Fore.RESET)
    assert False, "No se pudo encontrar el treeView"

# Comprobamos la búsqueda (NOMBRE)
for obj in tree_walk(app):
    if (obj.get_role_name() == 'table cell' and obj.get_text(0,-1)=="Pilar Campos"):
        break
else:
    process and process.kill()
    print("TEST 2: " + Fore.RED + "FAILED" + Fore.RESET)
    assert False, "El resultado no coincide con la búsqueda"

# Comprobamos la búsqueda (Id)
for obj in tree_walk(app):
    if (obj.get_role_name() == 'table cell' and obj.get_text(0,-1)=="03438aad-71af-4774-bbca-7ba409bcac20"):
        break
else:
    process and process.kill()
    print("TEST 2: " + Fore.RED + "FAILED" + Fore.RESET)
    assert False, "El resultado no coincide con la búsqueda"

# EL TEST 2 TERMINA
print("   TEST 2: OK")
f = open("test_regist.txt", "w")
f.write("2 OK")
f.close()
process and process.kill()
