from producto_dao import ProductoDAO

class AppInventario:

    # Declaramos el metodo constructor
    def __init__(self):
        self.producto_dao = ProductoDAO()

    # Creamos un metodo para gestionar el menu y las opciones que nos vaya enviando el User segun vaya respondiendo a los inputs 
    def menu_inventario(self):

        # Inicializamos la variable que va a controlar el salir de nuestra aplicacion
        salir = False

        # Mostramos un mensaje de bienvenida al User
        print("**** Bienvenido a la App de Inventario ****")

        # Realizamos un bucle para volver a mandar  el menu de nuestra App siempre y cuando el usuario no decida salir de esta 
        while not salir:

            try:

                pass

            except Exception as e:

                # Mostramos el error al Usuario
                print(f"Ocurrio un error con el menu de App Inventario: {e}")


    # Declaramos el metodo para mostrar el menu al ususario
    def mostrar_menu(self):

        # Mostramos en pantalla las opciones de nuestro menu
        print(""" 
                Lista de opciones del Menu:
                    1. Agregar un producto
                    2. Mostrar todos los productos
                    3. Buscar un producto
                    4. Actualizar un producto
                    5. Eliminar un producto
                    6. Salir
            """)
        
    # Declaramos un metodo para ejecutar la opcion que ha introducido el User
    