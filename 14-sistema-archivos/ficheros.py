
from io import open
import pathlib
# abrir Archivo
ruta = str(pathlib.Path().absolute()) + "/ficheros_texto.txt"
archivo = open(ruta , "a+")

# Escribir dentro de un archivo
archivo.write("\nSoy un texto metido desde Python\n")

# Cerrar archivo
archivo.close()

# Abrir archivo
ruta = str(pathlib.Path().absolute()) + "/ficheros_texto.txt"
archivo_lectura = open(ruta , "r")

# Leer contenido
#contenido = archivo_lectura.read()
#print(contenido)

# Leer contenido y guardarlo en lista
lista = archivo_lectura.readlines()
archivo_lectura.close()
for frase in lista:
    print("- " + frase.upper())
    
