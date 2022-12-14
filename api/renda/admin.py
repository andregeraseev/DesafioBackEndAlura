from django.contrib import admin
from .models import Receitas, Despesas


class Receita(admin.ModelAdmin):
    list_display = ('id', 'descricao', 'valor', 'categoria', 'data',)
    list_display_links = ('id', 'descricao',)
    search_fields = ('descricao',)


admin.site.register(Receitas, Receita)

class Despesa(admin.ModelAdmin):
    list_display = ('id', 'descricao', 'valor', 'categoria', 'data',)
    list_display_links = ('id', 'descricao',)
    search_fields = ('descricao',)

admin.site.register(Despesas, Despesa)

# Register your models here.
