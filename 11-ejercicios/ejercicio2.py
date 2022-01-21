"""
Ejercicio 2. 
Escribir un programa que añada valores a una lista mientras que su longitud sea menor a 120 y luego mostrar
la lista.
    
Plus: Usar while y for
    
"""

coleccion = []
x = 0
while x < 120:
    coleccion.append(f"Elemento = {x}") 
    print("Mostrando el " + coleccion[x])
    x += 1


"""
coleccion = []

for contador in range(0,120):
    coleccion.append(f"Elemento-{contador}")
    print(f"Mostrando el = " + coleccion[contador])
print(coleccion)
"""

