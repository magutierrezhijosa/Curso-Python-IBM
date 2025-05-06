# Importamos el paquete de flask y la clase de Flask
from flask import Flask

# Definimos la variable de app y lo asociamos al objeto Flask
app = Flask(__name__)

# Creamos el decorador
@app.route("/") # url: http://localhost:5000/
# Creo otro decorador para que atienda la peticion de index.html y responda con un Hola mundo igual que "/"
@app.route("/index.html")
def inicio():
    # Es recomendable usar el metodo de logger para enviar informacion a la consola
    app.logger.debug("Entramos al path de inicio /")
    return   "<p>Hola Mundo</p>"

# Ejecutamos el programa principal 
if __name__ == "__main__":
    # Llamamos a nuestr metodo .run() lo que hace que se levante nuestro servidor de Flask
    # IMPORTANTE para que los cambios se reflejen de manera automatica vamos a iniciarlo en modo debug
    app.run(debug=True)
    
 