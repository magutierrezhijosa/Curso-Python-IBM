# Declaro la clase Cliente
class Cliente:

    # Agregamos el constructor de la clase
    def __init__(self, id=None, nombre=None, apellido=None, membresia=None):
        # Declaramos los valores al inicializar
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.membresia = membresia

    # Agregamos el metodo __str__ para poder imprimir en cualquier momento el estado de los valores de los atributos de nuestro objeto
    def __str__(self):
        return (f"Id: {self.id}, Nombre: {self.nombre}, "
                f"Apellido: {self.apellido}, Membresia: {self.membresia}")