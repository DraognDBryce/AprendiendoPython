""" 
Son funcionalidades ya hechas para reutilizar.
En python por defecto hay muchos modulos que los puedes consultar aqui:
https://docs.python.org/3/py-modindex.html

Podemos conseguir modulos que ya estan en el lenguajes, en internet o crear nuestros modulos
"""
import datetime
#import mimodulo
#from mimodulo import holaMundo
from mimodulo import *

#print(mimodulo.holaMundo("Unai"))
#print(mimodulo.calculadora(5,5,False))

print(holaMundo("Antonio"))

# Modulo Fechas
print(datetime.date.today())
fechaCompleta = datetime.datetime.now()
print(fechaCompleta)
print(fechaCompleta.year)
print(fechaCompleta.day)

fechaFormateada = fechaCompleta.strftime("%d/%m/%y, %H:%M:%S")

print("Mi fecha personalizada: " + fechaFormateada)

# MODULOS MATEMATICAS
import math

# Sacar la raiz cuadrada de un numero
print("Raiz cuadrada de 10: ", math.sqrt(10))
print("Numero PI: ", math.pi)
print("Redondear: ", math.ceil(5.91283)) # Redondear a la alta
print("Redondear: ", math.floor(5.91283)) # Redondear a la baja

# MODULO RANDOM
import random
print("Numero aleatorio: ", random.randint(15,67))
