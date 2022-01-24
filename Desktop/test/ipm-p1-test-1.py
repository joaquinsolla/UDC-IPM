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
# TEST 1 - Lanzar App y mostrar vista 1
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
    print("TEST 1: " + Fore.RED + "FAILED" + Fore.RESET)
    assert False, f"La aplicación no se muestra en el escritorio"

# Se busca el botón 'Previous' (flecha para ir a página anterior)
for obj in tree_walk(app):
    if (obj.get_role_name() == 'push button' and
        obj.get_name() == 'Previous_Page'):
        break
else:
    process and process.kill()
    print("TEST 1: " + Fore.RED + "FAILED" + Fore.RESET)
    assert False, "No se pudo encontrar el botón 'Previous_Page'"

# Se busca el botón 'Next' (flecha para ir a página siguiente que está oculta en un principio)
for obj in tree_walk(app):
    if (obj.get_role_name() == 'push button' and
        obj.get_name() == 'Next_Page'):
        break
else:
    process and process.kill()
    print("TEST 1: " + Fore.RED + "FAILED" + Fore.RESET)
    assert False, "No se pudo encontrar el botón 'Next_Page'"

# Se busca el botón 'Home' (botón nos lleva a la página de inicio)
for obj in tree_walk(app):
    if (obj.get_role_name() == 'push button' and
        obj.get_name() == 'Home_Button'):
        break
else:
    process and process.kill()
    print("TEST 1: " + Fore.RED + "FAILED" + Fore.RESET)
    assert False, "No se pudo encontrar el botón 'Home_Button'"

# Se busca el label de nombre de la ventana
for obj in tree_walk(app):
    if (obj.get_role_name() == 'label' and
        obj.get_text(0, -1) == "Rastreador Covid"):
        break
else:
    process and process.kill()
    print("TEST 1: " + Fore.RED + "FAILED" + Fore.RESET)
    assert False, "No se encuentra el Label 'Rastreador Covid'"

# Se busca el label de inicio
for obj in tree_walk(app):
    if (obj.get_role_name() == 'label' and
        obj.get_text(0, -1) == "Introduzca el nombre de la persona:" and
        obj.get_name() == 'Introducir_Persona_Label'):
        break
else:
    process and process.kill()
    print("TEST 1: " + Fore.RED + "FAILED" + Fore.RESET)
    assert False, "No se encuentra el Label 'Introduzca el nombre de la persona:'"

# Se busca el Entry nombre para buscar personas
for obj in tree_walk(app):
    if (obj.get_role_name() == 'text' and
        obj.get_name() == 'Buscador_Nombre' and
        obj.get_text(0, -1) == ""):    #Inicialmente vacío
        break
else:
    process and process.kill()
    print("TEST 1: " + Fore.RED + "FAILED" + Fore.RESET)
    assert False, "No se encuentra el Entry nombre para buscar personas"

# Se busca el Entry apellido para buscar personas
for obj in tree_walk(app):
    if (obj.get_role_name() == 'text' and
        obj.get_name() == 'Buscador_Apellido' and
        obj.get_text(0, -1) == ""):    #Inicialmente vacío
        break
else:
    process and process.kill()
    print("TEST 1: " + Fore.RED + "FAILED" + Fore.RESET)
    assert False, "No se encuentra el Entry apellido para buscar personas"

# Se busca el botón 'Buscar'
for obj in tree_walk(app):
    if (obj.get_role_name() == 'push button' and
        obj.get_name() == 'Buscar'):
        break
else:
    process and process.kill()
    print("TEST 1: " + Fore.RED + "FAILED" + Fore.RESET)
    assert False, "No se pudo encontrar el botón 'Home_Button'"

# Se busca el treeView
for obj in tree_walk(app):
    if (obj.get_role_name() == 'table' and obj.get_column_description(0)=="Nombre" and obj.get_column_description(1)=="Id"):
        break
else:
    process and process.kill()
    print("TEST 1: " + Fore.RED + "FAILED" + Fore.RESET)
    assert False, "No se pudo encontrar el treeView"

# EL TEST 1 TERMINA
print("   TEST 1: OK")
f = open("test_regist.txt", "w")
f.write("1 OK")
f.close()
process and process.kill()
