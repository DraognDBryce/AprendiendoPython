"""
- Mostrar todas las tablas de multiplicar del 1 al 10
- Mostrando el titulo de la tabla y luego las multiplicaciones del 1 al 10
"""

contador = 0

while contador <= 10:
    print(f"\nTABLA DE MULTIPLICAR DEL {contador}")
    for tablas in range(1,11):
        print(f"{contador} X {tablas} = {tablas*contador}")
    contador +=1