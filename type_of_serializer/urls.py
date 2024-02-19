from django.urls import path
from. import views

urlpatterns = [
    path('',views.test),
    path('create_person/',views.CreatePerson.as_view()),
    path('create_person/<int:id>/',views.CreatePerson.as_view()),
    path('list_person/',views.PersonList.as_view()),


]   

