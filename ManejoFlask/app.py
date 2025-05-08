# Importamos el paquete de flask y la clase de Flask
from flask import Flask, render_template
# Importamos la clase ClienteDAO 
from cliente_dao import ClienteDAO
# Importamos la clase Cliente 
from cliente import Cliente
from cliente_forma import ClienteForma

# Definimos la variable de app y lo asociamos al objeto Flask
app = Flask(__name__)

app.config["SECRET_KEY"] = "llave_secreta_123"

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

    # Creamos un objeto de cliente form vacio
    # Vamos a usar este objeto para guardar  los valores del formulario
    cliente = Cliente()

    # Ahora creo un objeto de ClienteForm
    cliente_forma = ClienteForma(obj=cliente)


    return render_template("index.html", titulo=titulo_app, clientes=clientes_db, forma=cliente_forma)


# Ejecutamos el programa principal 
if __name__ == "__main__":
    # Llamamos a nuestr metodo .run() lo que hace que se levante nuestro servidor de Flask
    # IMPORTANTE para que los cambios se reflejen de manera automatica vamos a iniciarlo en modo debug
    app.run(debug=True)
    
 