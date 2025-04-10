import os.path

class ServicioSnacks:
    NOMBRE_ARCHIVO = "snacks.txt"

    def __init__(self):
        self.snacks = []    
        # Revisar si ya existe el archivo snacks
        # Si ya existe, obtenemos los snacks del archivo 
        if os.path.isfile(self.NOMBRE_ARCHIVO):
            self.snacks = self.obtener_snacks()
        # Sino, cargamos algunos snacks iniciales
        else:
            self.cargar_snack_iniciales()

    def cargar_snacks_iniciales(self):
        snacks_iniciales = [] 

    # def cargar_snacks_inicia:
    def obtener_snacks(self):
        pass
    