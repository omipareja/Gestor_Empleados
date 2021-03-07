from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, DetailView, CreateView, TemplateView, UpdateView, DeleteView
# Create your views here.
from aplicaciones.persona.models import Empleado
from django.urls import reverse_lazy
from .forms import *


class ListarEmpleadosByKword(ListView):
    ''' Listar empleado por palabra clave'''
    template_name = 'clave.html'
    context_object_name = 'empleados'



    def get_queryset(self):
        palabra = self.request.GET.get("texto",'')#obtengo parametro por metodo GET
        list = Empleado.objects.filter(first_name__icontains=palabra)
        print('RESULTADO',list)
        return  []
#Relacion muchos a muchas
class ListHabilidades(ListView):
    template_name = 'habilidades.html'
    context_object_name = 'habilidades'

    def get_queryset(self):
        empleado = Empleado.objects.get(pk=6)#me recupera un unico rehistro
        return empleado.habilidades.all() #me trae todos las habilidades del empleado
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Lista Habilidades'
        return context

#DetailVIew

#CCreateView
class SuccessView(TemplateView):
    template_name = "success.html"

class PruebaCreate(CreateView):
    template_name = "create.html"
    model = Empleado
    fields = ['first_name','last_name','job','departamento','habilidades','hoja_vida']#trae todos los campos del modelo
    success_url = reverse_lazy('persona:correcto')

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form): #interceptamos el formulario que se esta enviando para hacer el campo fullname
        empleado = form.save(commit=False) #almacenetodo lo que se ha obtenido en la base de datos el commite es para no hacer doble guardado
        empleado.full_name = empleado.first_name + ' ' + empleado.last_name
        empleado.save() # me actualiza el atributo al objeto
        return super(PruebaCreate, self).form_valid(form)

## INICIO DEL PRIMER PROYECTO ##
class InicioView(TemplateView):
    template_name = "home.html"

class ListAllEmpleados(ListView):
    template_name = 'list_all.html'
    paginate_by = 6 #para la paginacion de los resultados el crea un objeto de paginacion
    context_object_name = 'consulta'
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


    def get_queryset(self):
        palabra = self.request.GET.get("kword",'')#obtengo parametro por metodo GET
        print('palabra :', palabra)
        list = Empleado.objects.filter(first_name__icontains=palabra)
        return  list

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Lista Empleados'
        context['place_holder'] = 'Buscar empleado'
        return context


    #traer empleados por departamento
    # queryset = Empleado.objects.filter(
    #     departamento__name= 'contabilidad'
    # )

    #sobrescribimos el query set
    # pasamos parametro por url
    #def get_queryset(self):
    #    area = self.kwargs['shortname'] #para recoger lo que me llega por url
    #    lista = Empleado.objects.filter(
    #        departamento__name__icontains =  area
    #    )
    #    return lista

class ListByAreaEmpleado(ListView):
    template_name = 'list_area.html'
    context_object_name = 'consulta'


    def get_queryset(self):
        area = self.kwargs['area']
        list = Empleado.objects.filter(departamento__name__contains=area)
        return list

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Lista Empleados Por Area'
        context['place_holder'] = 'Buscar empleado'
        return context

class ListAdministrarEmpleado(ListView):
    template_name = 'administrar.html'
    paginate_by = 6
    context_object_name = 'consulta'
    model = Empleado

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


    def get_queryset(self):
        palabra = self.request.GET.get("kword",'')#obtengo parametro por metodo GET
        print('palabra :', palabra)
        list = Empleado.objects.filter(first_name__icontains=palabra)
        return  list

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Lista Empleados'
        context['place_holder'] = 'Buscar empleado'
        return context

class UpdateEmpleado(UpdateView):
    template_name = "update.html"
    model = Empleado
    fields = ['first_name', 'last_name', 'job', 'departamento', 'habilidades']
    success_url = reverse_lazy('persona:administrar_empleado')
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object() #recuperamos el objeto

        return super().post(request, *args, **kwargs)

    def form_valid(self, form): #interceptamos el formulario que se esta enviando para hacer el campo fullname
        empleado = form.save(commit=False) #almacenetodo lo que se ha obtenido en la base de datos el commite es para no hacer doble guardado
        empleado.full_name = empleado.first_name + ' ' + empleado.last_name
        empleado.save() # me actualiza el atributo al objeto
        return super(UpdateEmpleado, self).form_valid(form)

class EliminarEmpleado(DeleteView):
    model = Empleado
    template_name = "delete.html"
    success_url = reverse_lazy('persona:administrar_empleado')

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

class EmpleadoCreateView(CreateView):
    template_name = "create.html"
    model = Empleado
    form_class = EmpleadoForm #trae todos los campos del modelo
    success_url = reverse_lazy('persona:list_empleados')

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form): #interceptamos el formulario que se esta enviando para hacer el campo fullname
        empleado = form.save(commit=False) #almacenetodo lo que se ha obtenido en la base de datos el commite es para no hacer doble guardado
        empleado.full_name = empleado.first_name + ' ' + empleado.last_name
        empleado.save() # me actualiza el atributo al objeto
        return super(EmpleadoCreateView, self).form_valid(form)


class EmpleadoDetail(DetailView):
    model = Empleado
    template_name = "detail_empleado.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'empleado del mes'
        return context



