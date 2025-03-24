from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
    path('agregar_transaccion/', views.agregar_transaccion, name='agregar_transaccion'),
    path('listar_transacciones/', views.listar_transacciones, name='listar_transacciones'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='index'), name='logout'),
    path('register/', views.register, name='register'),
]