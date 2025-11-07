from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('viaje/<int:viaje_id>/', views.detalle_viaje, name='detalle_viaje'),
    path('destinos/', views.destinos, name='destinos'),
    path('destinos/<str:nombre_destino>', views.destinos, name='destino'),
    path('reservar/', views.reservar, name='reservar'),
    path('reservar/<str:nombre_destino>', views.reservar, name='reservar'),
]