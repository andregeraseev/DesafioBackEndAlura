from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from renda.views import ReceitaViewSet, DespesasViewSet, BuscaDespesasList,BuscaReceitasList,ListaReceitasMes, ListaDespesasMes, ResumoView

router = routers.DefaultRouter()
router.register(r'receitas', ReceitaViewSet)
router.register(r'despesas', DespesasViewSet)


urlpatterns = [
    path('', include((router.urls))),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('despesas?categoria=<slug:pk>', BuscaDespesasList.as_view()),
    path('receitas?descricao=<slug:pk>', BuscaReceitasList.as_view()),
    path('receitas/<int:ano>/<int:mes>/', ListaReceitasMes.as_view()),
    path('despesas/<int:ano>/<int:mes>/', ListaDespesasMes.as_view()),
    path('resumo/<int:ano>/<int:mes>/', ResumoView.as_view())

]
