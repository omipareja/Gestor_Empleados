from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView,ListView,CreateView

from aplicaciones.home.models import Prueba
from .forms import PruebaForm

class IndexView(TemplateView):
    template_name = 'success.html'

class PruebaListView(ListView):
    template_name = 'list.html'
    model = Prueba
    context_object_name = 'Lista'

class PruebaCreateView(CreateView):
    template_name = "add.html"
    model = Prueba
    form_class = PruebaForm
    success_url = reverse_lazy('prueba:correcto')

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

class Foundation(TemplateView):
    template_name = "foundation.html"