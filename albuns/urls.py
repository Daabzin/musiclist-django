from django.urls import path
from . import views

urlpatterns = [
    path('novo/<int:artista_id>/', views.NovoAlbumView.as_view(), name='novo_album'),
    path('delete/<int:id>/', views.DeletarAlbumView.as_view(), name='deletar_album'),
    path('editar/<int:id>/', views.EditarAlbumView.as_view(), name='editar_album'),
]