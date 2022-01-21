"""
1.Las funciones pueden acceder a las variables GLOBALES sin ningun tipo de problema aunque esten debajo de ellas

2. Recomendable poner las funciones arriba del fichero, podemos invocarlas donde queramos

3. Recomendable que en vez de hacer print dentro de la funcion, que este devuelva un dato usando el return y luego aplicamos el print como invocacion, por ejemplo.
"""

def mi_funcion(nombre):
    return "Hola que tal" + nombre

def mi_funcion2(apellidos):
    return "Hola que tal2" + apellidos
    

nombre = "Unai"
apellidos = "Torrecillas"


print(mi_funcion(nombre))
print(mi_funcion2(apellidos))

