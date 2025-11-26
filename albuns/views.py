from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .forms import AlbumForm
from albuns.models import Album
from artistas.models import Artista

class NovoAlbumView(View):
    def get(self, request, artista_id):
        artista = get_object_or_404(Artista, id=artista_id)
        form = AlbumForm()
        return render(request, 'albuns/form_album.html', {'form': form, 'artista': artista})

    def post(self, request, artista_id):
        artista = get_object_or_404(Artista, id=artista_id)
        form = AlbumForm(request.POST)
        
        if form.is_valid():
            album = form.save(commit=False)
            album.artista = artista
            album.save()
            return redirect('detalhes', id=artista_id)
            
        return render(request, 'albuns/form_album.html', {'form': form, 'artista': artista})
    
class DeletarAlbumView(View):
    def get(self, request, id):
        album = get_object_or_404(Album, id=id)
        return render(request, 'albuns/confirmar_delete_album.html', {'album': album})

    def post(self, request, id):
        album = get_object_or_404(Album, id=id)
        artista_id = album.artista.id 
        album.delete()
        return redirect('detalhes', id=artista_id) 
    
class EditarAlbumView(View):
    def get(self, request, id):
        album = get_object_or_404(Album, id=id)
        form = AlbumForm(instance=album)
        return render(request, 'albuns/form_album.html', {
            'form': form, 
            'artista': album.artista, 
            'editar': True
        })

    def post(self, request, id):
        album = get_object_or_404(Album, id=id)
        form = AlbumForm(request.POST, instance=album)
        
        if form.is_valid():
            form.save()
            return redirect('detalhes', id=album.artista.id)
            
        return render(request, 'albuns/form_album.html', {
            'form': form, 
            'artista': album.artista, 
            'editar': True
        })