from mysql.connector import pooling
from mysql.connector import Error


# Creo la clase Conexion para tener un pool de objetos tipo conexion y asi conseguir que
# los usuarios que se conectan puedan acceder mas rapido a la DATABASE
class Conexion:
    DATABASE = "inventario_db"
    USERNAME = "root"
    PASSWORD = "admin"
    DB_PORT = "3303"
    HOST = "localhost"
    POOL_SIZE = 5
    POOL_NAME = "zona_fit_pool"
    pool = None

    @classmethod
    # Definimos el metodo de la clase con un parametro tipo ***cls*** que 
    # nos va a permitir acceder a todas las constantes de nuestra clase 
    def obtener_pool(cls):
        # Si la variable clase pool es None
        if cls.pool is None: # Se crea el objeto pool 

            try:
                # Creamos el objeto de tipo pool donde vamos a guardar nuestras conexiones
                cls.pool = pooling.MySQLConnectionPool(
                    # Agregamos valores de cada una de las constantes que hemos definido
                    pool_name = cls.POOL_NAME,
                    pool_size = cls.POOL_SIZE,
                    host = cls.HOST,
                    port = cls.DB_PORT,
                    database = cls.DATABASE,
                    user = cls.USERNAME,
                    pasword = cls.PASSWORD

                )

            except Exception as e:
                print(f"Ocurrio un error al obtener el pool: {e}")

        # En el caso de que no sea None retornamos el objeto tipo pool
        else:
            return cls.pool