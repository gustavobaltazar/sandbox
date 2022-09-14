from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter    

router = DefaultRouter()
router.register('avaliacoes', views.AvaliacaoViewSet, basename='Avaliacoes')

# urlpatterns = router.urls
urlpatterns = [
    path('produtos/', views.ListarProduto.as_view()),
    path('avaliacoes/', views.ListarAvaliacao.as_view()),
    path('produtos/<int:pk>/', views.ProdutoDetalhe.as_view()),
    path('produtos/listar_clientes/', views.ListarCliente.as_view()),
    path('produtos/listar_pedidos/', views.ListarPedido.as_view()),
    path('produtos/listar_pedidos/<int:id>', views.PedidoDetalhe.as_view()),
    path('produtos/listar_clientes/<int:id>', views.ClienteDetalhe.as_view())
    
]