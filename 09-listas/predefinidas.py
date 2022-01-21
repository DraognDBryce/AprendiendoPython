cantantes = ["2pac", "Drake", "Bad Bunny", "Julio Iglesias"]
numeros = [1, 2, 5, 6, 3, 4,]

# Ordenadr una lista
print(numeros)
numeros.sort() # Ordena la lista
print(numeros)

# Añadir elementos
cantantes.append("Natos y Waor")
cantantes.insert(1,"David Bisbal") #Aqui añadimos, PERO, tenemos que decir en que indice lo colocaremos moviendo de posicion el que esta en esa posicion
print(cantantes)

# Eliminar elementos
cantantes.pop(1) # Elimina por indice
print(cantantes)
cantantes.remove("Bad Bunny") # Elimina por nombre
print(cantantes)

# Dar la vuelta a la lista
print(numeros)
numeros.reverse()
print(numeros)

# Buscar dentro de una lista
print("Drake" in cantantes) # Devolvera True si esta dentro de la lista

# Contar elementos
print(cantantes)
print(len(cantantes))

# Cuantas veces aparece un elemento
numeros.append(8)
print(numeros.count(8))

# Conseguir indice
print(cantantes.index("Drake"))

# Unir listas
cantantes.extend(numeros)
print(cantantes)
