from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('index/', views.index, name='index'),
    path('detalles_viaje/<int:viaje_id>/', views.detalle_viaje, name='detalle_viaje'),
    path('destinos/', views.destinos, name='destinos'),
    path('destinos/<int:destinoID>', views.detalle_destino, name='destino'),
    path('reservar/', views.reservar, name='reservar'),
    path('reservar/<str:nombre_destino>', views.reservar, name='reservar'),
    path('login/', views.login_enter, name='login_enter')
]