from django.db import models

# Create your models here.
# Esta clase va a representar una tabla 
class Proyect(models.Model):
    # Campos que vamos a usar  en nuestra tabla 
    title = models.CharField(max_length=200  ,  verbose_name="Titulo")
    description = models.TextField(verbose_name="Descripcion")
    image = models.ImageField(verbose_name="Imagen", upload_to="proyects")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edicion")
    link = models.URLField(verbose_name="Direccion Web" ,null=True, blank=True)

    class Meta:
        verbose_name = "proyecto"
        verbose_name_plural = "proyectos"
        ordering = ["-created"]

    def __str__(self):
        return self.title
    
