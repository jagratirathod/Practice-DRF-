from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.generics import ListCreateAPIView
from . models import *
from . serializers import *
from .paginations import CustomPagination


# Create your views here.

def test(request):
    return HttpResponse("test...........")

class StudentListCreate(ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    pagination_class = CustomPagination
