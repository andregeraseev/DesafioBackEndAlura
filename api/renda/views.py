from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import BasicAuthentication
from rest_framework import viewsets, filters, generics
from .models import Receitas, Despesas
from .serializers import ReceitaSerializer, DespesasSerializer
from django_filters.rest_framework import DjangoFilterBackend
import django_filters.rest_framework
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Sum


class ReceitaViewSet(viewsets.ModelViewSet):
    queryset = Receitas.objects.all()
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

        queryset = Receitas.objects.filter(data__year=self.kwargs['ano'], data__month=self.kwargs['mes'])
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

class ListaDespesasMes(generics.ListAPIView):
    """Exibindo todas as receitas de um determinado mês"""

    def get_queryset(self):

        queryset = Despesas.objects.filter(data__year=self.kwargs['ano'], data__month=self.kwargs['mes'])
        return queryset

    serializer_class = ReceitaSerializer

class ResumoView(APIView):

    def get(self, request, ano, mes):
        total_despesas =  Despesas.objects.filter(data__year=ano, data__month=mes).aggregate(Sum('valor'))['valor__sum']

        despesa_por_categoria = Despesas.objects.filter(data__year=ano,
                                                       data__month=mes).values('categoria').annotate(Sum('valor'))

        for despesa in despesa_por_categoria:
            print(despesa)
            despesa['R$'] = despesa['valor__sum']
            del despesa['valor__sum']


        total_receitas = Receitas.objects.filter(data__year=ano, data__month=mes).aggregate(Sum('valor'))['valor__sum']
        if total_receitas == None:
            saldo_final = total_despesas

        elif total_despesas == None:
            saldo_final = total_receitas

        else:
            saldo_final = total_receitas - total_despesas


        return Response({
            'total_despesas': total_despesas,
            'total_receitas': total_receitas,
            'saldo_final': saldo_final,
            'despesa_por_categoria': despesa_por_categoria

        })














