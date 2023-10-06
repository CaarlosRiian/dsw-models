from django.db import models

class Disco(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.CharField(max_length=200)
    nome_produtora = models.CharField(max_length=50)
    ano = models.DateTimeField("Data Publicada")
    pais = models.CharField(max_length=50) 
    genero = models.CharField(max_length=50)
    quantidade = models.IntegerField()

# Toda vez que mudar algo nos models
# você tem que atualziar o banco de dados
# python manage.py makemigrations -> mandar atualizações
# python manage.py migrate -> atualizar