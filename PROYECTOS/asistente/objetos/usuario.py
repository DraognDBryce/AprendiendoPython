from datetime import datetime
import mysql.connector

database = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "",
    databse = "master_python",
    port = 3306
)

cursor = database.cursor(buffered = True)

class Usuario:
    
    def __init__(self, nombre, apellido, email, pasword):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.pasword = pasword
    
    def registrar(self):
        time = datetime.date.now
        sql = "INSERT INTO usuarios VALUE(null, %s, %s, %s, %s, %s)"
        usuario = self.nombre, self.apellido, self.email, self.pasword, time
        
        try:
            cursor.execute(sql, usuario)
            database.commit()
            result = [cursor.rowcount, self]
        except:
            result = [0, self]
        
        return result
    
    def login(self):
        pass
        