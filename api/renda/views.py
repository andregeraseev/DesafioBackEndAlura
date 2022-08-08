from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import BasicAuthentication
from rest_framework import viewsets, filters
from .models import Receita, Despesas
from .serializers import ReceitaSerializer, DespesasSerializer
from django_filters.rest_framework import DjangoFilterBackend


class ReceitaViewSet(viewsets.ModelViewSet):
    queryset = Receita.objects.all()
    serializer_class = ReceitaSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class DespesasViewSet(viewsets.ModelViewSet):
    queryset = Despesas.objects.all()
    serializer_class = DespesasSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['descricao']
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

