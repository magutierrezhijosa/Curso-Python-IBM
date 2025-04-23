# Actualizar registros desde python a mysql
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
