""" 
- Capturar excepciones y manejo de errores en código
- Supceptibles a fallos/errores
"""
"""
try:
    nombre = input("¿Cual es tu nombre?: ")
    print(nombre)

    if len(nombre) > 1:
        nombre_usuario = f"El nombre es: {nombre}"
except:
    print("Ha ocurrido un error, mete bien el nombre")
    
else:
    print("Todo ha funcionado correctamente")
    
finally:
    print("Fin de la iteracion")
"""

# Multiples excepciones

"""
try:
    numero = int(input("Indique un numero para elevarlo al cuadrado: "))
    print("El cuadrado es " + str(numero * numero))
except TypeError:
    print("Debes convertir tus cadenas a enteros en el codigo")
except ValueError:
    print("Introduce un numero correcto")
except Exception as e:
    print("Ha ocurrido un error", type(e).__name__) # Para ver el error que da en ese momento en vez de hacerlo 1 a 1
"""

# Excepciones personalizadas o lanzar excepciones

try:
    nombre = input("Introduce el nombre: ")
    edad = int(input("Introduce la edad: "))

    if edad < 5 or edad > 110:
        raise ValueError("La edad introducida no es real")
    elif len(nombre) <= 1:
        raise ValueError("El nombre no esta completo")
    else:
        print("Bienvenido al master en Python" + nombre)
except ValueError:
    print("Introduce los datos correctamente")