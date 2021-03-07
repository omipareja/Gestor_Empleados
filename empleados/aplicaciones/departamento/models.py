from django.db import models

# Create your models here.
class Departamento(models.Model):
    name = models.CharField('Nombre',max_length=50)#el nombre es como aparecera en el administrador de django
    short_name = models.CharField('Nombre Corto', max_length=50,blank=True)
    anulate = models.BooleanField('Anulado',default=False)

    class Meta:
        verbose_name= 'Mi departamento'
        verbose_name_plural = 'Mis departamentos'
        ordering = ['name']
        #unique_together = ('name','shor_name') #no permite que se registre un atributo dos veces

    def __str__(self):
        return self.name