"""myapi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf.urls import url
from django.urls import path, include
from myapi.core import views
from myapi.api import UserAPI
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework import routers
from .core import views

router = routers.DefaultRouter()
router.register('api/events', views.CrearEventoViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/create-user/', UserAPI.as_view(), name='api_create_user'),
    path('api/api-auth/', obtain_auth_token, name='api_token_auth'),
    path('api/events/', views.EventList.as_view(), name = 'event_list'),
    path('api/events/<int:crearevento_id>', views.EventDetails.as_view(), name = 'details_event_list'),
    path('', include(router.urls))
]
