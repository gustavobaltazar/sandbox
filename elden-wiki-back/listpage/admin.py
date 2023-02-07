from django.contrib import admin
from . import models
from .models import Bosses

class BossList(admin.ModelAdmin):
    model = Bosses
    list_display = ['name', 'location']

admin.site.register(Bosses, BossList)
