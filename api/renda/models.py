from django.db import models

class Receita(models.Model):

    descricao = models.CharField(max_length=100, unique_for_month="data")
    valor = models.IntegerField()
    categoria = models.CharField(max_length=50)
    data = models.DateField()

    def __str__(self):
        return self.descricao

class Despesas(models.Model):

    descricao = models.CharField(unique_for_month="data", max_length=100)
    valor = models.IntegerField()
    categoria = models.CharField(max_length=50)
    data = models.DateField()

    def __str__(self):
        return self.descricao

