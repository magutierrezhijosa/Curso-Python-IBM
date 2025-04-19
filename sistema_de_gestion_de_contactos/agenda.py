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

    # Creo un Menu para mostrar las opciones que podemos hacer con nuestra agenda
    def menu_agenda():
        print(f"""--- MENU DE PELICULAS ---
              1. Agregar contacto  
              2. Mostrar contactos
              3. Buscar contacto
              4. Eliminar contacto
              5. Salir
               """)
        opcion = input("Elige una opcion: ")

        # Comprobamos que el valor introducido sea un numero
        # de lo contrario mandamos un mensaje de error 
        if opcion.isdigit():
            return int(opcion)
        else:
            print("Por favor, introduce un numero valido.")



    # Programa principal         
    if __name__ == "__main__":
        agenda = Agenda()