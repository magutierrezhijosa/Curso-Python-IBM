from mysql.connector import pooling
from mysql.connector import Error       

# Creo la clase Conexion para tener un pool de objetos tipo conexion
# y asi conseguir que los usuarios que se concectan puedan acceder 
# mas rapido a la DATABASE 
class Conexion:
    DATABASE = "zona_fit_db"
    USERNAME = "root"
    PASSWORD = "admin"
    DB_PORT = "3303"
    HOST = "localhost"
    POOL_SIZE = 5
    POOL_NAME = "zona_fit_pool"
    pool = None

    # Creamos el metodo de clase 
    @classmethod
    # Definimos el motodo de clase con un parametro tipo ***cls*** que nos va a permitir acceder a todas las constantes de nuestra clase
    def obtener_pool(cls):
        if cls.pool is None: # Se crea el objeto pool
            try:
                cls.pool = pooling.MySQLConnectionPool(


                )
            except Error as e:
                print(f"Ocurrio un error al obtener pool: {e}")