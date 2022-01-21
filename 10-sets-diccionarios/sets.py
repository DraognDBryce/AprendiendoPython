"""
Tipo de dato para tener una coleccion de valores, pero no tiene
ni indice ni orden
"""

personas = {
    "Unai",
    "Manolo",
    "Francisco"
}

personas.add("Paco") #Añadir al sets
personas.remove("Francisco") #Quitar del sets

print(type(personas))
print(personas)