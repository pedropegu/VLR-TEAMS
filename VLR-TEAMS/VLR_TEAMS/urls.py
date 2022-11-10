"""VLR_TEAMS URL Configuration

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
from django.urls import path
from VLR_APP.views import *
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from VLR_APP.api import *


urlpatterns = [
    #VLR_APP
    path('', include('VLR_APP.urls')),
    #ADMIN
    path('admin/', admin.site.urls),
    #LOGIN
    path("accounts/", include("django.contrib.auth.urls")),
    #API
    path('api/', include(api.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
