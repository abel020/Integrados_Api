from django.urls import path, include
from rest_framework import routers
from API import views

router = routers.DefaultRouter()
router.register(r'SCotizacion', views.SCotizacionViewSet)
router.register(r'OrdenCompra', views.Orden_De_Compra_ViewSet)

urlpatterns = [
    path('', include(router.urls)),
]