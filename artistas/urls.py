from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('novo_artista/', views.NovoArtistaView.as_view(), name='novo_artista'),
    path('novo_genero/', views.NovoGeneroView.as_view(), name='novo_genero'),
    path('<int:id>/', views.DetalhesView.as_view(), name='detalhes'),
    path('<int:id>/deletar/', views.DeletarArtistaView.as_view(), name='deletar_artista'),
    path('artista/editar/<int:id>/', views.EditarArtistaView.as_view(), name='editar_artista'),
    path('generos/', views.ListaGenerosView.as_view(), name='lista_generos'),
    path('generos/editar/<int:id>/', views.EditarGeneroView.as_view(), name='editar_genero'),
    path('generos/deletar/<int:id>/', views.DeletarGeneroView.as_view(), name='deletar_genero'),

]