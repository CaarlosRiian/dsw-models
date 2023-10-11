from django.db import models

class Artista(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome

class Selo(models.Model):
    nome_produtora = models.CharField(max_length=50)

    def __str__(self):
        return self.nome_produtora

class Disco(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.CharField(max_length=200)
    selo = models.ForeignKey(Selo, on_delete=models.CASCADE, blank=True, null=True)
    ano = models.DateTimeField("Data Publicada")
    pais = models.CharField(max_length=50) 
    genero = models.CharField(max_length=50)
    quantidade = models.IntegerField()
    artistas = models.ManyToManyField(Artista, related_name="discos")

    def __str__(self):
        return self.nome