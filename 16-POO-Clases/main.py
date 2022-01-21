# Programacion orientada a objetos

# Definir una clase, molde para crear mas objetos de ese tipo
# (Coche) Caracteristicas generales

class Coche:
    
    # ? Atributos o propiedades (Variables)
    # Caracteristicas del coche
    color = "Rojo"
    marca = "Ferrari"
    modelo = "Aventador"
    velocidad = 300
    caballaje = 500
    plazas = 2
    
    # ? Metodos, acciones que hacen el objeto
    
    def acelerar(self):
        self.velocidad += 1
    
    def frenar(self):
        self.velocidad -= 1
    
    def getVelocidad(self):
        return self.velocidad
    
    def setColor(self, color):
        self.color = color
        
    def getColor(self):
        return self.color
    
    def setModelo(self, modelo):
        self.modelo = modelo
    
    def getModelo(self):
        return self.modelo

# FIN DEFINICION CLASE

# Crear objeto/instanciar clase
coche = Coche() # ? Para crear la clase
print("COCHE 1: ")

coche.setColor("Amarillo")
coche.setModelo("Murcielago")

print(coche.marca, coche.getColor(),coche.getModelo()) # * Para sacar los atributos
print("Velocidad actual: ", coche.getVelocidad())

coche.acelerar()
coche.acelerar()
coche.acelerar()
coche.acelerar()

coche.frenar()

print("Velocidad actual: ", coche.getVelocidad())

print("--------------------------------------")
# ? CREAR MAS OBJETOS

coche2 = Coche()

print("COCHE 2: ")

coche2.setColor("Negro")
coche2.setModelo("Gallardo")

print(coche2.getColor(), coche2.getModelo(), coche2.marca)


print("--------------------------------------")
