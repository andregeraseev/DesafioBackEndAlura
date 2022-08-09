from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from renda.views import ReceitaViewSet, DespesasViewSet

router = routers.DefaultRouter()
router.register(r'receita', ReceitaViewSet)
router.register(r'despesas', DespesasViewSet)


urlpatterns = [
    path('', include((router.urls))),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    # path(r'despesas/', FiltroDespesaAPIView.as_view(), name='despesas-filtro')
]
