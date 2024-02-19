from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from .serializer import SignupUserSerializer , LoginUserSerializer
from rest_framework.response import Response
from django.contrib.auth.models import User
from oauth2_provider.models import  Application
import requests
import json
from practice_drf.settings import HOSTNAME
from drf_yasg.utils import swagger_auto_schema


# Create your views here.


def test(request):
    return HttpResponse("test...........")


class SignupView(APIView):
    @swagger_auto_schema(request_body=SignupUserSerializer)

    def post(self , request):
        serializer = SignupUserSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()

            user =  serializer.data
            user = User.objects.get(email=user['email'])

            if Application.objects.filter(user=user).exists():
                app = Application.objects.filter(user=user).last()
            else:

                app = Application(   
                        user=user,
                        authorization_grant_type="password",
                        client_type="confidential",
                        name=user.username,
                        redirect_uris = HOSTNAME
                    )

                auth_data = {
                    "username": request.data.get('username'),
                    "password": request.data.get('password'),
                    "grant_type": "password",
                    "client_id": app.client_id,
                    "client_secret": app.client_secret,
                }
                app.save()
                token_response = requests.post(HOSTNAME + "o/token/",data=auth_data)

                access_token = token_response.json()['access_token']
                refresh_token = token_response.json()['refresh_token']
                return Response(
                    {
                        "access": access_token,
                        "refresh": refresh_token,
                    }
                )
        else:
            return Response("User Already Exists")
        

# pip install django-cors-headers
# pip install django-oauth-toolkit
# python manage.py migrate

  

class LoginView(APIView):
    @swagger_auto_schema(request_body=LoginUserSerializer)
    def post(self, request):
        email = self.request.data["email"]
        password = self.request.data["password"]
        user = User.objects.get(email=email)
        user.check_password(password)
        if user:
            serializer = LoginUserSerializer(user)
            return Response(serializer.data)
        return Response("You have not signed up! Please sign up first.")
