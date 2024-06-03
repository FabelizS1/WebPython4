from django.contrib import admin
from .models import Project    #Con el punto delante de .models sabremos que estamos en la carpeta


class ProjectAdmin(admin.ModelAdmin):  
    readonly_fields = ('created', 'updated') #tupla con informacion para agregar las fechas en el administrador 

# Register your models here.
admin.site.register(Project, ProjectAdmin)