


class Contacto:

    def __init__(self,nombre,numero_telefono,correo):
        self.nombre = nombre
        self.numero_telefono = numero_telefono
        self.correo = correo

    def __str__(self):
        return(f"""Contacto ==> nombre: {self.nombre}, 
                                numero de telefono: {self.numero_telefono},
                                correo: {self.correo}
                """)
    
    def escribir_contacto(self):
        return f"{self.nombre},{self.numero_telefono},{self.correo}"