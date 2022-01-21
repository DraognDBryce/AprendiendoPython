"""
EJERCICIO 3:
Programa que compruebe si una variable esta vacia y si esta vacia rellenarla con texto en minusculas y mostrarlo en mayusculas.
"""

texto = ""
texto2 = "esto es un texto en minusculas"

"""
if texto == "":
    print(texto2)
    print(texto2.upper())
else:
    print(texto)
"""
    
if len(texto.strip()) <= 0:
    # Mostrar texto
    print(texto2.upper)
else:
    print(f"La variable tiene contenido {texto}")

