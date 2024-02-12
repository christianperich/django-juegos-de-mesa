from django.db import models

# Create your models here.
class Tienda(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre
    
    
class Juego(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre
    

class Detalles(models.Model):
    tienda = models.ForeignKey(Tienda, on_delete=models.CASCADE)
    juego = models.ForeignKey(Juego, on_delete=models.CASCADE)
    precio = models.IntegerField()
    url = models.URLField()
    imagen_url = models.URLField()

    def __str__(self):
        return f'{{self.juego}} - {{self.tienda}}'
    
