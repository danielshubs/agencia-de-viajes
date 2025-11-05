from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('destinos/', views.destinos, name='destinos'),
    path('destinos/<str:nombre_destino>', views.destinos, name='destino'),
    path('reservar/', views.reservar, name='reservar'),
    path('reservar/<str:nombre_destino>', views.reservar, name='reservar'),
]
