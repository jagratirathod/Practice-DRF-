from rest_framework import serializers
from django.contrib.auth.models import User


class RegisterSerializer(serializers.Serializer):
        email = serializers.EmailField()
        phone_number = serializers.IntegerField()


class LoginSerializer(serializers.Serializer):
    phone_number = serializers.IntegerField()

