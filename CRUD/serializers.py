from rest_framework import  serializers
from . models import *


class StudentDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('id','roll','name','city')

