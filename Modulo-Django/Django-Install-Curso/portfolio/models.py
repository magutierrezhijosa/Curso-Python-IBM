from django.db import models

# Create your models here.
# Esta clase va a representar una tabla 
class Proyect(models.Model):
    # Campos que vamos a usar  en nuestra tabla 
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)