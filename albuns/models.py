from django.db import models
from artistas.models import Artista

class Album(models.Model):
    artista = models.ForeignKey(Artista, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=100)
    ano_lancamento = models.IntegerField()
    
    def __str__(self):
        return f"{self.titulo} ({self.ano_lancamento})"