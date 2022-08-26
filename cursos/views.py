from django.shortcuts import render, HttpResponse, get_list_or_404, get_object_or_404
from .models import Courses

# Create your views here.

def index(request):
  cursos = Courses.objects.all()
  dados = { 
    'cursos': cursos
  }
  return render(request, 'index.html', dados)

# def get_courses(request):
#   data = Cursos.objects.all()
#   context = {
#     'data': data
#   }
#   return render(request, 'index.html', context)

def cursos(request, curso_id):
  curso = get_object_or_404(Courses, pk=curso_id)
  curso_a_ser_exibido = {
    'curso': curso
  }
  return render(request, 'curso.html', curso_a_ser_exibido)