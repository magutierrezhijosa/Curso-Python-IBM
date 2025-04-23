# Insertar registros en MySQL 
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

# Ejecutamos la sentencia INSERT 
sentencia_sql = "INSERT INTO personas(nombre, apellido, edad) VALUES(%s , %s, %s)"
# Guardamos la nueva entrada en una variable
valores = ("Victor", "Ramos", 46)
# Ejecutamos la sentencia
cursor.execute(sentencia_sql, valores)
# Ejecutamos el metodo commit para guardar los cambios en la DB
personas_db.commit()
# Mostramos un mensage de confirmacion de que se ha modificado la DB
print(f"Se ha agregado el nuevo registro a la DB : {valores}")
# Cerramos el cursor 
cursor.close()
# Cerramos la base de datos
personas_db.close()