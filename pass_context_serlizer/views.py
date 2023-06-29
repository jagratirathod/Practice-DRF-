from django.shortcuts import render
from rest_framework import viewsets
from .serializers import PostSerializer
from . models import *
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse("test")

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    http_method_names = ['post','get' ]

    def get_serializer_context(self):
        context = super(PostViewSet, self).get_serializer_context()
        context.update({"author":self.request.user })
        context.update({"title": self.request.POST.get("title")})
        return context