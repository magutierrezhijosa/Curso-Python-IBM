import os.path

# Creamos una clase que contenga la lista de contactos 
class GestionContactos:

    # Creo una variable global donde fuardo el nombre del archivo
    NOMBRE_ARCHIVO = "contactos.txt"

    # Definimos el metodo constructor que inicializa los valores de los atributos
    def __init__(self):

        # Atributo que vas a guardar la lista de contactos
        self.contactos= []

        # Comprobamos si existe el archivo donde guardamos la lista 
        # de contactos y en caso de que exista recoger los que ya estan
        if os.path.isfile(self.NOMBRE_ARCHIVO):
            pass
            #
            #
            # FALTA OBTENER LAS PELICULAS DEL TXT SI ES QUE LO HAY 
            #
            #
            #
        else:
            print("No existe contactos.txt todavia")

    