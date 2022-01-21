from coche import Coche

carro = Coche("Amarillo", "Renault", "Clio", 150, 200, 4)
carro2 = Coche("Verde", "Seat", "Panda", 220, 200, 4)
carro3 = Coche("Negro", "Citroen", "Sara", 150, 180, 4)

print(carro.getInfo())
print(carro2.getInfo())
print(carro3.getInfo())

# ? DETECTAR TIPADO

if type(carro3) == Coche:
    print("Es un objeto correcto")
else:
    print("No es un objeto")
    
# ? VISIBILIDAD

print(carro.soy_public)
#print(carro.__soyPrivado) NO SE PUEDE SI NO HAY UN METODO
print(carro.getPrivado()) # ESTO SI DEJA, YA QUE ES MEDIANTE UN METODO