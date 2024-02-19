from . serializers import *
from rest_framework import status
from . models import *
from rest_framework.response import Response
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema



# Create your views here.

def test(request):
    return HttpResponse("This is for testing api")


class StudentAPI(APIView):
    def get(self, request, pk=None):
        id = pk
        if id is not None:
            stu = Student.objects.get(id=id)
            serializer = StudentDetailsSerializer(stu)
            return Response(serializer.data)

        stu = Student.objects.all()
        serializer = StudentDetailsSerializer(stu,many=True)
        return Response(serializer.data)
    
    @swagger_auto_schema(request_body=StudentDetailsSerializer)
    def post(self, request):
        serializer = StudentDetailsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Data Created'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)
    
    @swagger_auto_schema(request_body=StudentDetailsSerializer)
    def put(self,request,pk=None):
        id = pk
        stu = Student.objects.get(pk=id)
        serializer = StudentDetailsSerializer(stu , data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Complete Data Updated'})
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


    @swagger_auto_schema(request_body=StudentDetailsSerializer)
    def patch(self, request ,pk =None):
        id=pk
        stu = Student.objects.get(id=id)
        serializer = StudentDetailsSerializer(stu , request.data)
        if serializer.is_valid():
            serializer.save()
            return  Response({'msg':'Patial data is updated'})
        return Response(serializer.error)
    
    def destroy(self,pk=None):
        id = pk 
        stu = Student.objects.get(id=id)
        stu.delete()
        return Response({'msg':'Data Delete'})     


