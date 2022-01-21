"""
Variable locales: Se definen dentro de la funcion y no se puede
usar fuera de ella, solo estan disponibles dentro.
A no ser que hagamos un return.

Variables globales: Son las que se declaran fuera de una 
funcion y estan disponibles dentro y fuera de ella
"""

# Variable global
frase = "Dorime, y muchas cosas mas que no me acuerdo"
print(frase)

# Variable local
def holaMundo():
    frase = "Hola Mundo!!"
# Si comentamos esta variable lo que harémos es que use la 
# variable global y esta no la podemos usar fuera de la funcion
    global website 
#Con esto haremos que la variable sea global aun dentro de una funcion
    website = "Una pagina web"
    print(frase)

holaMundo()