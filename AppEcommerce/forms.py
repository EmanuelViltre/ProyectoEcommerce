from django import forms


class VendedorFormulario(forms.Form):
    nombre = forms.CharField(max_length=200)
    apellido = forms.CharField(max_length=200)
    direccion = forms.CharField(max_length=200)
    dni = forms.IntegerField()


class CompradorFormulario(forms.Form):
    nombre = forms.CharField(max_length=200)
    apellido = forms.CharField(max_length=200)
    direccion = forms.CharField(max_length=200)
    dni = forms.IntegerField()


class ProductoFormulario(forms.Form):
    nombre_producto = forms.CharField(max_length=200)
    precio = forms.DecimalField(max_digits=10, decimal_places=2)
    descripcion = forms.CharField(max_length=200)


class EnvioFormulario(forms.Form):
    direccion_emisora = forms.CharField(max_length=200)
    direccion_receptora = forms.CharField(max_length=200)
    descripcion = forms.CharField(max_length=200)
    metodo_envio = forms.CharField(max_length=200)
