class Coche:
    
    # * ATRIBUTOS
    
    color = "Rojo"
    marca = "Ferrari"
    modelo = "Aventador"
    velocidad = 300
    caballaje = 500
    plazas = 2
    
    soy_public = "Hola, soy un atributo publico"
    __soyPrivado = "Hola, soy un atributo privado" # ! AL TENER __ DELANTE ES UN ATRIBUTO O VARIABLE PRIVADA
    
    def __init__(self, color, marca, modelo, velocidad, caballaje, plazas):
        self.color = color
        self.marca = marca
        self.modelo = modelo
        self.velocidad = velocidad
        self.caballaje = caballaje
        self.plazas = plazas
        
    def getPrivado(self):
        return self.__soyPrivado
        
    
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
    
    def setMarca(self, marca):
        self.marca = marca
        
    def getMarca(self):
        return self.marca
    
    def getInfo(self): # ! COMO UN TOSTRING DE JAVA
        info =  "----- INFORMACION DEL COCHE ------"
        info += "\n COLOR: " + self.getColor()
        info += "\n MARCA: " + self.getMarca()
        info += "\n MODELO: " + self.getModelo()
        info += "\n VELOCIDAD: " + str(self.getVelocidad())
        
        return info
        

    # * FIN DEFINICION CLASE