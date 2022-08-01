from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import BasicAuthentication
from rest_framework import viewsets
from .models import Receita, Despesas
from .serializers import ReceitaSerializer, DespesasSerializer

class ReceitaViewSet(viewsets.ModelViewSet):
    queryset = Receita.objects.all()
    serializer_class = ReceitaSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class DespesasViewSet(viewsets.ModelViewSet):
    queryset = Despesas.objects.all()
    serializer_class = DespesasSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
