from rest_framework import routers, serializers, viewsets
from .models import Receita,Despesas


class ReceitaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Receita
        fields = ['descricao', 'valor' ,'categoria', 'data']

class DespesasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Despesas
        fields = ['descricao', 'valor' ,'categoria', 'data']