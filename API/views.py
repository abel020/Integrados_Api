from django.http import HttpResponse
import requests
from rest_framework import viewsets

from API.forms import OrdenDeCompraForm, SolicitudCotizacionForm
from .serializer import *
from .models import *
from django.shortcuts import redirect, render
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
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

def Scompra(request):
    # Consume las APIs externas
    response = requests.get('https://sistemas-integrados-inventario-production.up.railway.app/api/proveedores/')

    if response.status_code == 200:
        data = response.json()

        # Maneja la solicitud POST (envío del formulario)
        if request.method == 'POST':
            form = OrdenDeCompraForm(request.POST)
            if form.is_valid():
                form.save()  # Guarda la solicitud si es válida
                return solicitud_exito(request)  # Llama a la función y devuelve su resultado
            else:
                return JsonResponse({
                    'status': 'error',
                    'message': 'Hubo un error al enviar el formulario.'
                })

        # Maneja la solicitud GET (muestra el formulario y los datos de las APIs)
        else:
            form = OrdenDeCompraForm()
            context = {
                'proveedores': data,
                'solicitudes': SolicitudCotizacion.objects.all(),  # Obtén las solicitudes relacionadas
            }
            return render(request, 'Scompras.html', context)
    else:
        # Maneja errores en caso de que alguna de las APIs falle
        return render(request, 'error.html', {'error': 'Error al consumir las APIs'})
    

def actualizar_scompra(request, pk):
    # Obtener la orden de compra mediante el ID (pk)
    orden_compra = get_object_or_404(Orden_De_Compra, pk=pk)

    # Consumir las API de proveedores
    response = requests.get('https://sistemas-integrados-inventario-production.up.railway.app/api/proveedores/')
    
    if response.status_code == 200:
        data = response.json()

        # Procesar el formulario de actualización
        if request.method == 'POST':
            form = OrdenDeCompraForm(request.POST, instance=orden_compra)
            if form.is_valid():
                form.save()  # Guarda los cambios
                return redirect('solicitud_exito')  # Redirige a la página de éxito
            else:
                return JsonResponse({
                    'status': 'error',
                    'message': 'Hubo un error al actualizar la solicitud.'
                })

        else:
            form = OrdenDeCompraForm(instance=orden_compra)
            context = {
                'form': form,
                'proveedores': data,  # Pasamos los proveedores al contexto
                'solicitudes': SolicitudCotizacion.objects.all()  # Pasamos las solicitudes al contexto
            }
            return render(request, 'Scompras.html', context)
    else:
        return render(request, 'error.html', {'error': 'Error al consumir las APIs'})

def eliminar_scompra(request, pk):
    orden_compra = get_object_or_404(Orden_De_Compra, pk=pk)
    orden_compra.delete()  # Elimina la orden de compra
    return redirect('solicitud_exito')  # Redirige a la página de éxito

def ObtenerCotizacion(request):
    cotizaciones = SolicitudCotizacion.objects.all()
    return render(request, 'Solicitud_exito.html', {'cotizaciones': cotizaciones})

def Scotizacion(request):
    # Consume las APIs externas
    response = requests.get('https://contactomodulo-production.up.railway.app/api/clientes')
    response2 = requests.get('https://sistemas-integrados-inventario-production.up.railway.app/api/productos/')

    if response.status_code == 200 and response2.status_code == 200:
        data = response.json()
        data2 = response2.json()

        # Maneja la solicitud POST (envío del formulario)
        if request.method == 'POST':
            form = SolicitudCotizacionForm(request.POST)
            if form.is_valid():
                form.save()  # Guarda la solicitud si es válida
                return solicitud_exito(request)  # Llama a la función y devuelve su resultado
            else:
                return JsonResponse({
                    'status': 'error',
                    'message': 'Hubo un error al enviar el formulario.'
                })

        # Maneja la solicitud GET (muestra el formulario y los datos de las APIs)
        else:
            form = SolicitudCotizacionForm()
            context = {
                'form': form,
                'clientes': data,
                'productos': data2
            }
            return render(request, 'Scotizacion.html', context)

    else:
        # Maneja errores en caso de que alguna de las APIs falle
        return render(request, 'error.html', {'error': 'Error al consumir las APIs'})

def actualizar_scotizacion(request, pk):
    # Obtener la cotización por pk
    cotizacion = get_object_or_404(SolicitudCotizacion, pk=pk)

    # Consumir las APIs
    response = requests.get('https://contactomodulo-production.up.railway.app/api/clientes')
    response2 = requests.get('https://sistemas-integrados-inventario-production.up.railway.app/api/productos/')

    if response.status_code == 200 and response2.status_code == 200:
        data = response.json()
        data2 = response2.json()

        # Procesar el formulario
        if request.method == 'POST':
            form = SolicitudCotizacionForm(request.POST, instance=cotizacion)
            if form.is_valid():
                form.save()
                return redirect('solicitud_exito')  # Redirige a una página de éxito
        else:
            form = SolicitudCotizacionForm(instance=cotizacion)

        # Pasar las APIs al contexto
        return render(request, 'Scotizacion.html', {
            'form': form,
            'clientes': data,
            'productos': data2
        })
    else:
        return render(request, 'error.html', {'error': 'Error al consumir las APIs'})


def eliminar_scotizacion(request, pk):
    cotizacion = get_object_or_404(SolicitudCotizacion, pk=pk)
    cotizacion.delete()  # Elimina la solicitud de cotización
    return redirect('solicitud_exito')  # Redirige a la página de éxito

def solicitud_exito(request):
    # Recuperar todas las solicitudes de cotización y órdenes de compra
    cotizaciones = SolicitudCotizacion.objects.all()
    compras = Orden_De_Compra.objects.all()

    context = {
        'cotizaciones': cotizaciones,
        'compras': compras,
    }
    return render(request, 'solicitud_exito.html', context)

def index(request):
    return render(request, 'index.html')

def acerca_erp(request):
    return render(request, 'acerca_erp.html')

def soporte(request):
    return render(request, 'soporte.html')
