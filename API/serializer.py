from rest_framework import serializers
from .models import *

class SCotizacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SolicitudCotizacion
        fields = '__all__'

class Orden_De_Compra_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Orden_De_Compra
        fields = '__all__'