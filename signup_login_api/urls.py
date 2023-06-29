from django.urls import path
from. import views

urlpatterns = [
    path('signup/',views.SignupApi.as_view()),
    path('login/',views.Login.as_view()),
    path('edit/',views.EditProfile.as_view()),

]   

