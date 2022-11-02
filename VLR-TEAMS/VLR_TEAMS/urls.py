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
urlpatterns = [
    path('', DefaultView.as_view()),
    path('admin/', admin.site.urls),
    #LOGIN
    path("accounts/", include("django.contrib.auth.urls")),

    #TEAM
    path('teams/',TeamListView.as_view(), name="team-list"),
    path('teams/<int:pk>/', TeamListViewDetail.as_view(), name='team-detail'),
    path('teams/add/', TeamCreateView.as_view(), name='team-add'),
    path('teams/<int:pk>/edit', TeamUpdateView.as_view(), name='team-update'),
    path('teams/<int:pk>/delete', TeamDeleteView.as_view(), name='team-delete'),

    #CLIENTES
    path('clients/', ClientListView.as_view(), name="client-list"),
    path('clients/<int:pk>/', ClientDetailView.as_view(), name="client-detail"),
    path('register/', ClientCreateView.as_view(), name='clients-add'),
    path('clients/<int:pk>/edit', ClientUpdateView.as_view(), name='clients-update'),
    path('clients/<int:pk>/delete', ClientDeleteView.as_view(), name='clients-delete'),

    #DIRECTIVOS
    path('directivos/', DirectivoListView.as_view(), name="directivo-list"),
    path('directivos/<int:pk>/', DirectivoDetailView.as_view(), name="directivo-detail"),
    path('directivos/add/', DirectivoCreateView.as_view(), name='directivo-add'),
    path('directivos/<int:pk>/edit', DirectivoUpdateView.as_view(), name='directivo-update'),
    path('directivos/<int:pk>/delete', DirectivoDeleteView.as_view(), name='directivo-delete'),

    #JUGADORES
    path('players/', PlayerListView.as_view(), name="player-list"),
    path('players/<int:pk>/', PlayerDetailView.as_view(), name="player-detail"),
    path('players/add/', PlayerCreateView.as_view(), name='player-add'),
    path('players/<int:pk>/edit', PlayerUpdateView.as_view(), name='player-update'),
    path('players/<int:pk>/delete', PlayerDeleteView.as_view(), name='player-delete'),


    #ENTRENADORES
    path('coaches/', CoachListView.as_view(), name="coach-list"),
    path('coaches/<int:pk>/', CoachDetailView.as_view(), name="coach-detail"),
    path('coaches/add/', CoachCreateView.as_view(), name='coach-add'),
    path('coaches/<int:pk>/edit', CoachUpdateView.as_view(), name='coach-update'),
    path('coaches/<int:pk>/delete', CoachDeleteView.as_view(), name='coach-delete'),

    #ANUNCIOS
    path('anuncios/', AnuncioListView.as_view(), name="anuncios-list"),
    path('anuncios/<int:pk>/', AnuncioDetailView.as_view(), name="anuncios-detail"),
    path('anuncios/add/', AnuncioCreateView.as_view(), name='anuncios-add'),
    path('anuncios/<int:pk>/edit', AnuncioUpdateView.as_view(), name='anuncios-update'),
    path('anuncios/<int:pk>/delete', AnuncioDeleteView.as_view(), name='anuncios-delete'),
]
