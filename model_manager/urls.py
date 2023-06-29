from django.urls import path
from. import views

urlpatterns = [
    path('',views.test_n),
    path('stud/',views.StudentView.as_view()),

]
