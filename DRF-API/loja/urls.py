from cgitb import lookup
from django.urls import path, include
from . import views
from rest_framework_nested import routers   

router = routers.DefaultRouter()
router.register('categorias', views.CategoriaViewSet)
router.register('produtos', views.ProdutoViewSet, basename='produtos')

produto_router = routers.NestedDefaultRouter(router, 'produtos', lookup='produtos')
produto_router.register('avaliacoes', views.AvaliacaoViewSet, basename='avaliacoes')

urlpatterns = router.urls + produto_router.urls
# urlpatterns = [
#     path('produtos/', views.ListarProduto.as_view()),
#     path('avaliacoes/', views.ListarAvaliacao.as_view()),
#     path('produtos/<int:pk>/', views.ProdutoDetalhe.as_view()),
#     path('produtos/listar_clientes/', views.ListarCliente.as_view()),
#     path('produtos/listar_pedidos/', views.ListarPedido.as_view()),
#     path('produtos/listar_pedidos/<int:id>', views.PedidoDetalhe.as_view()),
#     path('produtos/listar_clientes/<int:id>', views.ClienteDetalhe.as_view())
    
# ]