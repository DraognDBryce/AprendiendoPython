"""
Una funcion es un conjunto de instrucciones agrupadas bajo un mismo nombre o un nombre concreto que pueden reutilizarse
invocando a la funcion tantas veces como sea necesario

def NOMBRE_DE_FUNCION(parametros):
    BLOQUE/CONJUNTO DE INSTRUCCIONES

NOMBRE_DE_FUNCION(mi_parametro)
"""
# EJEMPLO 1

print("##### EJEMPLO 1 #####")

# Definir la funcion
def muestraNombres():
    print("Antonio")
    print("Juan")
    print("Unai")
    print("Lucia")
    print("Sara")
    print("\n")

# Invocando las funciones
muestraNombres() # Podemos poner varios
#muestraNombres() 
#muestraNombres() 

# EJEMPLO 2 PARAMETROS
print("##### EJEMPLO 2 #####")

"""
def mostrarTuNombre(nombre, edad):
    print(f"Tu nombre es {nombre}")

    if edad >= 18:
        print("Es mayor de edad")
    else:
        print("Es menor de edad")

nombre = input("Introduce tu nombre: ")
edad = int(input("Introduce tu edad: "))
mostrarTuNombre(nombre, edad)
"""

# EJEMPLO 3 MAS EJEMPLOS DE PARAMETROS Y FUNCIONES
print("##### EJEMPLO 3 #####")

def tabla(numero):
    print(f"La tabla de multiplicar del {numero}")

    for contador in range(1,11):
        operacion = numero*contador
        print(f"{numero} X {contador} = {operacion}")
    print("\n")

tabla(3)

# EJEMPLO 3.1

"""
Cogemos la funcion y la implantamos dentro del bucle for, como si la invocaramos
pero fuera de la funcion, este es un potencial de las funciones
"""
for ntabla in range (1,11):
    tabla(ntabla)

# EJEMPLO 4 PARAMETROS OPCIONALES
print("##### EJEMPLO 4 #####")

# Al poner el valor None o False no hace falta que pongamos nada y ese parametro se vuelve opcional
# Si luego ponemos el valor, se revelara al haber puesto el if
def getEmpleado(nombre, dni = None):
    print("EMPLEADO")
    print(f"nombre: {nombre}")

    if dni != None:
        print(f"DNI: {dni}")

getEmpleado("Unai Torrecillas")


# EJEMPLO 5 RETURN O DEVOLVER DATOS
print("##### EJEMPLO 5 #####")

def saludame(nombre):
    saludo = f"Hola, saludos {nombre}"

    return saludo

print(saludame("Unai"))

# EJEMPLO 6
print("##### EJEMPLO 6 #####")

def calculadora(num1, num2, basicas = False):

    suma = num1 + num2
    resta = num1 - num2
    multi = num1 * num2
    div = num1 / num2

    cadena = ""

    cadena += "Suma: " + str(suma)
    cadena += "\n"
    cadena += "Resta: " + str(resta)
    cadena += "\n"
    cadena += "Multiplicacion: " + str(multi)
    cadena += "\n"
    cadena += "Division: " + str(div)

    return cadena
print(calculadora(5,5))

# EJEMPLO 7 FUNCIONES DENTRO DE OTRAS FUNCIONES
print("##### EJEMPLO 7 #####")

def getNombre(nombre):
    texto = f"El nombre es: {nombre}"
    return texto

def getApellidos(apellidos) :
    texto = f"Los apellidos son {apellidos}"
    return texto

"""
En vez de usar las funciones varias veces, podemos juntarlas
en una sola y asi llamarlas desde una sola.
"""

def devuelveTodo(nombre, apellidos):
    texto = getNombre(nombre) + "\n" + getApellidos(apellidos)
    return texto

print(devuelveTodo("Unai", "Torrecillas Martinez"))

# print (getNombre("Unai"), getApellidos("Torrecillas Martinez"))

# EJEMPLO 8 FUNCIONES LAMBDA
print("##### EJEMPLO 8 #####")

dime_el_year = lambda year: f"El año es {year}"
print(dime_el_year(2021))

