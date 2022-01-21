"""
Hace un programa que pida numeros al ususario indifinidamente hasta meter el numero 111
"""


contador = 1

while contador < 100:
    numero = int(input("Adivina el numero: "))
    if numero == 111:
        print("Felicidades, adivino el numero!!")
        break
    else:
        print("Intentelo de nuevo")