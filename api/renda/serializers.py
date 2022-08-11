from rest_framework import routers, serializers, viewsets
from .models import Receitas,Despesas


class ReceitaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Receitas
        fields = ['descricao', 'valor', 'categoria', 'data']

class DespesasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Despesas
        fields = ['descricao', 'valor', 'categoria', 'data']



