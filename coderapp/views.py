from django.shortcuts import render, redirect, HttpResponse
from django.http.request import QueryDict
from django.http import HttpResponse
from .forms import AlbumEscuchadoFormulario
from .models import AlbumesEscuchados, Artista, AlbumesPendiente

def index(request):

      return render(request, "coderapp/index.html")

def albumes_pendiente(request):

      albumes_pendiente =  AlbumesPendiente(album="TESTING", año="2018")
      albumes_pendiente.save()
      documentoDeTexto = f"--->Album: {albumes_pendiente.album}   Año: {albumes_pendiente.año}"


      return HttpResponse(documentoDeTexto)

def inicio(request):

      return render(request, "coderapp/inicio.html")

def artista(request):
    artistas = Artista.objects.all()
    print(artistas)
    return render(request, 'coderapp/artista_form.html', {'artistas': artistas})


def agregar_album(request):
    if request.method == 'POST':
        miFormulario = AlbumEscuchadoFormulario(request.POST)
        if miFormulario.is_valid():  # Agrega paréntesis a is_valid
            informacion = miFormulario.cleaned_data
            album = AlbumesEscuchados(nombre=informacion['nombre'], año=informacion['año'])
            album.save()  # Corrige el nombre de la variable (profesor a album)
            return render(request, "coderapp/album_escuchado_confirmacion.html", {"album": album})
    else:
        miFormulario = AlbumEscuchadoFormulario()

    return render(request, "coderapp/album_escuchado_form.html", {"miFormulario": miFormulario})

def buscar(request):
    if request.GET.get("album"):
        album = request.GET['album']
        año = AlbumesPendiente.objects.filter(album__icontains=año)
        return render(request, "coderapp/album_pendiente_form.html", {"album": album, "año": año})
    else:
        respuesta = "No enviaste datos"
    return HttpResponse(respuesta)
