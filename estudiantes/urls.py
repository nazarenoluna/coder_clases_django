from django.urls import path

from estudiantes.views import saludo, listar_estudiantes, listar_profesores


urlpatterns = [
    path('lista/', listar_estudiantes),
    path('lista-profesores/', listar_profesores),
    path('saludar2/', saludo),    
]