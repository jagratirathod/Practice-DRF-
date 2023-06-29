from rest_framework import  serializers
from . models import *

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['author','title']

    def create(self, validated_data):
        author=self.context['author']
        title=self.context['title']
        post=Post.objects.create(author=author,title=title)
        return post
    


   


    

