from django.db import models

# Create your models here.
class Genero(models.Model):
    nombre = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre


class Editorial(models.Model):
    nombre = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre


class Autor(models.Model):
    nombre = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre


class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=200)
    anio = models.IntegerField()
    disponible = models.BooleanField(default=True)
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE)
    editorial = models.ForeignKey(Editorial, on_delete=models.CASCADE, null=True, blank=True)
    autores = models.ManyToManyField(Autor, blank=True)
    sinopsis = models.TextField(blank=True)
    precio = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True, default=0)
    estado = models.CharField(max_length=10, choices=[
        ('ARCHIVADO', 'ARCHIVADO'),
        ('PERDIDO', 'PERDIDO'),
        ('PRESTADO', 'PRESTADO'),
        ('DISPONIBLE', 'DISPONIBLE'),
    ], default='DISPONIBLE')

    def __str__(self):
        return self.titulo
