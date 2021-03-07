from django.forms import *
from .models import *

class EmpleadoForm(ModelForm):
    class Meta:
        model = Empleado
        fields = (
            'first_name',
            'last_name',
            'job',
            'departamento',
            'avatar',
            'habilidades',

        )

        widgets = {
            'habilidades': CheckboxSelectMultiple()

        }