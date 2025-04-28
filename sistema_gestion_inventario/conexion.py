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
    POOL_NAME = "inventario_pool"
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
                    password = cls.PASSWORD

                )
                return cls.pool
            except Exception as e:
                print(f"Ocurrio un error al obtener el pool: {e}")

        # En el caso de que no sea None retornamos el objeto tipo pool
        else:
            return cls.pool
        
    
    @classmethod
    # Metodo par acrear nuevos objetos de tipo conexion 
    def obtener_conexion(cls):
        return cls.obtener_pool().get_connection()
    
    @classmethod
    # Metodo para cerrar la conexion una vez se haya usado
    def liberar_conexion(cls,conexion):
        conexion.close()

# # Prueba par comprobar que todo funciona correctamente y esta bien importado
# if __name__ == "__main__":

#     # Creamos un objeto pool
#     conexion = Conexion()
#     print(conexion)
#     # Creamos un objeto de tipo conexion 
#     pool = conexion.obtener_pool()
#     obtener_conexion = conexion.obtener_conexion()
#     print(obtener_conexion) 
#     print(pool) 
#     # Por ultimo cerramos la conexion 
#     Conexion.liberar_conexion(obtener_conexion)
#     print(f"Se ha liberado el objeto obtener_conexion")