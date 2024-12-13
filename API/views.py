from rest_framework import viewsets
from .serializer import *
from .models import *
from django.shortcuts import render
# Create your views here.

class SCotizacionViewSet(viewsets.ModelViewSet):
    queryset = SolicitudCotizacion.objects.all()
    serializer_class = SCotizacionSerializer

class Orden_De_Compra_ViewSet(viewsets.ModelViewSet):
    queryset = Orden_De_Compra.objects.all()
    serializer_class = Orden_De_Compra_Serializer

# Nueva función para renderizar un HTML
def renderizar_html(request):
    # Puedes pasar un contexto si es necesario
    context = {
        "mensaje": "Bienvenido a la página de ejemplo",
        "items": SolicitudCotizacion.objects.all(),  # Ejemplo de datos para mostrar
    }
    return render(request, 'inicio.html', context)