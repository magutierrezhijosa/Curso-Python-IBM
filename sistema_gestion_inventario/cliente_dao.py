from conexion import Conexion

# Creamos la clase ClienteDAO
class ClienteDAO:

    # Esta clase va a tener la funcionalidad para poder interactuar con objetos de tipo producto y realizar CRUD con los datos

    # Declaramos las constantes de clase par ahacer posteriormente consultas con ellas
    SELECCIONAR = "SELECT * FROM producto ORDER BY id"
    INSERTAR = "INSERT INTO producto(nombre, cantidad, precio, categoria) VALUES (%s, %s, %s)"
    ACTUALIZAR = "UPDATE producto SET nombre=%s, cantidad=%s, precio=%s, categoria=%s"
    ELIMINAR = "DELETE FROM producto WHERE id=%s"

    # Vamos a crear los metodos de clase para realizar las consultas a la base de datos
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

            # Guardamos todos los registros de la Query que hicimos al Cliente
            registros = cursor.fetchall()

            # Mapeo de clase-tabla productos
            clientes = []
            

        except Exception as e:
            print(f"Ocurrio une error al seleccionar un producto: {e}")