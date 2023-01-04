from django.shortcuts import render
from django.http import HttpResponse
 
from datetime import datetime


def saludo(request):
    return HttpResponse(f'hola comision 47635. hora:{datetime.now()}')

 


