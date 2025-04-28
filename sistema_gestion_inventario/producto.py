


class Producto:

    # Agregamos el constructor de la clase con los parametros por defecto a None para que pueda crear se sin el valor de algun atributo
    def __init__(self, id=None, nombre=None, cantidad=None, precio=None, categoria=None):
        # Declaramos los valores al inicializar
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio
        self.categoria = categoria

    # Declaramos el metodo __str__ para poder imprimir enb cualquier momento el estado de los valores de los atributos de nuestro objeto
    def __str__(self):
        
        return (f"Id: {self.id}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, "
                f"Precio: {self.precio}, Categoria: {self.categoria}")