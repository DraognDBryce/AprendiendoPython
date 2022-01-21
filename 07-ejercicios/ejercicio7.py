"""
Hacer un programa que muestre todos los numeros impares entre 2 numeros que elija el usuario
"""

num1 = int(input("Indique el primer numero: "))
num2 = int(input("Indique el segundo numero: "))

if num1 < num2:
    for contador in range(num1, num2 +1):
        if contador % 2 == 1:
            print(contador)
elif num1 > num2:
    for contador in range(num2, num1 +1):
        if contador % 2 == 1:
            print(contador)
