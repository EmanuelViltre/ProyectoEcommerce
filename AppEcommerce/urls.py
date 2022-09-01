from django.urls import path
from AppEcommerce import views


urlpatterns = [
    path("", views.inicio, name="Inicio"),
    path("vendedor/", views.vendedor, name="Vendedor"),
    path("comprador/", views.comprador, name="Comprador"),
    path("envio/", views.envio, name="Envio"),
    path("productos/", views.productos, name="Productos"),
    path("buscar/", views.buscar, name="buscar"),
]
