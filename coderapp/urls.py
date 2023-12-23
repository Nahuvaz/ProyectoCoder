from django.urls import path
from coderapp import views 

urlpatterns = [
    path('', views.index, name='index'), 
    path('artista', views.artista, name='artista'),
    path('album-escuchado', views.agregar_album, name='agregar_album'),
    path('albumes-pendiente', views.albumes_pendiente, name='album_pendiente'),
    path('buscar/', views.buscar),
]