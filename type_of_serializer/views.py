from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from . serializer import  PersonSerializer 
from rest_framework.response import Response
from rest_framework import generics
from . models import Person
from drf_yasg.utils import swagger_auto_schema

# Create your views here.

def test(request):
    return HttpResponse("This is for testing api")


class CreatePerson(APIView):
    @swagger_auto_schema(request_body=PersonSerializer)
    def post(self,request):
        serializer = PersonSerializer(data = request.data)
        if serializer.is_valid(raise_exception=True):
            Person.objects.create(first_name = request.data['first_name'] , last_name = request.data['last_name'])
            return Response("Successfully created !")
        return Response("Invalid")
    

class PersonList(generics.ListCreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
   
    def create(self, request):
        person_serializer = PersonSerializer(data = request.data)
        person_serializer.is_valid(raise_exception=True)

        # first_name = serializer.validated_data['first_name']
        # last_name =  serializer.validated_data['last_name']
        # person = Person.objects.create(first_name=first_name, last_name=last_name)
        # return Response({"message": "Successfully Done!", "detail": {"first_name": first_name, "last_name": last_name}})

        person = Person.objects.create(**person_serializer.validated_data)
        return Response("Successfully Done")
