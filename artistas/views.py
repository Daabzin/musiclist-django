from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.db.models import Q
from .models import Artista, Genero
from .forms import ArtistaForm, GeneroForm
from albuns.models import Album

class HomeView(View):
    def get(self, request):
        query = request.GET.get('busca')
        if query:
            artistas = Artista.objects.filter(
                Q(nome__icontains=query) | Q(genero__nome__icontains=query)
            )
        else:
            artistas = Artista.objects.all()
        return render(request, 'artistas/home.html', {'artistas': artistas})

class NovoGeneroView(View):
    def get(self, request):
        form = GeneroForm()
        return render(request, 'artistas/form_genero.html', {'form': form})

    def post(self, request):
        form = GeneroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('novo_artista')
        return render(request, 'artistas/form_genero.html', {'form': form})

class NovoArtistaView(View):
    def get(self, request):
        form = ArtistaForm()
        return render(request, 'artistas/form_artista.html', {'form': form})

    def post(self, request):
        form = ArtistaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        return render(request, 'artistas/form_artista.html', {'form': form})

class DetalhesView(View):
    def get(self, request, id):
        artista = get_object_or_404(Artista, id=id)
        albuns = Album.objects.filter(artista=artista)
        return render(request, 'artistas/detalhes.html', {
            'artista': artista, 
            'albuns': albuns
        })

class DeletarArtistaView(View):
    def get(self, request, id):
        artista = get_object_or_404(Artista, id=id)
        return render(request, 'artistas/confirmar_delete.html', {'artista': artista})

    def post(self, request, id):
        artista = get_object_or_404(Artista, id=id)
        artista.delete()
        return redirect('home')