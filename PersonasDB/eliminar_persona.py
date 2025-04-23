# Eliminar registros desde python a mysql
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

# Declaramos la sentencia de sql que vamos a realizar a la DB
sentencia_sql = "DELETE FROM personas WHERE id=%s"

# Agregamos los valores que vamos a necesitar para hacer la consulta
# IMPORTANTE para que lo recoja como una tubla debemos agregar la coma al final
valores = (5,)

# Ejecutamos la sentenciar con el metodo execute()
cursor.execute(sentencia_sql, valores)

# Guardamos los cambios en la DB
personas_db.commit()

# Mostramos un mensaje para confirmar que se ha relizado la accion
print(f"Se ha eliminado el campo con el id : {valores}")

# Cerramos el cursor
cursor.close()
# Cerramos la DB
personas_db.close()
