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

                # En primer lugar vamos a llamar a mostrar menu para que el User nos envie la opcion que desea realizar
                opcion = self.mostrar_menu()

                # Despues de recoger la opcion deseada vamos a ejecutar dicha opcion 


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
        
        # Recogemos el valor de la opcion que nos instropduzca el User
        opcion = input("Introduce una opcion del menu: ")

        # Comprobamos si la opcion que introdujo el User es un digito
        if opcion.isdigit():
            # Si es un digito lo devolvemos como un entero
            return int(opcion)
        else:
            # Sino es un digito le mandamos un error al usuario 
            print(f"La opcion que has introducido no es un nuemero: {opcion}")
        
    # Declaramos un metodo para ejecutar la opcion que ha introducido el User
    def ejecutar_opcion(self, opcion):

        # Dependiendo de la opcion que se envie se ejecutaran unas funciones

        # Opcion de AGREGAR un producto
        if opcion == 1:
            
            # Vamos a preguntar al User por los datos del nuevo producto
            nombre = input("Introduce el nombre del nuevo producto:  ")
            cantidad = input("Introduce la cantidad del nuevo producto:  ")
            precio = input("Introduce el precio del nuevo producto:  ")
            categoria = input("Introduce la categoria del nuevo producto:  ")

            

# Declaramos el programa principal
if __name__ == "__main__":

    pass