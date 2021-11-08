from django.http.response import HttpResponse
from django.shortcuts import render
from rest_framework import serializers
from .serializers import TodoSerializer
from .models import ToDo

from rest_framework.decorators import api_view
from rest_framework.response import Response


# Create your views here.

def home(request):
     return HttpResponse('<center><h1 style="background-color:powderblue;">Welcome</h1></center>')


@api_view(['GET'])
def todoList(request):
     queryset = ToDo.objects.all()
     
     serializer =TodoSerializer(queryset, many = True)
     return Response(serializer.data)
     