from django.urls import path    
from . import views

urlpatterns= [
    path('boss_show/', views.listpage),
    path('boss_show/lists_bosses/', views.lista_bosses)
]  