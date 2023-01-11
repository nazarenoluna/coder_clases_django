from django.urls import path

from estudiantes.views import  listar_estudiantes,listar_profesores,listar_cursos


urlpatterns = [
    path('alumno/', listar_estudiantes, name="listar_alumnos"),
    path('profesores/', listar_profesores, name="listar_profesores"),
    path('cursos/', listar_cursos, name="listar_cursos"),
]