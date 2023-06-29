from django.urls import path
from. import views

urlpatterns = [
        path('',views.BlogView.as_view()),
        path('author/',views.AuthorView.as_view()),
        path('entry/',views.EntryView.as_view()),

]   

