"""
CONDICIONAL IF (Si sucede una cosa, pasara esto)

SI(IF) Se_cumple_esta_condicion:
        Ejecutar grupo de instrucciones

SI NO(ELSE):
        Se ejecutan otro grupo de instrucciones


if condicion:
    instrucciones
else:
    instrucciones
"""

# EJEMPLO 1

print("\n##### EJEMPLO 1 #####")

color = "rojo"
#color = input("Adivina cual es mi color favorito\n")

if color == "rojo":
    print("Bien! El color es rojo")
else:
    print("El color incorrecto")

"""

OPERADORES CONDICIONALES
== Igual
!= diferente
< menor que
> mayor que
<= menor o igual
>= mayor o igual

OPERADORES LOGICOS
and - Y
or - O
! - Negacion
not - No
"""

print("\n#### EJEMPLO 2 ####")

year = 2021
#year= int(input("¿En que año estamos?:\n"))


if year <= 2021:
    print("Estamos antes o en 2021")
else:
    print("Año posterior a 2021")


# IF ANIDADOS
print("\n#### EJEMPLO 3 ####")

nombre = "Unai Torrecillas"
ciudad = "Almeria"
contiente = "Europa"
edad = 25
Mayoriaedad = 18

if Mayoriaedad >= 18:
    print(f"{nombre} es mayor de edad")

    if contiente != "Europa":
        print(f"El usuario {nombre} no es Europeo")
    else:
        print(f"{nombre} es Europeo y de la ciudad {ciudad}")

else:
    print(f"El usuario{nombre} no es mayor de edad")

print("\n#### EJEMPLO 4 ####")

dia = 1
#dia = int(input("Indique el dia de la semana:\n"))

if dia == 1:
    print("Es lunes")
elif dia == 2:
    print("Es martes")
elif dia == 3:
    print("Es miercoles")
elif dia == 4:
    print("Es jueves")
elif dia == 5:
    print("Es viernes")
elif dia == 6 or 7:
    print("Es fin de semana")
else:
    print("No existe ese dia de la semana")

print("\n#### EJEMPLO 5 ####")

"""
OPERADORES LOGICOS

and - Y
or - O
! - Negacion
not - No
"""

edadMinima = 18
edadMaxima = 65
edadReal = 18

if edadReal >= 18 and edadReal <= 65:
    print("Tiene edad para trabajar")
else:
    print("No tiene edad para trabajar")

print("\n#### EJEMPLO 6 ####")

pais = "Alemania"

if pais == "Mexico" or pais == "España" or pais == "Colombia":
    print(f"{pais} Es un pais de habla hispana")
else:
    print(f"{pais} no es un pais de habla hispana")

print("\n#### EJEMPLO 7 ####")

pais = "Alemania"

if not(pais == "Mexico" or pais == "España" or pais == "Colombia"):
    print(f"{pais} NO es un pais de habla hispana")
else:
    print(f"{pais} es un pais de habla hispana")

