from django.urls import path
from. import views

urlpatterns = [
    path('',views.test),
    path('stud/',views.StudentListCreate.as_view()),

]   

