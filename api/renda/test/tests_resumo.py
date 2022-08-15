from rest_framework.test import APITestCase, APIClient
from renda.models import Despesas, Receitas
from rest_framework import status
from django.contrib.auth.models import User



class ResumoTestCase(APITestCase):

    def autentica(self):
        """funçao para autenticar"""
        self.user = User.objects.create_user('c3po', password='123456')
        return self.client.force_authenticate(user=self.user)


    def setUp(self):



        self.receita_test= Receitas.objects.create(
            descricao='teste resumo receita', valor='100', categoria= 'venda', data= '2022-01-01'
        )

        self.despesa_test= Despesas.objects.create(
            descricao='teste resumo despesa', valor='200', categoria= 'A', data= '2022-01-01'
        )


    def test_requisicao_get_para_filtrar_resumo_por_data(self):
        """Teste para verificar a requisição GET que filtra o resumo do mes"""
        self.autentica()
        response = self.client.get('/resumo/2022/01/')
        self.assertEquals(response.status_code, status.HTTP_200_OK)
