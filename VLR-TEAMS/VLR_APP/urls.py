from django.contrib import admin
from django.urls import path
from VLR_APP.views import *
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', DefaultView.as_view(), name="home"),
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
    path('clients/<int:pk>/edit', ClientUpdateView.as_view(), name='client-update'),
    path('clients/<int:pk>/delete', ClientDeleteView.as_view(), name='client-delete'),

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