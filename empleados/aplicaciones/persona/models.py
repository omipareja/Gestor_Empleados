from django.db import models
from aplicaciones.departamento.models import Departamento
from ckeditor.fields import RichTextField
# Create your models here.

class Habilidades(models.Model):
    habilidades = models.CharField('Habilidad',max_length=50)


    class Meta:
        verbose_name = 'Habilidad'
        verbose_name_plural= 'Habilidades'

    def __str__(self):
        return self.habilidades


class Empleado(models.Model):
    JOB_CHOICES = (
        ('0','contador'),
        ('1','administrador'),
        ('2','economista')
    )
    first_name = models.CharField('Nombres',max_length=60)
    last_name = models.CharField('Apellidos',max_length=60)
    full_name = models.CharField('Nombre completo',max_length=120,blank=True)
    job = models.CharField('Trabajos',max_length=1,choices=JOB_CHOICES)
    departamento = models.ForeignKey(Departamento,on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='upload',blank=True,null=True)
    habilidades = models.ManyToManyField(Habilidades)
    #hoja_vida = RichTextField() #hace parte del plugin ckeditor
    def __str__(self):
        return self.first_name

    class Meta:
        verbose_name = 'Persona'
        verbose_name_plural= 'Personas'