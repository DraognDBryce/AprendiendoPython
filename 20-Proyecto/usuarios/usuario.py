import hashlib
import usuarios.conexion as conexion
import datetime

connect = conexion.conectar()
database = connect[0]
cursor = connect[1]

class Usuario:
    
    # ? Constructor
    def __init__(self,nombre, apellido, email, pasword):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.pasword = pasword
    
    
    def registrar(self):
        fecha = datetime.datetime.now()
        
        # ? Cifrar contraseña
        cifrado = hashlib.sha256()
        cifrado.update(self.pasword.encode('utf-8'))
        sql = "INSERT INTO usuarios VALUE(null, %s, %s, %s, %s, %s)"
        usuario = (self.nombre, self.apellido, self.email, cifrado.hexdigest(), fecha)
        
        # ? Para manejar los posibles errores
        try: 
            cursor.execute(sql, usuario)
            database.commit()
            result = [cursor.rowcount, self]
        except:
            
            result = [0, self]
        
        return result
        
    def identificar(self):
        pass
        