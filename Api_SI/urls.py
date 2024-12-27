"""
URL configuration for Api_SI project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.documentation import include_docs_urls
from API.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',inicio, name='inicio'),
    path('api/', include('API.urls')),
    path('docs/', include_docs_urls(title='Api documentacion')),
    path('Scotizacion/', Scotizacion, name='Scotizacion'),
    path('Scompra/', Scompra, name='Scompra'),
    path('solicitud_exito/', solicitud_exito, name='solicitud_exito'),
    path('acerca_erp/', acerca_erp, name='acerca_erp'),
    path('soporte/', soporte, name='soporte'),
    path('scompra/<int:pk>/actualizar/', actualizar_scompra, name='actualizar_scompra'),
    path('scompra/<int:pk>/eliminar/', eliminar_scompra, name='eliminar_scompra'),
    path('scotizacion/<int:pk>/actualizar/', actualizar_scotizacion, name='actualizar_scotizacion'),
    path('scotizacion/<int:pk>/eliminar/', eliminar_scotizacion, name='eliminar_scotizacion'),
]

