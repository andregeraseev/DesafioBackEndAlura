from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import BasicAuthentication
from rest_framework import viewsets, filters, generics
from .models import Receita, Despesas
from .serializers import ReceitaSerializer, DespesasSerializer
from django_filters.rest_framework import DjangoFilterBackend
import django_filters.rest_framework


class ReceitaViewSet(viewsets.ModelViewSet):
    queryset = Receita.objects.all()
    serializer_class = ReceitaSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['descricao']
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class BuscaReceitasList(generics.ListAPIView):
    """Busca receita pela descricao"""
    queryset = Despesas.objects.all()
    serializer_class = ReceitaSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filter_backends[1].search_param = 'descricao'
    search_fields = ['descricao']

class ListaReceitasMes(generics.ListAPIView):
    """Exibindo todas as receitas de um determinado mês"""

    def get_queryset(self):

        queryset = Receita.objects.filter(data__year=self.kwargs['ano'], data__month=self.kwargs['mes'])
        return queryset

    serializer_class = ReceitaSerializer


class DespesasViewSet(viewsets.ModelViewSet):
    queryset = Despesas.objects.all()
    serializer_class = DespesasSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['descricao']
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    filter_backends[1].search_param = 'descricao'
    search_fields = ['descricao']

class BuscaDespesasList(generics.ListAPIView):
    """Busca despesas pela descricao"""
    queryset = Despesas.objects.all()
    serializer_class = DespesasSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filter_backends[1].search_param = 'descricao'
    search_fields = ['descricao']















