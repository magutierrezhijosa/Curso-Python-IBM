from conexion import Conexion
from producto import Producto

# Creamos la clase ClienteDAO
class ProductoDAO:

    # Esta clase va a tener la funcionalidad para poder interactuar con objetos de tipo producto y realizar CRUD con los datos

    # Declaramos las constantes de clase par ahacer posteriormente consultas con ellas
    SELECCIONAR = "SELECT * FROM productos ORDER BY id"
    INSERTAR = "INSERT INTO productos(nombre, cantidad, precio, categoria) VALUES (%s, %s, %s)"
    ACTUALIZAR = "UPDATE productos SET nombre=%s, cantidad=%s, precio=%s, categoria=%s"
    ELIMINAR = "DELETE FROM productos WHERE id=%s"

    # Vamos a crear los metodos de clase para realizar las consultas a la base de datos

    @classmethod
    # Definimos el metodo para agregar nuevos productos a nuestra tabla productos
    def insertar(cls,producto):

        # Creamos la variable que va a guardar nuestra conexion
        conexion = None

        # Iniciamos un bloque Try Exception
        try:

            # Creamos un objeto de tipo Conexion
            conexion = Conexion.obtener_conexion()

            # Creamos un objeto de tipo cursor 
            cursor = conexion.cursor()

            # Recogemos los valores que nos envie el User
            valores = (producto.nombre, producto.cantidad, producto.precio, producto.categoria)

            # Ejecutamos la QUERY desde nuestro cursor
            cursor.execute(cls.INSERTAR, valores)

            # Guardamos los cambios en la base de datos con .commit()
            conexion.commit()

            # Podemos retornar de manera opcional cuantos valores se modificaron en la base de datos
            return cursor.rowcount

        except Exception as e:

            # Mostramos el error por pantalla
            print(f"Ocurrio un error al agregar un producto: {e}")

        finally:
            # Revisamos el objeto conexion para cerrarlo en el caso de que no sea None
            if conexion is not None:
                # Cerramos el cursor
                cursor.close()
                # Cerramos la conexion
                Conexion.liberar_conexion(conexion)
            
    @classmethod
    def seleccionar(cls):

        # Declaramos la variable para guardar el estado de la conexion
        conexion = None

        try:
            # Vamos a pedir una conexion a la clase Conexion
            conexion = Conexion.obtener_conexion()

            # Declaramos la variable de cursor
            cursor = conexion.cursor()

            # Ejecutamos la QUERY que tenemos almacenada en la CONSTANTE de clase
            # por medio del cursor que hemos creado anteriormente
            cursor.execute(cls.SELECCIONAR)

            # Guardamos todos los registros de la Query que hicimos al Producto
            registros = cursor.fetchall()

            # Mapeo de clase-tabla productos
            productos = []
            for registro in registros:

                # Guardamos cada registro en una variable producto
                producto = Producto(registro[0],registro[1],registro[2],registro[3],registro[4])
                
                # Agregaqmos nuestro objeto de tipo Producto
                productos.append(producto)

            # Por ultimo devolvemos la lista de Objetos de tipo Producto
            return productos

        except Exception as e:
            print(f"Ocurrio une error al seleccionar un producto: {e}")

        finally:
            # Revisamos el objeto conexion para cerrarlo en el caso de que no sea None
            if conexion is not None:
                # Cerramos el cursor
                cursor.close()
                Conexion.liberar_conexion(conexion)


    # Declaramos el metodo de la clase 

if __name__ == "__main__": 

    productos = ProductoDAO.seleccionar()
    print(f"Los clientes son : ")
    for producto in productos:
        print(producto)