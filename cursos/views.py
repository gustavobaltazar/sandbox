from django.shortcuts import render, HttpResponse
from .models import Courses

# Create your views here.

def index(request):
  return render(request, 'index.html')

# def get_courses(request):
#   data = Cursos.objects.all()
#   context = {
#     'data': data
#   }
#   return render(request, 'index.html', context)

def cursos(request):
  return render(request, 'curso.html')

def index(request):
  cursos = {
    1 : 'Smart Automation',
    2 : 'Mecatrônica',
    3 : 'Manufatura Digital',
    4 : 'Administração'
  }

  dados = {
    'nome_cursos' : cursos
  }
  return render(request, 'index.html', dados)