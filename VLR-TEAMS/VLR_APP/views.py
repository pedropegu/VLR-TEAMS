from django.shortcuts import render
from VLR_APP.models import *
from django.views.generic import *

# Create your views here.

#TEAMS
class TeamListView(ListView):
    model = team

class TeamListViewDetail(DetailView):
    queryset = team.objects.all()

#CLIENTES
class ClientListView(ListView):
    model = client
    template_name="VLR_APP/client_list.html"

class ClientDetailView(DetailView):
    queryset = client.objects.all()
    template_name="VLR_APP/client_detail.html"

#DIRECTIVOS
class DirectivoListView(ListView):
    model = directivo

class DirectivoDetailView(DetailView):
    queryset = directivo.objects.all()
    template_name="VLR_APP/directivo_detail.html"

#JUGADORES
class PlayerListView(ListView):
    model = player

class PlayerDetailView(DetailView):
    queryset = player.objects.all()
    template_name="VLR_APP/player_detail.html"

#ENTRENADORES
class CoachListView(ListView):
    model = coache

class CoachDetailView(DetailView):
    queryset = coache.objects.all()
    template_name="VLR_APP/coach_detail.html"

#ANUNCIOS
class AnuncioListView(ListView):
    model = anuncio

class AnuncioDetailView(DetailView):
    queryset = anuncio.objects.all()
    template_name="VLR_APP/anuncio_detail.html"
