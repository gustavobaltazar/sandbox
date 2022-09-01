from django.urls import path
from . import views

urlpatterns = [
    path('produtos/', views.listar_produtos),
    path('produtos/<int:id>/', views.produto_detalhe),
    path('produtos/listar_clientes/', views.listar_clientes),
]