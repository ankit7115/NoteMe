# from django.shortcuts import render
# from django.http import HttpResponse
# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import todoSerializer
from .models import Todo
from rest_framework import status

@api_view(['GET'])
def getTodos(request):
    todos = Todo.objects.all()
    serializer = todoSerializer(todos, many = True)
    return Response(serializer.data)


@api_view(['GET'])
def getTodo(request,pk):
    todo = Todo.objects.get(id = pk)
    serializer = todoSerializer(todo, many = False)
    return Response(serializer.data)

@api_view(['POST'])
def createTodo(request):
    data = request.data
    todo = Todo.objects.create(
        title = data['title'],
        body = data['body'],
    )
    serializer = todoSerializer(todo, many = False)
    return Response(serializer.data)

@api_view(['PUT'])
def updateTodo(request, pk):
    todo = Todo.objects.get(pk=pk)
    serializer = todoSerializer(todo, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def deleteTodo(request,pk):
    todo = Todo.objects.get(id = pk)
    todo.delete()
    return Response('Note Deleted!')
