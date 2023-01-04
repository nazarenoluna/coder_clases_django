from django.urls import path

from estudiantes.views import saludo


urlpatterns = [
    path('saludar/', saludo),
    path('saludar2/', saludo),
    path('saludar3/', saludo),
]