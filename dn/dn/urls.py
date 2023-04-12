"""dn URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.conf.urls import handler404, handler500
from . import views as core_views
from config import *

from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from inbox.views import Notify

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'notify', Notify)

urlpatterns = [
    path('<slug:pk>/api/', include(router.urls)),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # path('<slug:pk>/api/notify/', Notify, name="notify"),
    path("admin/", admin.site.urls),
    path("accounts/", include("allauth.urls")),

    path("", core_views.welcome, name="welcome"),
    path("profile/", core_views.profile, name="profile"),
    path("<slug:pk>/", core_views.rprofile, name="rprofile"),
    path("<slug:pk>/actions/", include("actions.urls")),
    path("<slug:pk>/inbox/", include("inbox.urls")),
]
