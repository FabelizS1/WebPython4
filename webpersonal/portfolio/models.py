from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200, verbose_name="Titulo") #se agrega siempre que es un campo de texto max_length
    description = models.TextField(verbose_name="Descripcion")
    image = models.ImageField(verbose_name="Imagen", upload_to="projects") #guardar todo en un directorio upload_to que se creara en media
    link = models.URLField(verbose_name="Direccion Web", null=True, blank=True) #Campo para agregar enlaces
    created = models.DateTimeField(auto_now_add = True, verbose_name="Fecha de Creacion") #fecha de creacion, auto_now_addv = True se ejecuta cada vez que se inserta un registro
    updated = models.DateTimeField(auto_now = True, verbose_name="Fecha de Edicion") #fecha de modificion, auto_now = Truen se ejecuta cada vez que se actualiza un registro


    class Meta:
        verbose_name = "proyecto"
        verbose_name_plural = "proyectos"
        ordering = ["-created"] #Colocar - antes de created para que se ordene el campo created al reverso
    
    def __str__(self): #Se agrega esto para que no muestre el nombre de Object sino que diga el nombre del Proyecto
        return self.title