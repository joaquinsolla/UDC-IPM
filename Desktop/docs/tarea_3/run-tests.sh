
COUNT=0
FAILED=0

echo  $'EXECUTING TESTS:'
echo  $'----------------'

python3 ipm-p1-test-1.py
((COUNT=COUNT+1))
if [[ $(cat test_regist.txt) != "1 OK" ]]; then
((FAILED=FAILED+1))
fi

python3 ipm-p1-test-2.py
((COUNT=COUNT+1))
if [[ $(cat test_regist.txt) != "2 OK" ]]; then
((FAILED=FAILED+1))
fi

python3 ipm-p1-test-3.py
((COUNT=COUNT+1))
if [[ $(cat test_regist.txt) != "3 OK" ]]; then
((FAILED=FAILED+1))
fi

python3 ipm-p1-test-4.py
((COUNT=COUNT+1))
if [[ $(cat test_regist.txt) != "4 OK" ]]; then
((FAILED=FAILED+1))
fi

python3 ipm-p1-test-5.py
((COUNT=COUNT+1))
if [[ $(cat test_regist.txt) != "5 OK" ]]; then
((FAILED=FAILED+1))
fi

python3 ipm-p1-test-6.py
((COUNT=COUNT+1))
if [[ $(cat test_regist.txt) != "6 OK" ]]; then
((FAILED=FAILED+1))
fi

python3 ipm-p1-test-7.py
((COUNT=COUNT+1))
if [[ $(cat test_regist.txt) != "7 OK" ]]; then
((FAILED=FAILED+1))
fi

python3 ipm-p1-test-c.py
((COUNT=COUNT+1))
if [[ $(cat test_regist.txt) != "C OK" ]]; then
((FAILED=FAILED+1))
fi

echo  $'----------------'
echo  $'DONE: '$COUNT'    FAILED: '$FAILED
rm test_regist.txt





#Give execution permissions to this script: chmod +x run-tests.sh

#----TESTS-------
# 1 - Lanzar App y mostrar vista 1
# 2 - Búsqueda de persona
# 3 - Selección de persona y muestra de sus datos
# 4 - Historial de Actividad de una persona
# 5 - Rastreo Contactos Persona
# 6 - Navegación de ventana
# 7 - Diálogo
# 8 - Concurrencia
