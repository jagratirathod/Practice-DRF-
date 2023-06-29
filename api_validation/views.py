from django.shortcuts import render
from.models import *
from .serializers import BlogSerializer , AuthorSerializer , EntrySerializer
from rest_framework.generics  import CreateAPIView

# Create your views here.


class BlogView(CreateAPIView):
    queryset =  Blog.objects.all()
    serializer_class = BlogSerializer

class AuthorView(CreateAPIView):
    queryset =  Author.objects.all()
    serializer_class = AuthorSerializer

class EntryView(CreateAPIView):
    queryset =  Entrys.objects.all()
    serializer_class = EntrySerializer
    
    
