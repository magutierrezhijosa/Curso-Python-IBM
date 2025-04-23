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
# Creamos la sentencia tipo UPDATE para actualizar un campo 
sentencia_sql = "UPDATE personas SET nombre=%s, apellido=%s, edad=%s WHERE id=%s"
# Guardamos en una variable los valores que vamos a actualizar en la DB
valores = ("Victoria", "Flores", 45, 5) 
# Llamamos al metodo execute() para ejecutar nuestra sentencia y agregar los valores que tenemos ya guardados en la variable 
cursor.execute(sentencia_sql,valores)
# Guardamos los cambios en la base de datos
personas_db.commit()
# Mostramos un mensage en pantalla que nos indique que se actualizaron los campos
print(f"Se ha modificado la informacion a : {valores}")
# Cerramos el cursor
cursor.close()
# Cerramos la DB 
personas_db.close()

