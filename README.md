# Sistema de Módulo de Compras

## Descripción

Este proyecto es un sistema de gestión de compras desarrollado con Django REST Framework, SQLite y APIs REST. Permite a los usuarios gestionar solicitudes de cotización y órdenes de compra a través de una interfaz sencilla y efectiva.

## Autor

Gomez Abel

## Tecnologías Utilizadas

- **Django REST Framework**: Framework para construir APIs web.
- **SQLite**: Base de datos ligera.
- **Python**: Lenguaje de programación utilizado.
- **Django**: Framework web para el desarrollo de aplicaciones.

## Estructura de la Base de Datos

Este sistema cuenta con dos tablas principales:

### 1. SolicitudCotizacion

- **nombre_cliente**: Nombre del cliente que realiza la solicitud.
- **correo_cliente**: Correo electrónico del cliente.
- **telefono_cliente**: Teléfono del cliente.
- **fecha_solicitud**: Fecha en la que se realiza la solicitud.
- **fecha_limite**: Fecha límite para la cotización.
- **producto_solicitud**: Producto solicitado.
- **cantidad_solicitud**: Cantidad solicitada.
- **descripcion_cotizacion**: Descripción de la cotización.
- **estado_solicitud**: Estado actual de la solicitud.
- **estadoActividad**: Estado de actividad de la solicitud.

### 2. Orden_De_Compra

- **solicitud**: Relación con la solicitud de cotización.
- **proveedor**: Proveedor asociado a la orden.
- **precio_unitario**: Precio por unidad del producto.
- **cantidad_aprobada**: Cantidad aprobada para la compra.
- **tiempo_entrega**: Fecha y hora de entrega.
- **condiciones**: Condiciones de la compra.
- **total**: Total calculado para la orden.
- **estado**: Estado actual de la orden.
- **fecha_cotizacion**: Fecha de la cotización.

## Consumo de APIs

El sistema también consume varias APIs para enriquecer la funcionalidad de la aplicación. A continuación se describen las APIs utilizadas:

1. **API de Clientes**
   ```python
   'https://contactomodulo-production.up.railway.app/api/clientes'
   ```
   Esta API permite obtener información sobre los clientes registrados en el sistema.

2. **API de Productos**
   ```python
   'https://sistemas-integrados-inventario-production.up.railway.app/api/productos/'
   ```
   Esta API proporciona acceso a la lista de productos disponibles en el inventario.

3. **API de Proveedores**
   ```python
   'https://sistemas-integrados-inventario-production.up.railway.app/api/proveedores/'
   ```
   Con esta API se puede obtener información sobre los proveedores disponibles para las órdenes de compra.

## Instalación

1. Clona este repositorio:
   ```bash
   git clone https://github.com/abel020/SistemaModuloCompras.git
   ```

2. Navega al directorio del proyecto:
   ```bash
   cd SistemaModuloCompras
   ```

3. Crea un entorno virtual e instálalo:
   ```bash
   python -m venv env
   source env/bin/activate  # En Windows usa `env\Scripts\activate`
   pip install -r requirements.txt
   ```

4. Inicia el servidor:
   ```bash
   python manage.py runserver
   ```

## Uso

1. Abre tu navegador y ve a `http://127.0.0.1:8000`.
2. Utiliza las APIs disponibles para gestionar solicitudes de cotización y órdenes de compra.

## Capturas de Pantalla

### Menú Principal
![Menú Principal](stactifiles/rest_framework/img/menu.jpeg)

### Formulario de Solicitud de Cotización
![Formulario de Solicitud de Cotización](stactifiles/rest_framework/img/FCot.jpeg)

### Formulario de Orden de Compra
![Formulario de Orden de Compra](stactifiles/rest_framework/img/FCom.jpeg)

### Resumen de Solicitudes
![Resumen de Solicitudes](stactifiles/rest_framework/img/Resumen.jpeg)

![Resumen de Solicitudes](stactifiles/rest_framework/img/ResumenCompra.jpeg)

### API REST Framework
![API REST Framework](stactifiles/rest_framework/img/menu.jpeg)

## Despliegue

Este proyecto está desplegado en Railway. Puedes acceder a la aplicación en el siguiente enlace:

[Enlace a la aplicación desplegada](https://web-production-e323b.up.railway.app)

### Archivos importantes para el despliegue

- **Procfile**: Este archivo es necesario para que Railway sepa cómo ejecutar la aplicación.
- **runtime.txt**: Este archivo especifica la versión de Python que se utilizará en el entorno de Railway.

## Contribuciones

Si deseas contribuir a este proyecto, por favor sigue estos pasos:

1. Realiza un fork del repositorio.
2. Crea una nueva rama (`git checkout -b feature/nueva-caracteristica`).
3. Realiza tus cambios y haz un commit (`git commit -m 'Añadir nueva característica'`).
4. Haz push a la rama (`git push origin feature/nueva-caracteristica`).
5. Abre un Pull Request.


