"""
EJERCICIO 4:
Crear un script que tenga 4 variables, una lista, un string, un entero y un booleano y que imprima un mensaje segun el tipo de dato de cada variable.
"""
def traducirtipo(tipo):
    result = None
    if tipo == list:
        result = "LISTA"
    elif tipo == str:
        result == "STRING"
    elif tipo == int:
        result == "ENTERO"
    elif tipo == bool:
        result == "BOOLEANO"
    
    return result
    
def comprobar(dato, tipo):
    test = isinstance(dato, tipo)
    result = ""
    if test:
        print(f"Este dato es de tipo {traducirtipo(tipo)}")
    else:
        result = "El archivo no corresponde"
    return result
        
lista = ["Unai", 25]
hola = "Soy una String"
num = 25
verdadero = True

print(comprobar(lista, list))
print(comprobar(hola, str))
print(comprobar(num, int))
print(comprobar(verdadero, bool))

    
    


