from django import forms
from .models import Artista, Genero

class ArtistaForm(forms.ModelForm):
    class Meta:
        model = Artista
        fields = '__all__'

class GeneroForm(forms.ModelForm):
    class Meta:
        model = Genero
        fields = '__all__'