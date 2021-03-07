from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.edit import FormView
from django.views.generic import ListView, DetailView, CreateView, TemplateView, UpdateView, DeleteView
from .forms import *
from aplicaciones.persona.models import *
from .models import *
# Create your views here.
class NewDepartamento(FormView): #Esta vista no trabja directamente con modelos
    template_name = "departamento.html"
    form_class = NewDepartamento
    success_url = reverse_lazy('departamento:list_departamento')

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


    def form_valid(self, form):
        nombre = form.cleaned_data['nombre']
        apellido = form.cleaned_data['apellidos']
        depa = Departamento.objects.create(
            name= form.cleaned_data['departamento'],
            short_name= form.cleaned_data['shorname']
        )
        Empleado.objects.create( #crar registro
            first_name= nombre,
            last_name= apellido,
            job = '1',
            departamento= depa
        )
        return  super(NewDepartamento, self).form_valid(form)

class DepartamentoListView(ListView):
    template_name = 'departamento_list.html'
    model = Departamento
    context_object_name = 'consulta'
    paginate_by = 2  # para la paginacion de los resultados el crea un objeto de paginacion
    ordering = 'id'
   # def get_queryset(self):
   #     palabra = self.request.GET.get("kword", '')  # obtengo parametro por metodo GET
   #     list = Departamento.objects.filter(name__icontains=palabra)
   #     return list

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Lista Departamentos'
        context['place_holder'] = 'Buscar Departamento'
        return context


