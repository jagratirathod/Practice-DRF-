from django.shortcuts import render
from . serializers import *
from rest_framework import status
from . models import *
from rest_framework.response import Response
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.parsers import JSONParser, MultiPartParser

# Create your views here.


class SignupApi(APIView):
    #     def post(self,request):
    #         serializer = UserSerializer(data=request.data)
    #         if serializer.is_valid():
    #             serializer.save()
    #             return Response(serializer.data)

    # with token - # settings.py -> installed_app -    'rest_framework.authtoken'  then migrate

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            user = User.objects.get(username=serializer.data['username'])
            if user:
                token, created = Token.objects.get_or_create(user=user)
                return Response({
                    'token': token.key,
                    'user_id': user.pk,
                    'email': user.email
                })
            return Response(serializer.data)
        else:
            return Response("User Already Exists")


# not working
class Login(APIView):
    parser_classes = (JSONParser, MultiPartParser)

    def post(self, request):
        email = request.data["email"]
        password = request.data["password"]
        user = User.objects.filter(email=email)
        if user.check_password(str(password)):
            return Response("Successfully Login")
        return Response("Invalid user")

    def post(self, request):
        email = request.data["email"]
        password = request.data["password"]
        user = User.objects.filter(email=email)
        if user.check_password(password):
            token, created = Token.objects.get_or_create(user=user)
            return Response({
                    'token': token.key,
                    'user_id': user.pk,
                    'email': user.email
                })

            # return Response("Successfully Login")
        return Response("Login Failed !")


class EditProfile(APIView):
    def post(self,request):
        email = request.data["email"]
        firstname = request.data["first_name"]
        lastname = request.data["last_name"]
        if User.objects.filter(email = email).exists():
            user = User.objects.get(email = email)
            user.first_name = firstname
            user.last_name = lastname
            user.save()
            return Response("Successfully Edit !")
        else:
            return Response("Invalid user")



            
