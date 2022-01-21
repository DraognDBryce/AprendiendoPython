from random import randint

"""
def main():
    
    print(" #### ADIVINA EL NUMERO #### \n")
    numero_random = randint(1,15)
    numero_usuario = int(input("Indique un numero del 1 al 15: "))
    
    if numero_usuario == numero_random:
        print(f"ENHORABUENA! {numero_usuario} es el numero correcto")
    else:
        print(f"FALLO! el numero correcto es {numero_random}")
    
    main()
main()
"""

numero_random = randint(1,15)
numero_usuario = int(input("Indique un numero del 1 al 15: "))

while numero_usuario != numero_random:
    if numero_usuario < numero_random:
        print("El numero es BAJO, intentalo de nuevo\n")
        numero_usuario = int(input("Indique un numero del 1 al 15: "))
    else:
        print("El numero es ALTO, intentelo de nuevo\n")
        numero_usuario = int(input("Indique un numero del 1 al 15: "))
        
print("Has adivinado el nuermo correcto!, este era " + str(numero_random))
    