# Crear un archivo con Python
nombre_archivo = "mi_archivo.txt"

#Abrir el archivo en modo escritura ("w")
with open(nombre_archivo, "w") as archivo:
    archivo.write("Hola como estas\n")
    archivo.write("estoy agregando informacion al archivo\n")

# archivo = open(nombre_archivo, "w")
# archivo.write("Hola como estas")
# archivo.write("\nestoy agregando informacion al archivo")
# archivo.close()

print(f"Se creo el archivo correctamente {nombre_archivo}")


# Otra forma de abrir el archivo 