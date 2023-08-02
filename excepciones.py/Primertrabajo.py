from os import strerror

try:
    file = open ("","wt")
    nombre =str(input("introdusca el nombre a guardar: "))
    apellidos= str (input("Introdusca el apellido que desea guardar: "))
    telefono = int(input("Ingrese el numero que desea almacenar:"))
    Dirrecion = str (input("Ingrese la dirrecion a guardar:"))
    
    for i in range (10):
        file.write(nombre+"\n")
        file.write(apellidos+"\n")
        file.write(telefono+"\n")
        file.write(Dirrecion+"\n")
    file.close()

except IOError as e:
    print("Se produjo un error de E/S:",strerror(e.errno))