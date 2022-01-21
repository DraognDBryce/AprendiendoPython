import sqlite3

# ? 1. Crear-Abrir la conexion
miConexion = sqlite3.connect("PrimeraBase.db")

# ? 2.Crear el cursor
miCursor = miConexion.cursor()

# ? 3.Ejecutar la consulta
miCursor.execute("CREATE TABLE productos (NOMBRE_ARTICULO VARCHAR)")

# Cerrar la conexion
miConexion.close()
