""" 
PROYECTO PYTHON MYSQL:
- Abrir asistente
- Login o registro
- Si elegimos registro creara un usuario en la base de bbdd
- Crear nota, mostrar nostar o borrarlas
"""
from objetos import acciones

inicio = input("Bienvenid@ ¿Que desea? \n-Registro \n-Login").lower()

if inicio == "registro":
    acciones.registro()
    
elif inicio == "login":
    acciones.login()
    

