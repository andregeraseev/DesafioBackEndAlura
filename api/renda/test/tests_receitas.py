from django.test import TestCase
from rest_framework.test import APITestCase
from renda.models import Receitas
from django.urls import reverse
from rest_framework import status
# Create your tests here.

class ReceitasTestCase(APITestCase):

    def setUp(self):
        self.list_url = reverse('Receitas-list')
        self.receita_1= Receitas.objects.create(
            descricao='teste', valor='100', categoria= 'aluguel', data= '2022-01-01'
        )

        self.receita_2= Receitas.objects.create(
            descricao='teste 2', valor='10.5', categoria= 'estudos', data= '2022-01-01'
        )


    # def test_falhador(self):
    #     self.fail('Teste falhou de proposito')

    def test_requisicao_get_para_listar_receitas(self):
        """Teste para verificar requisisao GET para uma receita"""

        response = self.client.get('/receitas/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_requisicao_get_para_listar_uma_receitas(self):
        """Teste para verificar requisisao GET para listar as receitas"""

        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_requisicao_post_para_criar_receita(self):
        """Teste para verificar requisisao POST para criar uma receitas"""
        data = {
            'descricao':'teste 3',
            'valor':'11',
            'categoria':'Aluguel',
            'data':'2024-01-08'

        }
        response = self.client.post(self.list_url, data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_requisicao_put_para_alterar_receita(self):
        """Teste para verificar requisisao PUT para alterar uma receita"""
        data = {
            'descricao':'teste autualizado',
            'valor':'50.0',
            'categoria': 'A',
            'data':'2022-02-01'

        }
        response = self.client.put('/receitas/1/', data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_requisicao_post_para_impedir_criar_receitas_no_mesmo_mes_com_mesma_descricao(self):
        """Teste para verificar requisisao POST, para impedir criar duas receitas com mesma descricao no mesmo mes"""
        data = {

            'descricao': 'teste 2',
            'valor': '11',
            'categoria': 'estudos',
            'data': '2022-01-01'

        }
        response = self.client.post(self.list_url, data=data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


    def test_requisicao_post_para_completar_todos_campos_obrigatorios(self):
        """Teste para verificar requisisao POST, para impedir criar receita sem completar campos obrigatorios"""
        data = {

            'descricao': 'teste 2',
            'categoria': 'aluguel',

        }
        response = self.client.post(self.list_url, data=data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_requisicao_delete_para_deletar_receita(self):
        """Teste para verificar a requisição  deletar receita"""
        response = self.client.delete('/receitas/1/')
        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_requisicao_get_para_buscar_receita_por_descricao(self):
        """Teste para verificar a requisição GET que busca as receitas por descrição"""

        response = self.client.get('/receitas/?descricao=test/')
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_requisicao_get_para_filtrar_receita_por_data(self):
        """Teste para verificar a requisição GET que filtra as receitas por data ano, mes"""

        response = self.client.get('/receitas/2022/01/')
        self.assertEquals(response.status_code, status.HTTP_200_OK)





