"""
- Escribir un programa que muestre los cuadrados (numero multiplicado por si mismo) de los 60 primeros numeros naturales
- Resolver con while y for
"""

# WHILE
print("\n ###### BUCLE WHILE ######")
contador = 0
while contador <= 60:

    cuadrado = contador * contador
    print(f"El cuadrado de {contador} es {cuadrado}")
    
    contador += 1

# FOR
print("\n ###### BUCLE FOR ######")
for contador in range(61):

    cuadrado = contador * contador
    print(f"el cuadrado de {contador} es {cuadrado}")
