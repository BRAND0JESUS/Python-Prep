''' Crear un script con el nombre "clase09_ej2.py2" que reciba como un valor de temperatura en grados centígrados, un valor de humedad y por último si llovio (Con True o False). Y que cada vez que sea invocado, cargue en el archivo provisto "clase09_ej2.csv" una marca de tiempo y esa información.

Para trabajar con tipos de datos relacionados con la medición del tiempo, como ser fechas, horarios o marcas de tiempo se puede utilizar la clase *datetime*

import datetime

x = datetime.datetime.now()
print("Ahora =",x)
x = datetime.datetime(2020, 5, 10)
print("Fecha fija =",x)

fecha_hora = '2022-05-10 12:30:00'
objeto_datetime = datetime.datetime.strptime(fecha_hora, '%Y-%m-%d %H:%M:%S')
print("objeto datetime =", objeto_datetime)
marca_de_tiempo = datetime.datetime.timestamp(objeto_datetime)
print("timestamp =", marca_de_tiempo)
fecha_hora2 = datetime.datetime.fromtimestamp(marca_de_tiempo)
print("fecha hora =", fecha_hora2)
'''

import sys
import datetime
import os

if (len(sys.argv) == 4):

    x = datetime.datetime.now()
    x = datetime.datetime(2020, 5, 10)

    fecha_hora = '2022-05-10 12:30:00'
    objeto_datetime = datetime.datetime.strptime(fecha_hora, '%Y-%m-%d %H:%M:%S')
    marca_de_tiempo = datetime.datetime.timestamp(objeto_datetime)
    fecha_hora2 = datetime.datetime.fromtimestamp(marca_de_tiempo)
    # open file
    fd = open('clase09_ej2.csv', 'a') # file descriptor
    # write text
    texto = str(marca_de_tiempo) + ',' + sys.argv[1] + ',' + sys.argv[2] + ',' +sys.argv[3] +'\n'
    fd.write(texto)
    # close file
    fd.close()

else:
    print ('The amount of parameters are incorrect, verify')


