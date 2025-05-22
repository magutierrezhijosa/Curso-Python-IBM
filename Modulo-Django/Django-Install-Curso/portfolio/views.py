from django.shortcuts import render

# Create your views here.
# Creamos la vista para mostrar el Portfolio
def portfolio(request):

    return render(request , "portfolio/portfolio.html")