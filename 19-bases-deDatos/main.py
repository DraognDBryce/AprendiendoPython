import mysql.connector

# ? Conexion
database = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "",
    database = "master_python" # * Poner al crear la DATABASE
)

# ? Saber si la conexion ha sido correcta
# print(database)

# ? Cursor para crear las consultas
cursor = database.cursor(buffered = True)

# ! CREAR LA BASE DE DATOS
# ? Hacer consultas
cursor.execute("CREATE DATABASE IF NOT EXISTS master_python") # * Crear la DATABASE
cursor.execute("SHOW DATABASES") # * Mostrar la DATABASE

# * Recorrer la DATABASE
for bd in cursor:
    print(bd)

print("-------------")

# ! CREAR TABLAS
cursor.execute(""" 
CREATE TABLE IF NOT EXISTS vehiculos(
    id int(10) auto_increment not null,
    marca varchar(40) not null,
    modelo varchar(40) not null,
    precio float(10,2) not null,
    CONSTRAINT pk_vehiculo PRIMARY KEY(id)
    
)
               """)

cursor.execute("SHOW TABLES")

for table in cursor:
    print(table)
    
# ! INSERTAR DATOS DENTRO DE UNA TABLA
#cursor.execute("INSERT INTO vehiculos VALUES(null,'Opel', 'Astra', 18500)")
coches = [
    ('Seat', ' Ibiza', 5000),
    ('Renault', 'Clio', 15000),
    ('Critoen', 'Saxo', 2000),
    ('Mercedez', 'Clase C', 25000)
]

# * Los %s es pasa sustituir los valores, al añadirle la variable en forma de tupla los pondra
#cursor.executemany("INSERT INTO vehiculos VALUES(null, %s, %s, %s)", coches)

database.commit() # * Sin hacer esto no guardara realmente los datos en la tabla

# ! SACAR INFO DE LA BASE DE DATOS
# ? Sacar PARTES CONCRETAS de la tabla
# cursor.execute("SELECT marca, modelo, precio FROM vehiculos")

# ? Sacar TODA la info de dentro de la tabla
# * Si ponemos un WHERE con ello sacamos algo especifico, como en este caso los precios <= 5000 y con el AND, como operador logico le decimos otra especificacion
cursor.execute("SELECT * FROM vehiculos WHERE precio <= 5000 AND marca = 'Seat'")
result = cursor.fetchall() # fetchone CON ESTO SOLO NOS SACA UN DATO

print("----- TODOS MIS COCHES ----- ")

for coche in result:
# *  Como sacamos las cosas de las listas, aqui podemos hacer lo mismo, en este caso sacaremos las marcas
    print(coche[1] ,coche[3]) 

cursor.execute("SELECT * FROM vehiculos")

# * Nos sacara el primer coche de la tabla
coche = cursor.fetchone()
print(coche)

# ? BORRAR REGISTROS DE UNA TABLA
cursor.execute("DELETE FROM vehiculos WHERE marca = 'Mercedez'")
database.commit() # Ejecuta el cambio

print(cursor.rowcount, "Borrados!!") # Para indicar cuantos registros se han borrado

# ? ACTUALIZAR DATOS
cursor.execute("UPDATE vehiculos SET modelo = 'Leon' WHERE marca = 'Seat'")
database.commit()

print(cursor.rowcount, "Actualizado!!")
