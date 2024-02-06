from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
import requests
from practice_drf.settings import HOSTNAME
from rest_framework.response import Response
from .serializer import  UserSerializer

# Create your views here.


class SignIn(APIView):
    def post(self,request):
        serializer = UserSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()

            auth_data = {
                "username" : request.data.get("username") ,
                "password" : request.data.get("password") ,
            }
            token = requests.post(HOSTNAME + "simple_jwt/api/token/", data=auth_data)
            access_token = token.json()['access']
            refresh_token = token.json()['refresh']
            return Response(
                {
                    "Access Token" : access_token ,
                    "Refresh Token" : refresh_token ,
                }
            )
        else:
            return HttpResponse("User already exists")
        

class CreateRefreshToken(APIView):
        def post(self, request):
                token_data = {
                        "refresh": request.data.get('refresh'),
                }
                token = requests.post(HOSTNAME + "simple_jwt/api/token/refresh/", data=token_data)
                access_token = token.json()['access']
                return Response({
                        'Access Token': access_token
                })
        