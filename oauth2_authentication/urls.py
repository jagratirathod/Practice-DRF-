from django.urls import path
from. import views

urlpatterns = [
    path('test/',views.test),
    path('', views.SignupView.as_view()),
    path('login/', views.LoginView.as_view()),
]

  

