from cliente_dao import ClienteDAO
from cliente import Cliente

# Definimos la clase 
class AppZonaFit:

    # Declaramos el metodo constructor
    def __init__(self):
        self.cliente_dao = ClienteDAO()

    # Declaro la funcion que gestiona el menu 
    def menu_zona_fit(self):

        # Declaramos la variable qque nos va a indicar cuando salir
        salir = False
        # Hacemos un print de bienvenida
        print("****** Bienvenido a la App de Zona Fit ******")

        # Bucle que se repite hasta que el usuario quiera salir del menu
        while not salir:

            try:
                # Mostramos al usuario el menu para que elija la opcion
                opcion = self.mostrar_menu()
                # Ejecutamos la opcion que el usuario eligio
                salir = self.ejecutar_opcion(opcion)

            except Exception as e:

                # En el caso que ocurra un erro lo mostramos por pantalla
                print(f"Ha ocurrido un error: {e}")
    
    # Funcion que imprime el menu y recoge la opcion 
    def mostrar_menu(self):

        # Mostramos en pantalla un print con las opciones 
        print(f""" ------ MENU DE ZONA FIT ------
              1. Listar clientes
              2. Agregar cliente 
              3. Actualizar cliente
              4. Elminar cliente
              5. Salir
              """)
        
        opcion = input("Elige una opcion: ")

        # Comprobamos el valor de la opcion que introdujo sea un numero
        if opcion.isdigit():
            return int(opcion)
        else:
            print("Por favor, introduce un numero ")
    
    # Funcion que recoge la opcion que introduce el usuario y ejecuta el metodo para llevar a cabo esa funcion 
    def ejecutar_opcion(self, opcion):
        if opcion == 1:
            clientes = self.cliente_dao.seleccionar()
            print(f"Los clientes son : ")
            for cliente in clientes:
                print(cliente)
            
        elif opcion == 2:
            # Pedimos al usuario los valores para poder insertar un nuevo cliente
            nombre1 = input("Introduce un nombre para el nuevo cliente: ")
            apellido1 = input("Introduce un apellido para el nuevo cliente: ")
            membresia1 = input("Introduce la membresia para el nuevo cliente: ")
            # Lo Guardamos en una tupla
            nuevo_cliente = Cliente(nombre = nombre1, apellido = apellido1, membresia = membresia1)
            clientes_insertados = self.cliente_dao.insertar(nuevo_cliente)
            print(f"Clientes insertados : {clientes_insertados}")
        elif opcion == 3:
             # Pedimos al usuario los valores para poder actualizar un cliente
            id = input("Introduce el id para editar cliente : ")
            nombre = input("Introduce un nombre para editar cliente : ")
            apellido = input("Introduce un apellido para editar cliente : ")
            membresia = input("Introduce la membresia para editar cliente : ")
            # Declaro la variable donde guardo los valores del cliente 
            cliente_actualizar = Cliente(id, nombre, apellido, membresia)
            # Guardamos los resultados en otra variable
            clientes_actualizados = self.cliente_dao.actualizar(cliente_actualizar)
            # Mostramos en pantalla los rescultados obtenidos de la consulta
            print(f"Clientes actualizados : {clientes_actualizados}")
        elif opcion == 4:
            # Pedimos al usuario la id del cliente que desea eliminar 
            id = input("Introduce el id para eliminar cliente: ")

            # Creamos un objeto tipo cliente con el id que nos envio el user
            cliente_eliminar = Cliente(id = id)
            # Llamamos al metodo que nos elminia clientes dentro de cliente_dao
            clientes_eliminados = self.cliente_dao.eliminar(cliente_eliminar)
            # Mostramos un mensaje de confirmaciuon al user
            print(f"Se eliminaron los clientes: {clientes_eliminados}")

        elif opcion == 5:
            # Nos despedimos del usuario al salir de la aplicacion
            print("Hasta la proxima !")
            return True
        else:
            print(f"Opcion no valida : {opcion}")

        input("\nPresiona Enter para continuar ....")
        return False
# Programa principal
if __name__ == "__main__":
    app_zona_fit = AppZonaFit()
    app_zona_fit.menu_zona_fit()
