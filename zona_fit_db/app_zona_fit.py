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
            self.cliente_dao.seleccionar()
        elif opcion == 2:
            
            self.cliente_dao.insertar()
