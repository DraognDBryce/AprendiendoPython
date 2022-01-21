from usuario import Usuario

class Acciones:
    def registro(self):
        print("Bienvenid@ a la sesion de registro")
        nombre = input("Indique su NOMBRE: ")
        apellido = input("Indique su APELLIDO: ")
        email = input("Inidique su EMAIL: ")
        pasword = input("Indique su CONTRASEÑA: ")

    def login(self):
        email = input("Email: ")
        pasword = input("Contraseña: ")