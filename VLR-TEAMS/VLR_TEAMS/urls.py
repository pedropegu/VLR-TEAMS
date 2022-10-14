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

urlpatterns = [
    path('admin/', admin.site.urls),
    path('teams/',TeamListView.as_view(), name="team-list"),
    path('teams/<int:pk>/', TeamListViewDetail.as_view(), name='team-detail'),
    path('clients/', ClientListView.as_view(), name="client-list"),
    path('clients/<int:pk>/', ClientDetailView.as_view(), name="client-detail"),
    path('directivos/', DirectivoListView.as_view(), name="directivo-list"),
    path('directivos/<int:pk>/', DirectivoDetailView.as_view(), name="directivo-detail"),
    path('players/', PlayerListView.as_view(), name="player-list"),
    path('players/<int:pk>/', PlayerDetailView.as_view(), name="player-detail"),
    path('coaches/', CoachListView.as_view(), name="coach-list"),
    path('coaches/<int:pk>/', CoachDetailView.as_view(), name="coach-detail"),
    path('anuncios/', AnuncioListView.as_view(), name="anuncios-list"),
    path('anuncios/<int:pk>/', AnuncioDetailView.as_view(), name="anuncios-detail"),
]
