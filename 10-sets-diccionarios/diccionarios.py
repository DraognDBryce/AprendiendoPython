"""
Diccionario:
Es un tipo de dato que almacena un conjunto de datos en 
formato clave > valor.
Es parecido a un array asociativo o un objeto json.
"""

persona = {
    "nombre": "Unai",
    "apellidos": "Torrecillas",
    "web": "unaitorrecillas.es"
}

print(persona["apellidos"]) #Para sacar el valor

# Lista con diccionarios

contactos = [
    {
        'nombre': 'Unai',
        'email': 'unai@uani.com'
    },
    {
        'nombre': 'Antonio',
        'email': 'antonio@antonio.com'
    },
    {
        'nombre': 'Salvador',
        'email': 'salvador@salvador.com'
    }
]
contactos[0]['nombre'] = 'Antoñito'
print(contactos[0]['nombre'])

print('\nListado de contactos: ')

for contacto in contactos:
    print("-----------------------------")
    print(f'Nombre del contacto: {contacto["nombre"]}')
    print(f'Email de contacto: {contacto["email"]}')
    print("-----------------------------")