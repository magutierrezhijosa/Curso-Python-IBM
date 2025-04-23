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
        # Ci la variable clase pool es None 
        if cls.pool is None: # Se crea el objeto pool
            try:
                cls.pool = pooling.MySQLConnectionPool(
                    # Agregamos valores a cada una de las constantes que hemos ido definiendo
                    pool_name = cls.POOL_NAME,
                    pool_size = cls.POOL_SIZE,
                    host = cls.HOST,
                    port = cls.DB_PORT,
                    database = cls.DATABASE,
                    user = cls.USERNAME,
                    password = cls.PASSWORD


                )
                return cls.pool
            except Error as e:
                print(f"Ocurrio un error al obtener pool: {e}")

        # En el caso de que no sea None retornamos el objeto de tipo pool
        else:
            return cls.pool
        
    @classmethod
    # Metodo para crear nuevos objetos de tipo conexion 
    def obtener_conexion(cls):
        return cls.obtener_pool().get_connection()
    
    @classmethod
    # Metodo para cerrar la conexion una vez haya sido utilizada
    def liberar_conexion(cls, conexion):
        conexion.close()

# Prueba par comprobar que todo funciona correctamente y esta bien importado
if __name__ == "__main__":

    # Creamos un objeto pool
    pool = Conexion.obtener_pool()
    print(pool)
    # Creamos un objeto de tipo conexion 
    conexion1 = pool.get_connection()
    print(conexion1)
    # Por ultimo cerramos la conexion 
    Conexion.liberar_conexion(conexion1)
    print(f"Se ha liberado el objeto conexion1")