from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework  import status
from .models import Bosses
from .serializer import BossSerializer

def listpage(request):
    return render(request, 'index.html')

@api_view(['GET', 'POST'])
def list_bosses(request):
    if request.method == 'GET':
        queryset = Bosses.objects.all()
        serializer = BossSerializer(queryset, many=True) 
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = BossSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def boss_details(request, id):
    pass 
