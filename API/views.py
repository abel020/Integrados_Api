from rest_framework import viewsets
from .serializer import *
from .models import *
# Create your views here.

class SCotizacionViewSet(viewsets.ModelViewSet):
    queryset = SolicitudCotizacion.objects.all()
    serializer_class = SCotizacionSerializer

class Orden_De_Compra_ViewSet(viewsets.ModelViewSet):
    queryset = Orden_De_Compra.objects.all()
    serializer_class = Orden_De_Compra_Serializer