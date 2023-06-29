from django.urls import path
from. import views

urlpatterns = [
    path('',views.test1),
    # path('song/',views.SongView.as_view()),
    # path('singer/',views.SingerView.as_view()),

]   

