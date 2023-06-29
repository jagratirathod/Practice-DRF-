from . serializers import *
from rest_framework import status
from . models import *
from rest_framework.response import Response
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView



# Create your views here.

def test(request):
    return HttpResponse("test...........")


class StudentAPI(APIView):
    def get(self, request, pk=None):
        id = pk
        if id is not None:
            stu = Student.objects.get(id=id)
            serializer = StudentSerializer(stu)
            return Response(serializer.data)

        stu = Student.objects.all()
        serializer = StudentSerializer(stu,many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Data Created'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)
    
    def put(self,request,pk=None):
        id = pk
        stu = Student.objects.get(pk=id)
        serializer = StudentSerializer(stu , data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Complete Data Updated'})
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request ,pk =None):
        id=pk
        stu = Student.objects.get(id=id)
        serializer = StudentSerializer(stu , request.data)
        if serializer.is_valid():
            serializer.save()
            return  Response({'msg':'Patial data is updated'})
        return Response(serializer.error)
    
    def destroy(self,pk=None):
        id = pk 
        stu = Student.objects.get(id=id)
        stu.delete()
        return Response({'msg':'Data Delete'})     


