from django.shortcuts import render
from django.http import HttpResponse
from.models import *
from .serializers import *
from rest_framework import viewsets


# Create your views here.

def test2(request):
    return HttpResponse("test...........")


class StudentView(viewsets.ModelViewSet):
    queryset =  Student.objects.all()
    serializer_class = StudentSerializer

