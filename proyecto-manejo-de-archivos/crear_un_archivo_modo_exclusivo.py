print("*** Abrir un archivo en modo exclusivo ***")

nombre_archivo = "mi_archivo.txt"

try:
    with open(nombre_archivo, "x") as archivo:
        archivo.write("Escritura en modo exclusivo\n")
        archivo.write("Espero te sea util")
    print(f"Se ha creado el archivo {nombre_archivo}")
except FileExistsError:
    print(f"El archivo {nombre_archivo} ya existe")