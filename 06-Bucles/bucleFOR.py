"""
for variable in elemento_iterable (lista, rango, etc):
    BLOQUE DE INSTRUCCIONES
"""

contador = 0

for contador in range(0, 5):
    print("Voy por el " + str(contador))

# EJEMPLO CON TABLAS DE MULTIPLICAR

print("\n ##### EJEMPLO 1 #####")

numeroUsuario = int(input("¿De que numero quieres la tabla?: "))

if numeroUsuario >= 1:
    print(f"Tabla de multiplicar del numero {numeroUsuario}")

for numero_tabla in range(0,11):

    if numeroUsuario == 45:
        print("No se pueden mostrar numeros prohibidos")

        # Cortar el bucle
        break
    
    print(f"{numeroUsuario} X {numero_tabla} = {numeroUsuario*numero_tabla}" )
else:
    print("Tabla terminada")
