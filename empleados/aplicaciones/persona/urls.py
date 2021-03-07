from django.urls import path
from .views import *
from django.conf import  settings
from django.conf.urls.static import static
app_name  = "persona"

urlpatterns = [


    path('buscar-empleado/',ListarEmpleadosByKword.as_view()),
    path('listar-habilidades/',ListHabilidades.as_view()),
    path('success/',SuccessView.as_view(),name='correcto'),
    path('eliminar-empleado/<int:pk>/',EliminarEmpleado.as_view(),name='delete'),
    #####################URLS PRIMER PROYECTO############
    path('',InicioView.as_view(),name="home"),
    path('listar-empleados/',ListAllEmpleados.as_view(),name='list_empleados'),
    path('ver-empleado/<int:pk>/', EmpleadoDetail.as_view(),name='empleado_detail'),
    path('area-empleado/<str:area>/', ListByAreaEmpleado.as_view(),name='area_empleado'),
    path('administrar-empleado/', ListAdministrarEmpleado.as_view(),name='administrar_empleado'),
    path('update-empleado/<int:pk>/', UpdateEmpleado.as_view(), name='update'),
    path('create-empleados/', EmpleadoCreateView.as_view(),name='create'),

#############################URLS MULTIMEDIA #######################
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT) # LA puedo ver desde el servidor