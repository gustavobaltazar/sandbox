from django.contrib import admin

from .models import Courses

class CursosDisplay(admin.ModelAdmin):
    list_display = ('nome_curso_bosch', 'nome_curso_senai')

admin.site.register(Courses, CursosDisplay)

# Register your models here.
