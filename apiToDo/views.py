from django.http.response import HttpResponse
from django.shortcuts import render
from rest_framework import serializers
from .serializers import TodoSerializer
from .models import ToDo

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


# Create your views here.

def home(request):
     return HttpResponse('<center><h1 style="background-color:powderblue;">Welcome</h1></center>')


@api_view(['GET'])
def todoList(request):
     queryset = ToDo.objects.all()
     
     serializer =TodoSerializer(queryset, many = True)
     return Response(serializer.data)
     
     
@api_view(['POST'])
def todoListCreate(request):
     serializer = TodoSerializer(data = request.data)
     if serializer.is_valid():
          serializer.save()
     return Response(serializer.data)

@api_view(['GET','POST'])
def toDo_list(request):
     
     if request.method == 'GET':
          queryset = ToDo.objects.all()
          serializer =TodoSerializer(queryset, many = True)
          return Response(serializer.data)
     elif request.method == 'POST':
          serializer = TodoSerializer(data = request.data)
          if serializer.is_valid():
               serializer.save()
               return Response(serializer.data,status=status.HTTP_201_CREATED)
          return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
     