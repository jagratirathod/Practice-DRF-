from rest_framework import serializers
from.models import *
import datetime

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model=Blog
        fields=['name','tagline']

    def validate_name(self,attrs):                                                     # Field  level validation
        if attrs[0].lower()!='r':      
            raise serializers.ValidationError('Name should be start with R')
        return attrs
 

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Author
        fields=['name', 'email' , 'city' , 'phone']

    def validate(self, data):                                                           # Object level validation 
        phone = data.get('phone')
        city = data.get('city')
        if len(str(phone))!=10  or  city.lower() == 'ranchi':
            raise serializers.ValidationError('Mobile should be of  10 digit')
        return data
    


def city_should_not_indore(value):                                                       # Validator
    if  value.lower()=='indore':      
        raise serializers.ValidationError('city should not Indore !')
    return value

class EntrySerializer(serializers.Serializer):
    name = serializers.CharField()
    city = serializers.CharField(validators = [city_should_not_indore])
    
    class Meta:
        fields = '__all__'

    def create(self, validated_data):
        return Entrys.objects.create(**validated_data)



        
    
