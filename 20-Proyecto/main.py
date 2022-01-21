""" 
PROYECTO PYTHON MYSQL:
- Abrir asistente
- Login o registro
- Si elegimos registro creara un usuario en la base de bbdd
- Crear nota, mostrar nostar o borrarlas
"""
from usuarios import acciones

print("""
Acciones disponibles:
    - Registro
    - Login
      """)

# ? Creamos el objeto
hazEl = acciones.Acciones()

accion = input("¿Que quieres hacer?: ").lower()
if accion == "registro":
    hazEl.registro()    

elif accion == "login":
    hazEl.login()