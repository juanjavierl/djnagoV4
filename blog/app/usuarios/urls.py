from django.urls import path

from app.usuarios import views

urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('salir/', views.salir, name='salir'),
]