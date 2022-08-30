from django.urls import path
from AppEcommerce import views


urlpatterns = [
    path("", views.inicio, name="Inicio"),
    path("producto", views.producto, name="Producto"),
    path("vendedor", views.vendedor, name="Vendedor"),
    path("comprador", views.comprador, name="Comprador"),
    path("envio", views.envio, name="Envio"),
]
