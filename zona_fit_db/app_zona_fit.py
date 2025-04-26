from cliente_dao import ClienteDAO

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
            nombre = input("Introduce un nombre para el nuevo cliente: ")
            apellido = input("Introduce un apellido para el nuevo cliente: ")
            membresia = input("Introduce la membresia para el nuevo cliente: ")
            # Lo Guardamos en una tupla
            nuevo_cliente = (nombre, apellido, membresia)
            self.cliente_dao.insertar(nuevo_cliente)
        elif opcion == 3:
            pass
        elif opcion == 4:
            pass
        elif opcion == 5:
            print("Hasta la proxima!")
            return True
        else:
            print(f"Opcion no valida : {opcion}")

        input("\nPresiona Enter para continuar ....")
        return False
# Programa principal
if __name__ == "__main__":
    app_zona_fit = AppZonaFit()
    app_zona_fit.menu_zona_fit()
