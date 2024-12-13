from django import forms
from .models import SolicitudCotizacion
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
