from django.db import models

class Receita(models.Model):

    descricao = models.CharField(max_length=100, unique_for_month="data")
    valor = models.DecimalField(max_digits=8, decimal_places=2)
    categoria = models.CharField(max_length=50)
    data = models.DateField()

    def __str__(self):
        return self.descricao

class Despesas(models.Model):
    CATEGORIAS = (
        ('A', 'Alimentação'),
        ('S', 'Saúde'),
        ('M', 'Moradia'),
        ('T', 'Transporte'),
        ('E', 'Educação'),
        ('L', 'Lazer'),
        ('I', 'Imprevistos'),
        ('O', 'Outras')
    )

    descricao = models.CharField(unique_for_month="data", max_length=100)
    valor = models.DecimalField(max_digits=8, decimal_places=2)
    categoria = models.CharField(max_length=1, null=False, blank=False, choices= CATEGORIAS, default='O')
    data = models.DateField()

    def __str__(self):
        return self.descricao

