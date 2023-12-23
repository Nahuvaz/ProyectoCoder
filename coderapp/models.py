from django.db import models

class Artista(models.Model):
    nombre = models.CharField(max_length=30)
    
class AlbumesEscuchados(models.Model):
    nombre = models.CharField(max_length=100,  default='Desconocido')
    año = models.PositiveIntegerField()

    def __str__(self):
        return self.nombre
    
class AlbumesPendiente(models.Model):
    album= models.CharField(max_length=30)
    año = models.PositiveIntegerField()
    