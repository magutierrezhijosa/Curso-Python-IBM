# Importamos el paquete de flask y la clase de Flask
from flask import Flask, render_template
# Importamos la clase ClienteDAO 
from cliente_dao import ClienteDAO

# Definimos la variable de app y lo asociamos al objeto Flask
app = Flask(__name__)

# Vamos a agregar una variable que va a ser el titulo de nuestra aplicaion
titulo_app = "Zona Fit (GYM)"

# Creamos el decorador
@app.route("/") # url: http://localhost:5000/
# Creo otro decorador para que atienda la peticion de index.html y responda con un Hola mundo igual que "/"
@app.route("/index.html")
def inicio():
    # Es recomendable usar el metodo de logger para enviar informacion a la consola
    app.logger.debug("Entramos al path de inicio /")

    # Recuperamos los clientes de la bd por medio de la clase ClienteDAO que tiene los metodos que necesitamos
    clientes_db = ClienteDAO.seleccionar()


    return render_template("index.html", titulo=titulo_app, clientes=clientes_db)


# Ejecutamos el programa principal 
if __name__ == "__main__":
    # Llamamos a nuestr metodo .run() lo que hace que se levante nuestro servidor de Flask
    # IMPORTANTE para que los cambios se reflejen de manera automatica vamos a iniciarlo en modo debug
    app.run(debug=True)
    
 