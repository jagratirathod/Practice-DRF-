"""
URL configuration for practice_drf project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from pass_context_serlizer.views import *
from nested_serializer.views import *
from serializer_method_field.views import *


router = routers.DefaultRouter()
router.register(r'post', PostViewSet),
router.register(r'songs', SongView, basename='song'),
router.register(r'singers', SingerView,basename='singer'),
router.register(r'student', StudentView)


urlpatterns = [
    # admin 
    path('admin/', admin.site.urls),

    # router
    path('', include(router.urls)),

    path('pass_context/',include('pass_context_serlizer.urls')),
    path('crud/',include('CRUD.urls')),
    path('api/',include('signup_login_api.urls')),
    path('valid/',include('api_validation.urls')),
    path('nested/',include('nested_serializer.urls')),
    path('method/',include('serializer_method_field.urls')),
    path('model_manager/',include('model_manager.urls')),
    path('model_inheritance/',include('model_inheritance.urls')),
    path('management_command/',include('management_command.urls')),
    path('pagin/',include('pagination_app.urls')),
    path('oauth2_auth/',include('oauth2_authentication.urls')),

    
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),

]
