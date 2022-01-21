""" 
EJERCICIO 5
Crear una lista con el contenido de esta tabla
ACCION  AVENTURA    DEPORTES
Accion: gta, cod, pubg
Aventura: assasins, crash bandicut, prince of persia
deportes: fifa, pro, motogp

Mostrar esta info ordenada
"""

tablas = [
    {
        "categoria": "ACCION",
        "juegos": ["GTA", " COD", "PUGB"]
    },
    {
        "categoria": "AVENTURAS",
        "juegos": ["ASSASINS", "CRASH", "PRINCE"]
    },
    {
        "categoria": "DEPORTES",
        "juegos": ["FIFA", "PRO", "MOTOGP"]
    }
 ]

for tabla in tablas:
    print(f"######### {tabla['categoria']} #########")
    for juegos in tabla["juegos"]:
        print(juegos)
        
        
    