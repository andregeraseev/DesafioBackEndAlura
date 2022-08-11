from django.test import TestCase
from rest_framework.test import APITestCase
from renda.models import Despesas
from django.urls import reverse
from rest_framework import status
# Create your tests here.

class DespesasTestCase(APITestCase):

    def setUp(self):
        self.list_url = reverse('Despesas-list')
        self.curso_1= Despesas.objects.create(
            descricao='teste', valor='10.5', categoria= 'I', data= '2022-01-01'
        )
        self.list_url = reverse('Despesas-list')
        self.curso_1= Despesas.objects.create(
            descricao='teste 2', valor='10.5', categoria= 'I', data= '2022-01-01'
        )


    # def test_falhador(self):
    #     self.fail('Teste falhou de proposito')


    def test_requisicao_get_para_listar_despesas(self):
        """Teste para verificar requisisao GET para listar as despesas"""
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code,status.HTTP_200_OK)

    def test_requisicao_put_para_criar_despesa(self):
        """Teste para verificar requisisao POST para criar uma despesas"""
        data = {
            'descricao':'teste 3',
            'valor':'11',
            'categoria':'A',
            'data':'2022-01-08'

        }
        response = self.client.post(self.list_url, data=data)
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)



