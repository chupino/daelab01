from django.urls import path
from . import views

urlpatterns = [
    path('app/sumar/<int:valor1>/<int:valor2>/', views.mi_vista, name='mi_vista'),
]