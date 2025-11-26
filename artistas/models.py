from django.db import models

class Genero(models.Model):
    nome = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nome

class Artista(models.Model):
    nome = models.CharField(max_length=100)
    pais_origem = models.CharField(max_length=50)
    genero = models.ForeignKey(Genero, on_delete=models.PROTECT, verbose_name="Gênero Musical")

    def __str__(self):
        return self.nome