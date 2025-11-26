from django.urls import path
from . import views

urlpatterns = [
    path('novo/<int:artista_id>/', views.NovoAlbumView.as_view(), name='novo_album'),
]