from django import forms
from .models import Orden_De_Compra, SolicitudCotizacion
from django.core.exceptions import ValidationError
from django.utils import timezone

class SolicitudCotizacionForm(forms.ModelForm):
    class Meta:
        model = SolicitudCotizacion
        fields = [
            'nombre_cliente',
            'correo_cliente',
            'telefono_cliente',
            'fecha_limite',
            'producto_solicitud',
            'cantidad_solicitud',
            'descripcion_cotizacion',
        ]
        widgets = {
            'fecha_limite': forms.DateTimeInput(attrs={'type': 'datetime-local'}),  # Formato adecuado para la fecha
        }

    def clean_fecha_limite(self):
        fecha_limite = self.cleaned_data['fecha_limite']
        if fecha_limite <= timezone.now():
            raise ValidationError("La fecha límite debe ser posterior a la fecha actual.")
        return fecha_limite

class OrdenDeCompraForm(forms.ModelForm):
    class Meta:
        model = Orden_De_Compra
        fields = [
            'solicitud',
            'proveedor',
            'precio_unitario',
            'cantidad_aprobada',
            'tiempo_entrega',
            'condiciones',
            'estado',
        ]
        widgets = {
            'tiempo_entrega': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'condiciones': forms.Textarea(attrs={'rows': 4}),
        }

    def clean_tiempo_entrega(self):
        tiempo_entrega = self.cleaned_data['tiempo_entrega']
        if tiempo_entrega < timezone.now():
            raise ValidationError("La fecha límite de entrega debe ser posterior o igual a la fecha actual.")
        return tiempo_entrega