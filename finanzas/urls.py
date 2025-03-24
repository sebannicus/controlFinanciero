from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('agregar_transaccion/', views.agregar_transaccion, name='agregar_transaccion'),
    path('listar_transacciones/', views.listar_transacciones, name='listar_transacciones'),
]