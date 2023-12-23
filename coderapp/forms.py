from django import forms

class ArtistaForm(forms.Form):
    nombre = forms.CharField(max_length=30)

class AlbumEscuchadoFormulario(forms.Form):   
    nombre= forms.CharField(max_length=30)
    año= forms.IntegerField()

class AlbumPendienteForm(forms.Form):
    album = forms.CharField(max_length=30)
    año = forms.IntegerField()