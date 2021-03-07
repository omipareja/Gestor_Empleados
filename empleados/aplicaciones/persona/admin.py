from django.contrib import admin

# Register your models here.
from .models import *


admin.site.register(Habilidades)

class EmpleadoAdmin(admin.ModelAdmin): #Se Crea una tabla en el admin y se modifica
    list_display = (
        'pk',
        'first_name',
        'last_name',
        'departamento',
        'job',
        'full_name',
        #'habilidades',
    )
    #
    def full_name(self,obj):
        return obj.first_name + ' ' + obj.last_name
    #

    search_fields = ('first_name',)# se crea un buscador por trabajo
    list_filter = ('job',)  # se crea un filtro
    filter_horizontal = ('habilidades',)# este campo solo funciona con relaciones MANYTOMANY
admin.site.register(Empleado,EmpleadoAdmin)