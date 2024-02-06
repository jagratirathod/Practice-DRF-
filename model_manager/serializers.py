from rest_framework import serializers
from .models import *


class DetailStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['name', 'roll','email']