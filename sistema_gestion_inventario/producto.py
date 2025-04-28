


class Producto:

    # Agregamos el constructor de la clase con los parametros por defecto a None para que pueda crear se sin el valor de algun atributo
    def __init__(self,nombre=None, cantidad=None, precio=None, categoria=None):
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio
        self.categoria = categoria