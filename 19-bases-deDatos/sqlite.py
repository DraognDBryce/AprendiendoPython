# Importar modulo
import sqlite3

# ? CONEXION A BASE DE DATOS
conexion = sqlite3.connect('pruebas.db')

# crear cursor
cursor = conexion.cursor()
# ? CREAR TABLA
cursor.execute("CREATE TABLE IF NOT EXISTS productos("+
               "id INTEGER PRIMARY KEY AUTOINCREMENT, "+
               "titulo VARCHAR(255), "+
               "descripcion TEXT, "+
               "precio int(255)"+
               
               ")")


# ? Cerrar la conexion
conexion.close()