import mysql.connector

personas_db = mysql.connector.connect(

    host ="localhost",
    port="3303",
    user="root",
    password="admin",
    database="personas_db"

)


cursor = personas_db.cursor()
cursor.execute("SELECT * FROM personas")
resultado = cursor.fetchall()

for linea in resultado:

    print(linea)

cursor.close()
personas_db.close()