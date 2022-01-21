"""
LISTAS (arrays)
Son colecciones o conjuntos de datos/valores, bajo un unico nombre.

para acceder a esos valores podemos usar un indice numerico
"""

pelicula = "Batman"

# Definir una lista
peliculas = ["Batman", "Spiderman", "El señor de los anillos"]
cantantes = list(("2pac", "Drake", "Jennifer Lopez"))
years = list(range(2020,2050))
variada = ["Unai", 20, 4.6, True, "Texto"]


#print(peliculas)
#print(cantantes)
#print(years)
#print(variada)


# Indices
pelicula = "Otra cosa"
peliculas[1] = "Gran Tornio" # Cambiando Spiderman x Gran Torino
print(peliculas)

print(peliculas[1]) # Seleccionar una parte
print(peliculas[-2]) # Seleccionar en negatrivo la parte
print(cantantes[0:2]) # Desde hasta
print(peliculas[1:]) # A partir de

# AÑADIR ELEMENTO A LISTA

cantantes.append("Kase O") # añadir a la lista con append()
print(cantantes)

# RECORRER LISTA
"""print("\n##### LISTADO DE PELICULAS #####")

nuevaPelicula = ""
while nuevaPelicula != "parar":
    nuevaPelicula = input("Introduce la nueva pelicula: ")

    if nuevaPelicula != "parar":
        peliculas.append(nuevaPelicula)

for pelicula in peliculas:
    #Con index nos saca el numero del indice de la pelicula
    print(f"{peliculas.index(pelicula)+1}. {pelicula}")

"""
# Listas multidimensionales

print("\n ####### LISTADO DE CONTACTOS ########")
contactos = [
    [
        "Antonio",
        "antonio@antonio.com"
    ]
    [
        "Luis",
        "luis@gmail.com"
    ]
    [
        "Salvador",
        "salvador@gmail.com"
    ]
]
for contacto in contactos:
    for elemento in contacto:
        if contacto.index(elemento) == 0:
            print("Nombre: " + elemento)
        else:
            print("Email: " + elemento)
    print("--------------")
# print(contactos[1][1])
