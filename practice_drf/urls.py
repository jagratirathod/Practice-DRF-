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
from django.urls import path, include , re_path
from rest_framework import routers
from pass_context_serlizer.views import *
from nested_serializer.views import *
from serializer_method_field.views import *

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# router = routers.DefaultRouter()
# router.register(r'post', PostViewSet),
# router.register(r'songs', SongView, basename='song'),
# router.register(r'singers', SingerView,basename='singer'),
# router.register(r'student', StudentView)


# swagger - 
schema_view = get_schema_view(
    openapi.Info(
        title="Your API",
        default_version='v1',
        description="API Description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@yourdomain.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)



urlpatterns = [
    # admin 
    path('admin/', admin.site.urls),

    # swagger -
    re_path(r'^swagger(?P<format>\.json|\.yaml)$',
            schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger',
            cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc',cache_timeout=0), name='schema-redoc'),

    # router
    # path('', include(router.urls)),

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
    path('simple_jwt/',include('app_simple_jwt.urls')),
    path('send_otp/',include('send_otp.urls')),
    path('type_seri/',include('type_of_serializer.urls')),

    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),


]
