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
#### Aqui vamos a definir  las vistas que vamos a usar ####
# Create your views here.
# Creamos la vista para mostrar home
def home(request):
    # Devolvemos la respuesta de tipo HttpResponse
    return render(request , "core/home.html")

#  Creamos una vista para mostrar el About
def about(request):
    return render(request , "core/about.html")

# Creamos la vista para mostrar el Portfolio
def portfolio(request):

    return render(request , "core/portfolio.html")

# Creamos la vista de Contacto
def contact (request):

    return render(request , "core/contact.html")
