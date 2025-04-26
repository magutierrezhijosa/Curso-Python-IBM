
# Creamos la clase ClienteDAO 
from conexion import Conexion
from cliente import Cliente


class ClienteDAO:
    # Esta clase va tener la funcionalidad para poder interactuar con objeto
    # de tipo cliente y realizar CRUD con los datos
    SELECCIONAR = "SELECT * FROM cliente ORDER BY id"
    INSERTAR = "INSERT INTO cliente(nombre, apellido, membresia) VALUES(%s, %s, %s)"
    ACTUALIZAR = "UPDATE cliente SET nombre=%s, apellido=%s, membresia=%s WHERE id=%s"
    ELIMINAR = "DELETE FROM cliente WHERE id=%s"

    @classmethod
    # Trabajamos con metodos de clase 
    def seleccionar(cls):
        conexion = None

        try:
            # Vamos a pedir una conexion a la clase Conexion
            conexion = Conexion.obtener_conexion()
            # Declaramos la variable de cursor
            cursor = conexion.cursor()
            # Ejecutamos la QUERY que tenemos almacenada el la CONSTANTE de clase 
            # por medio del cursor que hemos creado anteriormente
            cursor.execute(cls.SELECCIONAR)
            # Guardamos todos los registros de la QUERY que hicimos al Cliente
            registros = cursor.fetchall()
            # Mapeo de clase-tabla cliente
            clientes =[]
            for registro in registros:
                # Guardamos cada registro en una variable cliente
                cliente = Cliente(registro[0], registro[1], registro[2], registro[3])

                # Agregamos nuestro Objeto de tipo Cliente a nuesta lista de clientes[]
                clientes.append(cliente)
            # Por ultimo devolvemos la list ade Objetos de tipo Cliente
            return clientes

        except Exception as e:
            print(f"Ocurrio un error al seleecionar clientes: {e}")
        # 
        finally:
            # Revisamos el objeto conexion para cerrarlo en el caso de que no sea None
            if conexion is not None:
                # Cerramos el cursor
                cursor.close()
                Conexion.liberar_conexion(conexion)

    # Creamos otro metodo de clase 
    @classmethod
    def  insertar(cls, cliente):
        # Definimos la variable de conexion
        conexion = None

        try:
            # Creamos nuestra conexion llamando a la clase COnexion
            conexion = Conexion.obtener_conexion()
            # Creamos nuestro objeto cursor  usando la variable conexion
            cursor = conexion.cursor()
            # Agregamos los valores de los parametros segun declaramos en la constante INSERTAR
            valores =  (cliente.nombre, cliente.apellido, cliente.membresia)
            print(valores)
            # Usando el cursor llamamos al metodo execute para ejecutar la consulta de tipo insert usadon la consstante INSERT
            cursor.execute(cls.INSERTAR, valores)
            # Guardamos los cambios en la base de datos con .commit()
            conexion.commit()
            # Podemos retornar de manera opciona cuantos valores se modificaron en la base de datos
            return cursor.rowcount

        except Exception as e:
            print(f"Ocurrio un error al insertar: {e}")
        finally:
            # Revisamos el objeto conexion para cerrarlo en el caso de que no sea None
            if conexion is not None:
                # Cerramos el cursor
                cursor.close()
                Conexion.liberar_conexion(conexion)

    @classmethod
    def actualizar(cls,cliente):
        # Definimos la variable de conexion 
        conexion = None
        try:
            # Creamos un objeto de tipo conexion
            conexion = Conexion.obtener_conexion()
            # Definimos la variable de cursor y a traves de la conexion creamos un objeto de tipo cursor
            cursor = conexion.cursor()
            # recogemos los valores que vamos a introducir como parametros mas adelante
            valores = (cliente.nombre, cliente.apellido, 
                       cliente.membresia, cliente.id)
            # mediante el cursor ejecutamos la QUERY de actualizar nuestra tabla junto con los valores que hemos guardado
            cursor.execute(cls.ACTUALIZAR, valores)
            # Finalmente guardamos los cambios con un commit
            # conexion.commit()
            # Devolvemos cuantos registros se modificaron 
            return cursor.rowcount
        except Exception as e:
            print(f"Ocurrio un error al actualizar un cliente: {e}")
        finally:
            # Revisamos el objeto conexion para cerrarlo en el caso de que no sea None
            if conexion is not None:
                # Cerramos el cursor
                cursor.close()
                Conexion.liberar_conexion(conexion)


# Vamos a realizar una prueba para comprobar que recibimos los objetos y ademas 
# se esten conviertiendo a objetos de tipo cliente 
if __name__ == "__main__":
    # Insertar cliente
    # Utilizamos el constructor de la clase cliente sin el id para que sea insertar ya que si le indicamos un id la consulta seria de update
    cliente1 = Cliente(nombre="Alejandra", apellido="Tellez", membresia=300)
    # Llamamos al metodo de la clase ClienteDAO para insertar
    clientes_insertados = ClienteDAO.insertar(cliente1)
    # Mostramos en pantalla los clientes que hemos insertado
    print(f"Clientes insertados: {clientes_insertados}")
    
    
    
    
    # Seleccionas lo cliente
    clientes = ClienteDAO.seleccionar()
    for cliente in clientes:
        print(cliente)