"""
Hacer un programa que muestre todos los numeros que muestre el usuario
"""

num1 = int(input("Indique un primer numero: "))
num2 = int(input("Indique un segundo numero: "))

if num1 < num2:
    for contador in range(num1, num2 + 1):
        print(contador)
elif num1 > num2:
    for contador in range(num2, num1 + 1):
        print(contador)
else:
    print(f"Solo aceptamos numeros, el conjunto {num1} y {num2} no son validos")