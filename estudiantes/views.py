from django.shortcuts import render
from django.http import HttpResponse
 
from datetime import datetime

from estudiantes.models import Estudiante

def saludo(request):
    return HttpResponse(f'hola comision 47635. hora:{datetime.now()}')

def listar_estudiantes(request):
    contexto = {
        'estudiantes': Estudiante.objects.all()
    }
    return render(
        request=request,
        template_name='estudiantes/lista_estudiantes.html',
        context=contexto
    )


def listar_profesores(request):
    return render(request=request, template_name='estudiantes/lista_profesores.html')


