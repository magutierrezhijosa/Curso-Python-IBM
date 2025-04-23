import mysql.connector

# Creamos la conexion a MySQL 
personas_db = mysql.connector.connect(

    host ="localhost",
    port="3303",
    user="root",
    password="admin",
    database="personas_db"

)

# Agregamos le objeto cursor() que no nos permite enviar y recibir consultas SQL
cursor = personas_db.cursor()
# En esta linea ejecutamnos la consulta que queramos hacer a nuestra DB 
cursor.execute("SELECT * FROM personas")
# Recogemos el resultado de la consulta y lo guardamos en una variable 
resultado = cursor.fetchall()

# Recorremos las lineas del resultado iterando con un for
for linea in resultado:
    # Mostramos en pantalla los resultados
    print(linea)

# Tras realizar nuestras operaciones cerramos el cursor 
cursor.close()
# Cerramos la base de datos
personas_db.close()