from django.urls import path

from . import views

urlpatterns = [
  path("", views.index, name='index'),
  path("curso", views.cursos, name='curso'),

]