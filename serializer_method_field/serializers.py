from rest_framework import serializers
from.models import *
import datetime


class StudentSerializer(serializers.Serializer):                                           #  using  serializer.serializer                            
    email =  serializers.EmailField()
    first_name =  serializers.CharField()
    last_name =  serializers.CharField()
    city =  serializers.CharField()
    phone =  serializers.IntegerField()
    
    current_time = serializers.SerializerMethodField()                                      # first way
    
    def get_current_time(self, obj):
        time = datetime.datetime.now()
        return time
    
    # my_name = serializers.SerializerMethodField('get_full_name')                          # second way
    
#     def get_full_name(self, obj):
#         name = (obj.first_name + " " + obj.last_name).upper()
#         return name


#     def create(self, validated_data):
#         return Student.objects.create(**validated_data)

# class StudentSerializer(serializers.ModelSerializer):                                        # using model serializer 
#     full_name = serializers.SerializerMethodField()

#     def get_full_name(self, obj):
#         name = (obj.first_name + " " + obj.last_name).upper()
#         return name

#     class Meta:
#         model = Student
#         fields = ('email', 'first_name', 'last_name','city','phone','full_name')