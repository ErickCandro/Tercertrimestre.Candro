from os import strerror

try:
    counter=0
    stream= open("","rt")
    char = stream.read(1)
    while char != '':
        print(char,end='')
        counter +=1
        char = stream.read(1)
    stream.close()
    print("\n\nCaracteres que contiene el archivo",counter)
except IOError as e:
    print("Se produjo un error de tipo E/S: ",strerror(e.errno))