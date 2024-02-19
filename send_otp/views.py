from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from . models import Profile
import random
from send_otp.mixins import MessHandler 
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import *
from drf_yasg.utils import swagger_auto_schema

# Create your views here.


def test(request):
    return HttpResponse("This is for testing api")


class RegisterAPI(APIView):
    @swagger_auto_schema(request_body=RegisterSerializer)

    def post(self,request):
        serializer = RegisterSerializer(data = request.data)
        if serializer.is_valid():
            email = serializer.validated_data.get('email')
            phone_number = serializer.validated_data.get('phone_number')
            username = email
            user = User.objects.create_user(username=username, email=email)
            Profile.objects.create(user=user, phone_number=phone_number)
            return Response("Successfully Registered")
        return Response("Already registerd")


class LoginAPI(APIView):
    @swagger_auto_schema(request_body=LoginSerializer)

    def post(self,request):
        serializer = LoginSerializer(data = request.data)
        if serializer.is_valid():
            phone_number = serializer.validated_data.get('phone_number')
            profile = Profile.objects.filter(phone_number = phone_number).last()

            if not profile:
                return Response("Phone number does not exists !")
            else:
                profile.otp = random.randrange(1000, 9999)
                profile.save()
                # message_handler = MessHandler.sent_otp_number(phone_number, profile.otp)
                return HttpResponse("Successfully send otp")
            


class Verify_otp(APIView):
    # localhost:8000/send_otp/verify_otp/8b223063-4c7a-4dc1-970e-f86157da8f6c/
    def post(self,request,uid):
        # uid = request.data.get("uid").strip()
        otp = request.data.get("otp").strip()
        # profile = Profile.objects.filter(otp = otp , uid = uid)
        profile = Profile.objects.get(uid = uid)
        if otp == profile.otp:
            return Response(f'Verified Users uid : {uid}  and  OTP -  {otp}')
        return Response("OTP not verified ")


