from contacto import Contacto
from gestion_contactos import GestionContactos



class Agenda:

    # Declaramos el constructor de la clase 
    def __init__(self):
        # Inicializamos un objeto tipo GestionContactos
        self.gestion_contactos = GestionContactos()

    # Funcion que se va a ejecutar miestras no se salga del bucle while
    def agenda_contactos(self):
        # Declaro la variable par acontrolar el bucle while
        salir = False
        print("*** Bienvenido a la agenda ***")