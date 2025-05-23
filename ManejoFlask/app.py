# Importamos el paquete de flask y la clase de Flask
from flask import Flask, redirect, render_template, url_for
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

# Vamos a crear el Endpoint para poder GUARDAR los User
@app.route("/guardar" , methods=["POST"])
def guardar():

    # Creamos los objetos de cliente inicialmente objeto vacio
    cliente = Cliente()

    # Ahora creamos un objeto tipo ClienteForma
    cliente_forma = ClienteForma(obj=cliente)

    # Vamos a comprobar los datos del formulario cuando se ha pulsado submit
    # El cual valida los TIPOS DE VALORE , SI ES REQUERIDO etc
    if cliente_forma.validate_on_submit():
        #Lenamos el objeto Cliente con los valores del formulario
        # TAMBIE SE AGREGAR EL ID OCULTO
        cliente_forma.populate_obj(cliente)

        if not cliente.id:
            # Insertamos el nuevo Cliente en la bd
            ClienteDAO.insertar(cliente)
        else:
            # Actualizamos los valores del Cliente
            ClienteDAO.actualizar(cliente)
    
    # Vamos a redireccionar al EndPoint de /inicio para recargar los valores de los clientes de la DB
    return redirect(url_for("inicio"))

# Vamos a crear un nuevo EndPoint o Decorador el cual va a tener la funcion  para limpiar los valores que haya escritos dentro del formulario
@app.route("/limpiar")
def limpiar():
    return redirect(url_for("inicio"))

# Creo un Endpoint nuevo para poder editar los clientes de nuestra DB
@app.route("/editar/<int:id_cliente>")
def editar(id_cliente):
    
    # Esto regresara el objeto de la DB que tenga ese ID
    cliente = ClienteDAO.seleccionar_por_id(id_cliente)

    # Creo un Objeto de tipo ClienteForma
    cliente_forma = ClienteForma(obj=cliente) 

    # Recuperamos el listado de clientes para volver a mostrarlo
    clientes_db = ClienteDAO.seleccionar()

    #  Cargamos el index.html con toda la informacion del cliente seleccionado
    return render_template("index.html", titulo=titulo_app, clientes=clientes_db, forma=cliente_forma)

# Creo un ENdpoint nuevo para eliminar un Cliente de la DB
@app.route("/eliminar/<int:id_cliente>")
def eliminar(id_cliente):

    # Creo un objeto tipo Cliente con el id que se desea eliminar 
    cliente_eliminar = Cliente(id=id_cliente)

    # Llamamos a la clase ClienteDao para usar su metodo eliminar 
    ClienteDAO.eliminar(cliente_eliminar)

    return redirect(url_for("inicio")) 


# Ejecutamos el programa principal 
if __name__ == "__main__":
    # Llamamos a nuestr metodo .run() lo que hace que se levante nuestro servidor de Flask
    # IMPORTANTE para que los cambios se reflejen de manera automatica vamos a iniciarlo en modo debug
    app.run(debug=True)
    
 