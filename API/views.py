from django.http import HttpResponse
import requests
from rest_framework import viewsets

from API.forms import SolicitudCotizacionForm
from .serializer import *
from .models import *
from django.shortcuts import redirect, render
from django.http import JsonResponse
# Create your views here.

class SCotizacionViewSet(viewsets.ModelViewSet):
    queryset = SolicitudCotizacion.objects.all()
    serializer_class = SCotizacionSerializer

class Orden_De_Compra_ViewSet(viewsets.ModelViewSet):
    queryset = Orden_De_Compra.objects.all()
    serializer_class = Orden_De_Compra_Serializer

# Nueva función para renderizar un HTML

from datetime import datetime
from django.utils import timezone

def Scotizacion(request):
    if request.method == 'POST':
        form = SolicitudCotizacionForm(request.POST)
        if form.is_valid():
            form.save()  # Guarda la solicitud si es válida
            return redirect('solicitud_exito')  # Redirige a una página de éxito (cambia la URL según sea necesario)
        else:
            return JsonResponse({
                'status': 'error',
                'message': 'Hubo un error al enviar el formulario.'
            })
    else:
        form = SolicitudCotizacionForm()

    return render(request, 'Scotizacion.html', {'form': form})

def ObtenerCotizacion(request):
    cotizaciones = SolicitudCotizacion.objects.all()
    return render(request, 'Solicitud_exito.html', {'cotizaciones': cotizaciones})

def api_proxy(request):
    response = requests.get('https://contactomodulo-production.up.railway.app/api/clientes')
    print(response.json())  # Imprime la respuesta para verificar su formato
    return JsonResponse(response.json(), safe=False)
