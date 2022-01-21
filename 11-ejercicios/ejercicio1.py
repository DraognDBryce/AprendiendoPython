"""
Ejercicio 1. Hacer un programa que tenga una lista de 8
numeros enteros y haga lo siguiente:

- Recorrer la lista y mostrarla
- Hacer una funcion que recorra listas de numeros y devuelva un string para mostrar
- Ordenarla y mostrarla
- Mostrar su longitud
- Buscar algun elemento (que el usuario pida por teclado)
"""

lista = [2, 6, 8, 20, 1, 3, 7]

# Recorrer la lista
for n in lista:
    print(n)

# Funcion que recorra con string la lista
def recorerLista():
    for n in lista:
        print("Numero: " + str(n))

recorerLista()

# Ordenar la lista
lista.sort()
print(lista)

# Mostrar su longitud
print(len(lista))

# Buscar elemento que el usuario pida por teclado


# Crear la lista
numeros = [13,64,52,73,21,7,91,63]

def mostrarLista(lista):
    resultado = ""
    
    for elemento in lista:
        resultado += "Elemento: " + str(elemento)
        resultado += "\n"
        
    return resultado

print(mostrarLista(numeros))

# Recorrer y mostrar
print("####### Recorrer y mostrar #######")
for numero in numeros:
    print(numero)


print("####### Ordenarla y mostrar #######")
numeros.sort()
print(mostrarLista(numeros))

print("####### Mostrar la longitud #######")
print(len(numeros))

"""
try:
    print("####### Busqueda en la lista #######")

    busqueda = int(input("Introduce el numero: "))

    comprobar = isinstance(busqueda, int)
    while not comprobar or busqueda <= 0:
        busqueda = int(input("Introduce el numero: "))
    else:
        print(f"Has introducido el {busqueda}")
        
    print(f"#### Buscar en la lsita el numero {busqueda} ####")


    search = numeros.index(busqueda)
    print(f"El numero buscado existe en la lista, es el indice {search}")
except:
    print("El numero no esta en la lista, lo siento")
"""


