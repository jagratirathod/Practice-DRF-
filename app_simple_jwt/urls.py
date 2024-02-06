from django.urls import path
from. import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path('', views.SignIn.as_view()),
    path('refresh_token/', views.CreateRefreshToken.as_view()),

    # configure simple JWT -
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]   

