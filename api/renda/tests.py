# from django.test import TestCase
# from rest_framework.test import APITestCase
# from renda.models import Despesas
# from django.urls import reverse
# from rest_framework import status
# # Create your tests here.
#
# class DespesasTestCase(APITestCase):
#
#     def setUp(self):
#         self.list_url = reverse('Despesas-list')
#         self.curso_1= Despesas.objects.create(
#             descricao='teste', valor='10.5', categoria= 'I', data= '2022-01-01'
#         )
#         self.list_url = reverse('Despesas-list')
#         self.curso_1= Despesas.objects.create(
#             descricao='teste 2', valor='10.5', categoria= 'I', data= '2022-01-01'
#         )
#
#
#     # def test_falhador(self):
#     #     self.fail('Teste falhou de proposito')
#
#     def test_requisicao_get_para_listar_despesa(self):
#         """Teste para verificar requisisao GET para uma despesa"""
#         response = self.client.get('/despesas/1/')
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#
#     def test_requisicao_get_para_listar_despesas(self):
#         """Teste para verificar requisisao GET para listar as despesas"""
#         response = self.client.get(self.list_url)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#
#     def test_requisicao_post_para_criar_despesa(self):
#         """Teste para verificar requisisao POST para criar uma despesas"""
#         data = {
#             'descricao':'teste 3',
#             'valor':'11',
#             'categoria':'A',
#             'data':'2022-01-08'
#
#         }
#         response = self.client.post(self.list_url, data=data)
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#
#     def test_requisicao_put_para_alterar_despesa(self):
#         """Teste para verificar requisisao PUT para alterar uma despesa"""
#         data = {
#             'descricao':'teste autualizado',
#             'valor':'50.0',
#             'categoria': 'A',
#             'data':'2022-02-01'
#
#         }
#         response = self.client.put('/despesas/1/', data=data)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#
#
#     def test_requisicao_post_para_impedir_criar_despesa_mesmo_mes_com_mesma_descricao(self):
#         """Teste para verificar requisisao POST, para impedir criar duas despesas com mesma descricao no mesmo mes"""
#         data = {
#
#             'descricao': 'teste 2',
#             'valor': '11',
#             'categoria': 'A',
#             'data': '2022-01-01'
#
#         }
#         response = self.client.post(self.list_url, data=data)
#         self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
#
#
#     def test_requisicao_post_para_completar_todos_campos_obrigatorios(self):
#         """Teste para verificar requisisao POST, para impedir criar despesa sem completar campos obrigatorios"""
#         data = {
#
#             'descricao': 'teste 2',
#             'categoria': 'A',
#
#         }
#         response = self.client.post(self.list_url, data=data)
#         self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
#
#     def test_requisicao_delete_para_deletar_despesa(self):
#         """Teste para verificar a requisição  deletar despesa"""
#         response = self.client.delete('/despesas/1/')
#         self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)
#
#     def test_requisicao_get_para_buscar_despesa_por_descricao(self):
#         """Teste para verificar a requisição GET que busca as despesas por descrição"""
#
#         response = self.client.get('/despesas/?descricao=test/')
#         self.assertEquals(response.status_code, status.HTTP_200_OK)
#
#     def test_requisicao_get_para_filtrar_despesa_por_data(self):
#         """Teste para verificar a requisição GET que filtra as despesas por data ano, mes"""
#
#         response = self.client.get('/despesas/2022/01/')
#         self.assertEquals(response.status_code, status.HTTP_200_OK)
#
#
#
#
#
