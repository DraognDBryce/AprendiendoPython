"""
BUCLE WHILE

Estructura de control que itera o repite la ejecucion de una serie de instrucciones tantas veces como sea necesario
hasta que deje de cumplirse la condicion.

While condicion:
    BLOQUE DE INSTRUCCIONES
    actualizacion de contador
"""
print("\n##### EJEMPLO 1 #####")
contador = 1
while contador <= 20:
    print(f"Estoy en el numero {contador}")
    contador +=1

print("\n##### EJEMPLO 2 #####")
contador = 1
muestrame = str(0)
while contador <= 50:
    
    muestrame = muestrame + "," + str(contador)
    contador +=1
print(muestrame)

print("\n##### EJEMPLO 3 #####")

numeroUsuario = int(input("Indique un numero para la tabla: "))

if numeroUsuario < 1:
    numeroUsuario == 1
print(f"TABLA DE MULTIPLICAR DEL {numeroUsuario}")

contador = 1
while contador <= 10:
    print(f"{numeroUsuario} X {contador} = {numeroUsuario*contador}")
    contador +=1
else:
    print("TABLA FINALIZADA")