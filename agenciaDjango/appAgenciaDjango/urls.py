from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_rend, name='login'),
    path('login/enter/', views.login_enter, name='login_enter'),
    path('destinos/', views.destinos, name='destinos'),
    path('destinos/<int:destinoID>', views.detalle_destino, name='destino'),
    path('reservar/<str:viaje_id>', views.formulario_reserva, name='ver_reserva'),
    path('viajes/', views.viajes_general, name='viajes_general'),
    path('viajes/<str:destino_nombre>', views.viajes, name='viajes'),
    path('confirmar_reserva/<str:viaje_id>',views.confirmar_reserva,name = 'confirmar_reserva'),
    path('mis_reservas/', views.mis_reservas, name='mis_reservas'),
]