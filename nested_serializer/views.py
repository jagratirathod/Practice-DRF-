from django.shortcuts import render
from.models import *
from .serializers import *
from rest_framework.generics  import ListAPIView , CreateAPIView
from django.http import HttpResponse
from rest_framework import viewsets


# Create your views here.

def test1(request):
    return HttpResponse("test...........")


class SongView(viewsets.ModelViewSet):
    queryset =  Song.objects.all()
    serializer_class = SongSerializer

class SingerView(viewsets.ModelViewSet):
    queryset =  Singer.objects.all()
    serializer_class = SingerSerializer
