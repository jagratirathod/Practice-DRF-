from django.urls import path
from. import views

urlpatterns = [
    path('',views.test),
    path('student/',views.StudentAPI.as_view()),
    path('student/<int:pk>/',views.StudentAPI.as_view())
]   

