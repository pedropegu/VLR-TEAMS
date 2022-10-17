
from django.shortcuts import render
from VLR_APP.models import *
from django.views.generic import *
from django.urls import reverse_lazy
# Create your views here.

#DEFAULT VIEW
def DefaultView(request):
    return render(request, 'VLR_APP/default.html', {})


#TEAMS
class TeamListView(ListView):
    model = team
class TeamListViewDetail(DetailView):
    queryset = team.objects.all()
class TeamUpdateView(UpdateView):
    queryset = team.objects.all()
    fields=["name","foundation_date","city","info"]
class TeamCreateView(CreateView):
    model = team
    fields=["name","foundation_date","city","info"]
class TeamDeleteView(DeleteView):
    model = team
    success_url = reverse_lazy('team-list')


#CLIENTES
class ClientListView(ListView):
    model = client
    template_name="VLR_APP/client_list.html"
class ClientDetailView(DetailView):
    queryset = client.objects.all()
    template_name="VLR_APP/client_detail.html"
class ClientUpdateView(UpdateView):
    queryset = client.objects.all()
    fields=["user","fnac","description"]
class ClientCreateView(CreateView):
    model = client
    fields=["user","fnac","description"]
class ClientDeleteView(DeleteView):
    model = client
    success_url = reverse_lazy('Clients-list')


#DIRECTIVOS
class DirectivoListView(ListView):
    model = directivo
class DirectivoDetailView(DetailView):
    queryset = directivo.objects.all()
    template_name="VLR_APP/directivo_detail.html"
class DirectivoUpdateView(UpdateView):
    queryset = directivo.objects.all()
    fields=["client","team","position","experience"]
class DirectivoCreateView(CreateView):
    model = directivo
    fields=["client","team","position","experience"]
class DirectivoDeleteView(DeleteView):
    model = directivo
    success_url = reverse_lazy('directivos-list')


#JUGADORES
class PlayerListView(ListView):
    model = player
class PlayerDetailView(DetailView):
    queryset = player.objects.all()
    template_name="VLR_APP/player_detail.html"
class PlayerUpdateView(UpdateView):
    queryset = player.objects.all()
    fields=["client","team","riot","primary_rol","horarios","experience"]
class PlayerCreateView(CreateView):
    model = player
    fields=["client","team","riot","primary_rol","horarios","experience"]
class PlayerDeleteView(DeleteView):
    model = player
    success_url = reverse_lazy('player-list')


#ENTRENADORES
class CoachListView(ListView):
    model = coache
class CoachDetailView(DetailView):
    queryset = coache.objects.all()
    template_name="VLR_APP/coach_detail.html"
class CoachUpdateView(UpdateView):
    queryset = coache.objects.all()
    fields=["client","team","experience"]
class CoachCreateView(CreateView):
    model = coache
    fields=["client","team","experience"]
class CoachDeleteView(DeleteView):
    model = coache
    success_url = reverse_lazy('coach-list')


#ANUNCIOS
class AnuncioListView(ListView):
    model = anuncio
class AnuncioDetailView(DetailView):
    queryset = anuncio.objects.all()
    template_name="VLR_APP/anuncio_detail.html"
class AnuncioUpdateView(UpdateView):
    queryset = anuncio.objects.all()
    fields=["title","message"]
class AnuncioCreateView(CreateView):
    model = anuncio
    fields=["title","message","directivo"]
class AnuncioDeleteView(DeleteView):
    model = anuncio
    success_url = reverse_lazy('anuncios-list')