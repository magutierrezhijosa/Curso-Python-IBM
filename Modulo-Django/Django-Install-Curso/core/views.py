from django.shortcuts import render, HttpResponse

# Creamos una variable de tipo cadena 
html_base = """
<h1>Mi web personal</h1>
<ul>
    <li><a href="/">Portada</a></li>
    <li><a href="/about-me/ ">Acerca de </a></li>
    <li><a href="/portfolio/">Portafolio</a></li>
    <li><a href="/contact/">Contacto</a></li>
</ul>

"""

# Create your views here.
# Creamos la vista para mostrar home
def home(request):
    # Devolvemos la respuesta de tipo HttpResponse
    return HttpResponse(html_base + "<h2>Portada</h2><p>Esto es la portada </p>")

#  Creamos una vista para mostrar el About
def about(request):
    return HttpResponse(html_base + "<h2>Acerca de </h2><p>Me llamo MichelAngelo y soy programador</p>")

# Creamos la vista para mostrar el Portfolio
def portfolio(request):

    return HttpResponse(html_base + "<h2>Portafolio</h2><p>Este es el Portfolio de Michelangelo</p>")

# Creamos la vista de Contacto
def contact (request):

    return HttpResponse(html_base + "<h2>Contacto</h2><p>Contacto de Michelangelo</p>")