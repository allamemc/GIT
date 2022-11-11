import os
import random

for n in range(5):
    nombre_carpeta='alumno_'+str(random.randint(100, 999))
    os.mkdir(nombre_carpeta)