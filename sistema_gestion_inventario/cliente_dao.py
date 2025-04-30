

# Creamos la clase ClienteDAO
class ClienteDAO:

    # Esta clase va a tener la funcionalidad para poder interactuar con objetos de tipo producto y realizar CRUD con los datos
    # Declaramos las constantes de clase par ahacer posteriormente consultas con ellas
    SELECCIONAR = "SELECT * FROM producto ORDER BY id"