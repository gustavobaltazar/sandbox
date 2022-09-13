from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter    

router = DefaultRouter()
router.register('avaliacoes', views.AvaliacaoViewSet, basename='Avaliacoes')

# urlpatterns = router.urls
urlpatterns = [
    path('produtos/', views.ProdutoListar.as_view()),
    path('avaliacoes/', views.listar_avaliacao),
    path('produtos/<int:pk>/', views.ProdutoDetalhe.as_view()),
    path('produtos/listar_clientes/', views.listar_clientes),
    path('produtos/listar_pedidos/', views.listar_pedidos),
    path('produtos/listar_pedidos/<int:id>', views.pedido_detalhe),
    path('produtos/listar_clientes/<int:id>', views.cliente_detalhe)
    
]