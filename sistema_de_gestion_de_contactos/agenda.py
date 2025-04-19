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
        # Muesto los valores de la agenda si hay algo el el .txt
        self.gestion_contactos.listar_contactos()
        while not salir:
            try:
                # Desplegamos el menu para que el usuario interactue
                opcion = self.menu_agenda()

                # Falta ejecutar la opcion que nos envie el user

            except Exception as e:
                print(f"Ocurrio un erro: {e}")

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


    # Metodo que nos permite ejecutar una funcion dependiendo de que valor
    # nos envie el usuario 
    def ejecutar_opcion(self,opcion):

        # Opcion 1 : Agregar un contacto
        if opcion == 1:
            pass
        # Opcion 2 : Mostrar todos los contactos
        elif opcion == 2:
            pass
        # Opcion 3 : Buscar un contacto
        elif opcion == 3:
            pass
        # Opcion 4 : Eliminar un contacto
        elif opcion == 4:
            pass
        # En el caso de que no introduzca una opcion valida se le mostrara un
        # mensaje de error con la opcion que ha seleccionado
        else:
            print(f"Opcion no valida: {opcion}")

        # Hago una pausa para que el usuario vea la info 
        input("\nPresiona Enter para continuar ....1")
        return False

        

# Programa principal         
if __name__ == "__main__":
    agenda = Agenda()
    agenda.agenda_contactos()