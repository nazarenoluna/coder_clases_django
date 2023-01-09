from django.urls import path

from estudiantes.views import saludar, listar_estudiantes,listar_profesores


urlpatterns = [
    path('saludar/', saludar),
    path('lista-alumnos/', listar_estudiantes, name="lista_estudiantes"),
    path('saludar3/', listar_profesores, name="lista_profesores"),
]