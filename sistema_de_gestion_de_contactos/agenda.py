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
        # self.gestion_contactos.listar_contactos()
        while not salir:
            try:
                # Desplegamos el menu para que el usuario interactue
                opcion = self.menu_agenda()

                # Falta ejecutar la opcion que nos envie el user
                salir = self.ejecutar_opcion(opcion)

            except Exception as e:
                print(f"Ocurrio un erro: {e}")

    # Creo un Menu para mostrar las opciones que podemos hacer con nuestra agenda
    def menu_agenda(self):
        print(f"""--- MENU DE LA AGENDA ---
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
            self.agregar_contacto()
        # Opcion 2 : Mostrar todos los contactos
        elif opcion == 2:
            self.gestion_contactos.listar_contactos()
        # Opcion 3 : Buscar un contacto
        elif opcion == 3:
            self.buscar()
        # Opcion 4 : Eliminar un contacto
        elif opcion == 4:
            self.eliminar()
        # Opcion 5 : Salir del menu
        elif opcion == 5:
            print("Nos vemos pronto !")
            return True
        # En el caso de que no introduzca una opcion valida se le mostrara un
        # mensaje de error con la opcion que ha seleccionado
        else:
            print(f"Opcion no valida: {opcion}")

        # Hago una pausa para que el usuario vea la info 
        input("\nPresiona Enter para continuar ....")
        return False

    # Metodo para agregar nuevos contactos a la agenda 
    def agregar_contacto(self):
        # Pido que me introduzca la informacion del contacto y la guardo
        nombre = input("Introduce el nombre del contacto: ")
        numero_telefono = input("Inroduce el telefono: ")
        correo = input("Introduce el correo: ")

        # Creamos un objeto tipo Contacto con los valores que introdujo el User
        nuevo_contacto = Contacto(nombre,numero_telefono,correo)

        # FALTA LLAMAR AL METODO PARA AGREGAR EL CONTACTO AL .TXT
        self.gestion_contactos.agregar_contacto(nuevo_contacto)

    # Metodo para BUSCAR un contacto en la agenda
    def buscar(self):
        # Pido un nombre de contacto para buscarlo en la agenda
        nombre_para_buscar = input("Introduce el nombre del contacto que quieres buscar: ")

        self.gestion_contactos.buscar_contacto(nombre_para_buscar)

    #  Metodo para ELIMINAR un contacto de la agenda
    def eliminar(self):
        # Pido un nombre para elminar dicho contacto
        nombre_para_eliminar = input("Introduce el nombre del contacto a eliminar: ")
        # Llamamos al metodo para que elimina el contacto de la agenda
        self.gestion_contactos.eliminar_contacto(nombre_para_eliminar)

# Programa principal         
if __name__ == "__main__":
    agenda = Agenda()
    agenda.agenda_contactos()

    