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
    
