from conexion import Conexion
from producto import Producto

# Creamos la clase ClienteDAO
class ProductoDAO:

    # Esta clase va a tener la funcionalidad para poder interactuar con objetos de tipo producto y realizar CRUD con los datos

    # Declaramos las constantes de clase par ahacer posteriormente consultas con ellas
    SELECCIONAR = "SELECT * FROM productos ORDER BY id"
    INSERTAR = "INSERT INTO productos(nombre, cantidad, precio, categoria) VALUES (%s, %s, %s, %s)"
    BUSCAR = "SELECT * FROM productos WHERE nombre=%s"
    ACTUALIZAR = "UPDATE productos SET nombre=%s, cantidad=%s, precio=%s, categoria=%s WHERE id=%s"
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
            print(f"Estos son lso valores que vamos a introducir: {valores}")
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

    @classmethod
    # Declaramos el metodo de clase buscar 
    # el cual permite al usuario buscar un producto por nombre
    def buscar(cls,producto):

        # Inicializamos la variable donde se guarda la conexion
        conexion = None

        try:

            # Creamos el Objeto de tipo Conexion
            conexion = Conexion.obtener_conexion()

            # Creamos el objeto de tipo cursor
            cursor = conexion.cursor()

            # Guardamos los valores en un tupla para enviar los en una QUERY
            #IMPORTANTE poner la coma al final para que sea una tupla
            valores = (producto.nombre,)

            print(f"Los valores para buscar son: {valores}")
            # Ejecutamos  la QUERY
            cursor.execute(cls.BUSCAR, valores)

            # Recogemos la respuesta de la QUERY
            registro = cursor.fetchall()

            print(f"Este es la respueste de la QUERY: {registro}")

            producto_buscado = Producto(registro[0][0], registro[0][1], registro[0][2], registro[0][3], registro[0][4])

            print(f"Este es el resultado de producto_buscado: {producto_buscado}")

            # Devolvemos la respuesta que nos envio la QUERY
            return producto_buscado

        except Exception as e:
            print(f"Ha ocurrido un error al buscar un producto: {e}")

        finally:

            # Comprobamos que la conexion no sea None
            if conexion is not None:

                # Cerramos el cursor
                cursor.close()
                # Cerramos la conexion
                Conexion.liberar_conexion(conexion)

    @classmethod
    # Declaramos el metodo de clase actualizar
    # Permite al usuario actualizar la informacion de un producto
    def actualizar(cls, producto):

        # Declaramos la variable de conexion 
        conexion = None

        try:

            # Creamos el objeto de tipo Conexion
            conexion = Conexion.obtener_conexion()

            # Creamos el objeto de tipo cursor
            cursor = conexion.cursor()

            # Recogemos los valores del objeto que envio como parametro
            valores = (producto.nombre, producto.cantidad,producto.precio, producto.categoria, producto.id)

            print(f"Estos son los valores que vamos a enviar en la QUERY: {valores}")
            # Ejecutamos la QUERY que tenemois guardada en la CONSTANTE
            cursor.execute(cls.ACTUALIZAR, valores)

            # Guardamos los valores que hemos actualizado
            conexion.commit()

            # Devolvemos los campos que hemos actualizado
            return cursor.rowcount


        except Exception as e:

            # Mostramos en pantalla el error 
            print(f"Ocurrio un erro al actualizar: {e}")

        finally:

            # Compruebo que la conexion no sea None
            if conexion is not None:

                # Cerramos el cursor
                cursor.close()
                # Cerramos la conexion
                Conexion.liberar_conexion(conexion)

    
    @classmethod
    # Definimos el metodo de clase eliminar para borrar un producto de la tabla
    def eliminar(cls, producto):

        # Definimos la variable de la conexion 
        conexion = None

        try:
            # Creamos el objeto de tipo Conexion
            conexion = Conexion.obtener_conexion()

            # Creamos el objeto de tipo curor 
            cursor = conexion.cursor()

            # Guardamos en una tupla los valores del objeto que se nos envio como parametro
            valores = (producto.id,)

            # Ejecutamos la QUERY que tenemos en la CONSTANTE
            cursor.execute(cls.ELIMINAR, valores)

            # Guardamos los cambios en la DB 
            conexion.commit()

            # Devolvemos los valores que se han modificado
            return cursor.rowcount
        
        except Exception as e:

            print(f"Ocurrio un error al eliminar: {e}")

        finally:

            # Si la conexion no es None la cerramos 
            if conexion is not None:
                # Cerramos el cursor
                cursor.close()
                # Cerramos la conexion
                Conexion.liberar_conexion(conexion)
    

if __name__ == "__main__": 

    
    # # Prueba para el metodo de clase insertar
    # # Creamos un objeto de tipo producto
    # producto_insertar = Producto(nombre="Monitor", cantidad=50, precio=200, categoria="Tech")
    # response = ProductoDAO.insertar(producto_insertar)
    # print(f"Productos insertados : {response}")

    # # Prueba de lmetodo buscar
    # valores = Producto(nombre="Bicicleta")
    # producto_buscado = ProductoDAO.buscar(valores)

    # print(f"Este es el producto que buscabas es: {producto_buscado} ")

    # # Prueba metodo Actualizar
    # valores = Producto(3, "Patin-electrico", 5, 400, "Tech")
    # registro = ProductoDAO.actualizar(valores)
    # print(f"Este es el registro de actualizar: {registro}")

    # Pruebas metodo eliminar
    producto_eliminar = Producto(id = 4)
    registro = ProductoDAO.eliminar(producto_eliminar)
    print(f"Se eliminaron : {registro} productos")
    

    productos = ProductoDAO.seleccionar()
    print(f"Los productos son : ")
    for producto in productos:
        print(producto)