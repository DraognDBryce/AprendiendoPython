"""
Crear un programa donde saca el tanto por ciento que introduzca el ususario
"""

x = int(input("¿Que porcentaje quieres realizar?: "))
y = int(input("¿Que numero quieres hacer el porcentaje?: "))

porcentaje = x * (y / 100)

print(f"El {x} % de {y} es {porcentaje}")