from django.urls import path
from .views import *

app_name = "departamento"

urlpatterns = [

   ##############################33 #Inicio Proyectoooo#################33
    path('list_departamento/',DepartamentoListView.as_view(),name="list_departamento"),
    path('new_departamento/', NewDepartamento.as_view(), name="new_departamento"),

]