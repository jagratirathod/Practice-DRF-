from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.generics  import ListCreateAPIView
from . models import *
from .serializers import *

# Create your views here.

def test_n(request):
    return HttpResponse("test...........")


class StudentView(ListCreateAPIView):
    # queryset =  Student.student.all()
    queryset =  Student.stud.get_stu_roll_range(101,103)
    serializer_class = DetailStudentSerializer
