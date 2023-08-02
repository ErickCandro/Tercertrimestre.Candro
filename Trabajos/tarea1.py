#para leer un archivo csv se podria hacer de la siguiente manera:
from os import strerror
import csv
#Donde se importa csv y se usa la funcion with open para abrir el archivo que se desea 
try:
    with open('archivo.csv') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            print(', '.join(row))
except IOError as e:
    print("se a generado un error tipo e/s",strerror(e.errno))





#un ejemplo con escritura puede ser el siguiente:
import csv
#en donde nuevamente como en el anterior caso se habre el archivo pero en este caso se le agrega "w"
#para poder escribir en el 
with open('archivo.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Nombre', 'Apellido', 'Edad'])
    writer.writerow(['Juan', 'Perez', 25])
    writer.writerow(['Maria', 'Lopez', 30])