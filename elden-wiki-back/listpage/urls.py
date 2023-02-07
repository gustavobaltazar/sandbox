from django.urls import path    
from . import views

urlpatterns= [
    path('boss_show/', views.listpage),
    path('boss_show/list_bosses/', views.list_bosses)
]  