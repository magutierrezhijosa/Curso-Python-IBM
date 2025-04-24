
# Creamos la clase ClienteDAO 
from zona_fit_db.conexion import Conexion
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
            # Vamos a pedir una conexion a la clase COnexion
            conexion = Conexion.obtener_conexion()
            # Declaramos la variable de cursor
            cursor = conexion.cursor()

        except Exception as e:
            print(f"Ocurrio un error al seleecionar clientes: {e}")
        # 
        finally:
            # Revisamos el objeto conexion para cerrarlo en el caso de que no sea None
            if conexion is not None:
                # Cerramos el cursor
                cursor.close()
                Conexion.liberar_conexion(conexion)
