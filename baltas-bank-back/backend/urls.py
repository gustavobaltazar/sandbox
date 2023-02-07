from . import views
from rest_framework_nested import routers   

router = routers.DefaultRouter()
router.register('usuarios', views.UsuarioViewSet, basename='usuarios')
router.register('clientes', views.ClienteViewSet, basename='clientes')
router.register('cartoes', views.CartaoViewSet, basename='cartoes')
router.register('contas', views.ContaViewSet, basename='contas')
router.register('enderecos', views.EnderecoViewSet, basename='endereco')
urlpatterns = router.urls