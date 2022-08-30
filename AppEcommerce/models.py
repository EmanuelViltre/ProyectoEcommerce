from django.db import models

# Create your models here.
class Comprador(models.Model):
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    direccion = models.CharField(max_length=200)
    dni = models.IntegerField()

    def __str__(self):
        return self.nombre + " " + self.apellido


class Vendedor(models.Model):
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    direccion = models.CharField(max_length=200)
    dni = models.IntegerField()

    def __str__(self):
        return self.nombre + " " + self.apellido


class Producto(models.Model):
    nombre_producto = models.CharField(max_length=200)
    precio = models.DecimalField(max_digits=5, decimal_places=2)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre_producto + " " + str(self.precio)


class Envio(models.Model):
    direccion_emisora = models.CharField(max_length=200)
    direccion_receptora = models.CharField(max_length=200)
    descripcion = models.TextField()
    metodo_envio = models.CharField(max_length=200)

    def __str__(self):
        return self.metodo_envio
