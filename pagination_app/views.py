from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.generics import ListCreateAPIView
from . models import *
from . serializers import *
from .paginations import CustomPagination

from oauth2_provider.contrib.rest_framework import OAuth2Authentication, TokenHasReadWriteScope

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.

def test(request):
    return HttpResponse("test...........")

class StudentListCreate(ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    pagination_class = CustomPagination

    # authentication_classes = [TokenAuthentication]    
    # permission_classes = [IsAuthenticated]

    # authentication_classes = [OAuth2Authentication]
    # permission_classes = [TokenHasReadWriteScope]   

