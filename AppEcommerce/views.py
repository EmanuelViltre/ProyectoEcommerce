from django.http.request import QueryDict
from django.shortcuts import render, HttpResponse
from AppEcommerce.models import Vendedor, Comprador, Envio, Producto


# Create your views here.
def inicio(request):

    return render(request, "AppEcommerce/inicio.html")


def vendedor(request):

    return render(request, "AppEcommerce/vendedor.html")


def comprador(request):

    return render(request, "AppEcommerce/comprador.html")


def envio(request):

    return render(request, "AppEcommerce/envio.html")


def producto(request):

    return render(request, "AppEcommerce/producto.html")
