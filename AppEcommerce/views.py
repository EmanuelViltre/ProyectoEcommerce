from django.http.request import QueryDict
from django.shortcuts import render, HttpResponse
from AppEcommerce.models import Vendedor, Comprador, Envio, Producto
from AppEcommerce.forms import (
    VendedorFormulario,
    ProductoFormulario,
    EnvioFormulario,
    CompradorFormulario,
)

# Create your views here.
def inicio(request):

    return render(request, "AppEcommerce/inicio.html")


def productos(request):

    if request.method == "POST":

        miFormulario = ProductoFormulario(request.POST)

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data

            nombre_producto = (informacion["nombre_producto"],)
            precio = informacion["precio"]
            descripcion = (informacion["descripcion"],)

            producto = Producto(
                nombre_producto=nombre_producto, precio=precio, descripcion=descripcion
            )
            producto.save()

            return render(
                request, "AppEcommerce/inicio.html", {"mensaje": "Producto creado"}
            )

        else:

            return render(request, "AppEcommerce/inicio.html", {"mensaje": "Error"})

    else:

        miFormulario = ProductoFormulario()

    return render(request, "AppEcommerce/productos.html", {"Formulario": miFormulario})


def vendedor(request):

    if request.method == "POST":

        miFormulario = VendedorFormulario(request.POST)

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data

            nombre = (informacion["nombre"],)
            apellido = (informacion["apellido"],)
            direccion = (informacion["direccion"],)
            dni = informacion["dni"]

            vendedores = Vendedor(
                nombre=nombre, apellido=apellido, direccion=direccion, dni=dni
            )
            vendedores.save()

            return render(
                request, "AppEcommerce/inicio.html", {"mensaje": "Vendedor creado"}
            )

        else:

            return render(request, "AppEcommerce/inicio.html", {"mensaje": "Error"})

    else:

        miFormulario = VendedorFormulario()

    return render(request, "AppEcommerce/vendedor.html", {"Formulario": miFormulario})


def comprador(request):

    if request.method == "POST":

        miFormulario = CompradorFormulario(request.POST)

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data

            nombre = (informacion["nombre"],)
            apellido = (informacion["apellido"],)
            direccion = (informacion["direccion"],)
            dni = informacion["dni"]

            Compradores = Comprador(
                nombre=nombre, apellido=apellido, direccion=direccion, dni=dni
            )
            Compradores.save()

            return render(
                request, "AppEcommerce/inicio.html", {"mensaje": "Comprador creado"}
            )

        else:

            return render(request, "AppEcommerce/inicio.html", {"mensaje": "Error"})

    else:

        miFormulario = CompradorFormulario()

    return render(request, "AppEcommerce/comprador.html", {"Formulario": miFormulario})


def envio(request):

    if request.method == "POST":

        miFormulario = EnvioFormulario(request.POST)

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data

            direccion_emisora = (informacion["direccion_emisora"],)
            direccion_receptora = (informacion["direccion_receptora"],)
            descripcion = (informacion["descripcion"],)
            metodo_envio = (informacion["metodo_envio"],)

            Envios = Envio(
                direccion_emisora=direccion_emisora,
                direccion_receptora=direccion_receptora,
                descripcion=descripcion,
                metodo_envio=metodo_envio,
            )
            Envios.save()

            return render(
                request, "AppEcommerce/inicio.html", {"mensaje": "Envio creado"}
            )

        else:

            return render(request, "AppEcommerce/inicio.html", {"mensaje": "Error"})

    else:

        miFormulario = EnvioFormulario()

    return render(request, "AppEcommerce/envio.html", {"Formulario": miFormulario})


def buscar(request):

    if request.GET["dni"]:

        dni = request.GET["dni"]
        vendedores = Vendedor.objects.filter(dni__icontains=dni)

        return render(
            request, "AppEcommerce/inicio.html", {"vendedores": vendedores, "dni": dni}
        )

    else:

        respuesta = "No enviaste datos"

        return HttpResponse(respuesta)
