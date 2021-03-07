from django.urls import path
from .views import *

app_name= 'prueba'

urlpatterns = [
    path('prueba/',IndexView.as_view(),name="correcto"),
    path('Lista/',PruebaListView.as_view()),
    path('prueba-create/',PruebaCreateView.as_view()),
    path('foundation-list/',Foundation.as_view()),

]