
from flask_wtf import FlaskForm
from wtforms import HiddenField
from wtforms.fields.numeric import IntegerField
from wtforms.fields.simple import StringField, SubmitField
from wtforms.validators import DataRequired

# Creamos la clase y vamos a heredar de la clase FlaskForm
class ClienteForma(FlaskForm):

    # Vamos a definir el campo nombre de tipo cadena StringField lo cual va generar un campo para mostrar el input text tipo nombre

    id = HiddenField("id")
    # Por un lado va a generar el componenete de etiqueta y por otro lado va a generar el componente de input text
    nombre =  StringField("Nombre", validators=[DataRequired()])

    # Hacemos lo mismo para el campo apellido 
    apellido = StringField("Apellido", validators=[DataRequired()])

    # Igual para el campo de membresia pero en este caso cambiamos el tipo de dato qque vamos a recibir por un integer ya que el campo membresia es numerico
    membresia = IntegerField("Membresia" , validators=[DataRequired()])

    # Por ultimo vamos a generar el boton de SUBMIT
    guardar = SubmitField("Guardar")