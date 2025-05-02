from producto_dao import ProductoDAO
from producto import Producto

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
                salir = self.ejecutar_opcion(opcion)

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

            # Creo un objeto de tipo producto con los datos que nos dio el USER
            nuevo_producto = Producto(nombre=nombre,cantidad=cantidad,precio=precio,categoria=categoria)

            # Llamamos a la funcion de ClienteDao insertar()
            registro = self.producto_dao.insertar(nuevo_producto)

            # Mostramos los resultados de la consulta
            print(f"Productos insertados: {registro}")

        # Opcion Mostrar todos los productos
        elif opcion == 2:

            # Llamamos a la funcion seleccionar de ProductoDao
            registros = self.producto_dao.seleccionar()

            print("Los Producto del inventario son : ")

            # Recorremos los registros para mostrar los valores de cada uno
            for registro in registros:

                # Mostramos en pantalla cada registro
                print(registro)

        # Opcion Buscar un producto segun el nombre
        elif opcion == 3:

            # Pedimos al usuario que nos introduzca el nombre del producto que desea buscar
            nombre_producto = input("Introduce el nombre del producto que deseas buscar : ")

            # Creamos un objeto con el nombre que nos dio el USER
            producto_buscado = Producto(nombre=nombre_producto)

            # Llamamos a la funcion buscar de productoDAO
            registro = self.producto_dao.buscar(producto_buscado)


            # Mostramos al User el producto que buscaba
            print(f"El producto que buscabas es : {registro}")


        # Opcion Actualizar un producto del inventario
        elif opcion == 4:

            # Vamos a preguntar al User por los datos del nuevo producto
            id = input("Introduce la id del producto:  ")
            nombre = input("Introduce el nombre del producto:  ")
            cantidad = input("Introduce la cantidad del  producto:  ")
            precio = input("Introduce el precio del producto:  ")
            categoria = input("Introduce la categoria del producto:  ")

            # Creamos un objeto de tipo Producto con los valores dados
            producto_actualizar = Producto(id=id,nombre=nombre,cantidad=cantidad,precio=precio,categoria=categoria)

            # Llamamos a lmetodo actualizar de productoDAO
            registro = self.producto_dao.actualizar(producto_actualizar)

            # Mostramos en pantalla el resultado
            print(f"El producto se actualizo correctamente : {registro}")



        elif opcion == 6:

            # Nos despedimos del User
            print("Hasta la proxima .....")
            # Cambiamos la variable salir para no volver a entrar en el bucle 
            return True
        
        else: 
            # Si no introduce una opcion valida
            print(f"No has introducido una opcion valida : {opcion}")

        input("\nPresiona Enter para continuar ....")
        return False

# Declaramos el programa principal
if __name__ == "__main__":

    app_inventario = AppInventario()

    app_inventario.menu_inventario()