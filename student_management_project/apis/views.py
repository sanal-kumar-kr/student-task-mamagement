from django.shortcuts import render  
from rest_framework import generics
from .models import users,Task
from .serializers import StudentSerializer,TaskSerilizer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated]) 
def students_list(request):
    if not request.user.is_superuser:  
        return Response(
            {"detail": "You do not have permission to access this resource."},
            status=status.HTTP_403_FORBIDDEN
        )
    if request.method == 'GET':
        user = users.objects.exclude(is_superuser=1)
        serializer = StudentSerializer(user, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET','PUT', 'DELETE'])
@permission_classes([IsAuthenticated]) 
def student_management(request,pk):
    if not request.user.is_superuser:  
        return Response(
            {"detail": "You do not have permission to access this resource."},
            status=status.HTTP_403_FORBIDDEN
    )
    try:
        user = users.objects.get(pk=pk)
    except users.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = StudentSerializer(user)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = StudentSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



@api_view(['GET','POST'])
@permission_classes([IsAuthenticated]) 

def add_task(request):
    if not request.user.is_superuser:  
        return Response(
            {"detail": "You do not have permission to access this resource."},
            status=status.HTTP_403_FORBIDDEN
    )
    if request.method == 'POST':
        serializer = TaskSerilizer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated]) 

def task_list(request):
    if not request.user.is_superuser:  
        return Response(
            {"detail": "You do not have permission to access this resource."},
            status=status.HTTP_403_FORBIDDEN
    )
    if request.method == 'GET':
        tasks = Task.objects.all()
        serializer = TaskSerilizer(tasks, many=True)
        return Response(serializer.data)




@api_view(['GET','PUT','DELETE'])
@permission_classes([IsAuthenticated]) 
def task_management(request,pk):
    if not request.user.is_superuser:  
        return Response(
            {"detail": "You do not have permission to access this resource."},
            status=status.HTTP_403_FORBIDDEN
    )
    try:
        task = Task.objects.get(pk=pk)
    except users.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = TaskSerilizer(task)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = TaskSerilizer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET','POST','PUT','DELETE'])
@permission_classes([IsAuthenticated]) 
def student(request):
    if request.method == 'GET':
        tasks = Task.objects.filter(student=request.user.id)
        serializer = TaskSerilizer(tasks, many=True)
        return Response(serializer.data)
  

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated]) 
def update_task(request, pk):
    try:
        task = Task.objects.get(pk=pk)
    except Task.DoesNotExist: 
        return Response({"detail": "Task not found."}, status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = TaskSerilizer(task)
        return Response(serializer.data)
    elif request.method == 'PUT':
        if 'status' not in request.data:
            return Response(
                {"detail": "The 'status' field is required for updating."},
                status=status.HTTP_400_BAD_REQUEST
            )
        task.status = request.data['status']  
        task.save()
        return Response({"detail": "Task status updated successfully."}, status=status.HTTP_200_OK)
    return Response({"detail": "Method not allowed."}, status=status.HTTP_405_METHOD_NOT_ALLOWED)




