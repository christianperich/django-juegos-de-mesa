from django.urls import path
from juegos import views

urlpatterns = [
    path('', views.juegos, name='home'),
    path('buscar', views.buscar, name='buscar'),
]
