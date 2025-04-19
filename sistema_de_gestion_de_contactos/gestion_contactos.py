import os.path
from contacto import Contacto

# Creamos una clase que contenga la lista de contactos 
class GestionContactos:

    # Creo una variable global donde fuardo el nombre del archivo
    NOMBRE_ARCHIVO = "contactos.txt"

    # Definimos el metodo constructor que inicializa los valores de los atributos
    def __init__(self):

        # Atributo que vas a guardar la lista de contactos
        self.contactos= []

        # Comprobamos si existe el archivo donde guardamos la lista 
        # de contactos y en caso de que exista recoger los que ya estan
        if os.path.isfile(self.NOMBRE_ARCHIVO):
            
            # Busco los contactos que haya en el archivo txt
            self.contactos = self.obtener_contactos()

        else:
            # En el caso de que no exista muestro un error 
            print("No existe contactos.txt todavia")

    
    # Metodo que va a recoger la informacion del "contactos.txt"
    def obtener_contactos(self):

        # Creo una lista para recoger los contactos del archivo
        contactos = []

        try:
            # Abrimos el archivo en modo lectura "r" para recorrerlo y sacar los 
            # contactos del archivo txt 
            with open(self.NOMBRE_ARCHIVO, "r", encoding="utf8") as archivo:
                # Recorremos cada linea del archivo
                for linea in archivo:

                    # Recojo los valores en cada variable
                    nombre, numero_telefono, correo = linea.strip().split(",")
                    # Creo un objeto de tipo Contacto por cada linea
                    contacto = Contacto(nombre,numero_telefono,correo)
                    # Voy agregando los contactos a la lista que he creado
                    contactos.append(contacto)
        except Exception as e:
            print(f"Error al leer el archivo {e}")
        
        # Devolvemos los contactos
        return contactos
    
    # Metodo para listar los contactos 
    def listar_contactos(self):

        # Agregamos una validacion para que no intente imprimir si la lista 
        # esta vacia
        if not self.contactos:
            print("No se puede listar por que no hay contactos")
            return
        
        print("--- Contactos en la agenda ---")
        for contacto in self.contactos:
            print(contacto)

    # Metodo que guarda los conctos en el archivo .txt
    def guardar_contacto_archivo(self,contactos):

        try:
            # Vamos a abrir el archivo en modo escritura para 
            # agregar el nuevo contacto
            with open(self.NOMBRE_ARCHIVO, "a" , encoding="utf8") as archivo:
                # Recorremos contactos 
                for contacto in contactos:
                    # Agregamos el nuevo contacto a nuestro archivo .txt
                    archivo.write(f"{contacto.escribir_contacto()}\n")

        except Exception as e:
            print(f"No se pudo guardar el contacto en el archivo:{e}")

    # Metodo para agregar el contacto a la lista y posteriormente al .txt
    def agregar_contacto(self,contacto):

        # Primero agrego el contacto a la lista
        self.contactos.append(contacto)
        # Guardamos el contacto en el .txt 
        self.guardar_contacto_archivo([contacto])

    def buscar_contacto(self,name):

        try:
            # Abrimos el archivo con permisos de lectura para buscar el contacto
            with open(self.NOMBRE_ARCHIVO, "r", encoding="utf8") as archivo:

                # Declaro un contador par acomprobar si esta el nombre
                find = False
                # Recorremos linea a linea para buscar el nombre que nos dio el User
                for linea in archivo:
                     # Recojo los valores en cada variable
                    nombre, numero_telefono, correo = linea.strip().split(",")
                    # Si el nombre es igual al name que nos dio el User
                    if nombre == name:
                        # Le muestro el contacto 
                        print(f"El contacto con el nombre: {name} con numero: {numero_telefono} y correo: {correo}")
                        find = True
                # Si no encuentra ningun contacto con ese nombre le pasamos un mensaje de info
                if find == False:
                    print(f"No se encontro ningun contacto con el nombre: {name}")


        except Exception as e:
            print(f"ERROR: {e}")
