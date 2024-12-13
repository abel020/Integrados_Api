from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone

class SolicitudCotizacion(models.Model):
    nombre_cliente = models.CharField(max_length=100)
    correo_cliente = models.EmailField()
    telefono_cliente = models.CharField(max_length=20)
    fecha_solicitud = models.DateTimeField(auto_now_add=True)
    fecha_limite = models.DateTimeField()
    producto_solicitud = models.CharField(max_length=100)
    cantidad_solicitud = models.PositiveIntegerField()
    descripcion_cotizacion = models.TextField()
    estado_solicitud = models.CharField(max_length=50, default='En espera')
    estadoActividad = models.PositiveIntegerField(default=1)

    def clean(self):
        # Verifica que fecha_limite sea posterior a la fecha actual
        if self.fecha_limite <= timezone.now():
            raise ValidationError("La fecha límite debe ser posterior a la fecha actual.")

    # Método opcional: si quieres que siempre se valide antes de guardar
    def save(self, *args, **kwargs):
        self.clean()  # Ejecuta la validación antes de guardar
        super().save(*args, **kwargs)

        
class Orden_De_Compra(models.Model):
    solicitud = models.ForeignKey(SolicitudCotizacion, on_delete=models.CASCADE, related_name='ordenes_de_compra')
    proveedor = models.CharField(max_length=100)
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    cantidad_aprobada = models.PositiveIntegerField(default=1)  # Cantidad que se ha decidido comprar
    tiempo_entrega = models.DateTimeField()  # Tiempo de entrega en calendario
    condiciones = models.TextField()
    total = models.DecimalField(max_digits=10, decimal_places=2, editable=False)  # Total calculado
    estado = models.CharField(max_length=50, default='Por revisar')
    fecha_cotizacion = models.DateTimeField(auto_now_add=True)

    def clean(self):
        # Verifica que fecha_limite sea posterior a la fecha actual
        if self.tiempo_entrega < timezone.now():
            raise ValidationError("La fecha límite de entrega debe ser posterior o igual a la fecha actual.")

    def save(self, *args, **kwargs):
        self.clean()  # Ejecuta la validación antes de guardar
        # Calcular el total antes de guardar
        self.total = self.precio_unitario * self.cantidad_aprobada
        super().save(*args, **kwargs)
