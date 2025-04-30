

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