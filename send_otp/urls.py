from django.urls import path
from. import views

urlpatterns = [
    path('',views.test),
    path('register/', views.RegisterAPI.as_view() , name= 'register'),
    path('login/', views.LoginAPI.as_view() , name= 'login'),
    path('verify_otp/<uid>/', views.Verify_otp.as_view() , name= 'verify_otp'),
]   

