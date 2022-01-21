import usuarios.usuario as modelo

class Acciones:
    
    def registro(self):
        
        # ? Las opciones y datos
        print("\nDe acuerdo! Vamos a comenzar el registro")
        nombre = input("¿Cual es tu nombre?: ")
        apellido = input("¿Cuales son tus apellidos?: ")
        email = input("Introduce tu email: ")
        pasword = input("Introduce tu contraseña: ")
        
        # ? Creamos el objeto
        usuario = modelo.Usuario(nombre, apellido, email, pasword)
        registro = usuario.registrar()
        
        if registro[0] >= 1:
            
            print(f"Perfecto {registro[1].nombre} te has registrado con el email {registro[1].email}")
        else:
            print("No te has registrado correctamente")
        
    def login(self):
        print("\nIdentificate en el sistema")
        email = input("Introduce tu email: ")
        pasword = input("Introduce tu contraseña: ")