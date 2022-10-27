

from django.shortcuts import render
from VLR_APP.models import *
from django.views.generic import *
from django.urls import reverse_lazy
from .forms import *
from .forms import *
# Create your views here.

#DEFAULT VIEW

def DefaultView(request):
    return render(request, 'VLR_APP/default.html', {})


#TEAMS
class TeamListView(ListView):
    model = Team
class TeamListViewDetail(DetailView):
    queryset = Team.objects.all()
class TeamUpdateView(UpdateView):
    queryset = Team.objects.all()
    fields=["name","foundation_date","city","info"]
class TeamCreateView(CreateView):
    model = Team
    fields=["name","foundation_date","city","info"]
class TeamDeleteView(DeleteView):
    model = Team
    success_url = reverse_lazy('team-list')


#CLIENTES
class ClientListView(ListView):
    model = User
    template_name="VLR_APP/client_list.html"
class ClientDetailView(DetailView):
    queryset = User.objects.all()
    template_name="VLR_APP/client_detail.html"
class ClientUpdateView(UpdateView):
    queryset = User.objects.all()
    fields=["username","email","first_name","last_name","fnac","description"]
    template_name="VLR_APP/client_form.html"
class ClientCreateView(CreateView):
    model = User
    form_class = SignUpForm  
    template_name="VLR_APP/client_form.html"
class ClientDeleteView(DeleteView):
    model = User
    template_name="VLR_APP/client_confirm_delete.html"
    success_url = reverse_lazy('client-list')


#DIRECTIVOS
class DirectivoListView(ListView):
    model = Directivo
class DirectivoDetailView(DetailView):
    queryset = Directivo.objects.all()
    template_name="VLR_APP/directivo_detail.html"
class DirectivoUpdateView(UpdateView):
    queryset = Directivo.objects.all()
    fields=["client","team","position","experience"]
class DirectivoCreateView(CreateView):
    model = Directivo
    fields=["client","team","position","experience"]
class DirectivoDeleteView(DeleteView):
    model = Directivo
    success_url = reverse_lazy('directivo-list')


#JUGADORES
class PlayerListView(ListView):
    model = Player
class PlayerDetailView(DetailView):
    queryset = Player.objects.all()
    template_name="VLR_APP/player_detail.html"
class PlayerUpdateView(UpdateView):
    queryset = Player.objects.all()
    fields=["client","team","riot","primary_rol","horarios","experience"]
class PlayerCreateView(CreateView):
    model = Player
    fields=["client","team","riot","primary_rol","horarios","experience"]
class PlayerDeleteView(DeleteView):
    model = Player
    success_url = reverse_lazy('player-list')


#ENTRENADORES
class CoachListView(ListView):
    model = Coache
class CoachDetailView(DetailView):
    queryset = Coache.objects.all()
    template_name="VLR_APP/coach_detail.html"
class CoachUpdateView(UpdateView):
    queryset = Coache.objects.all()
    fields=["client","team","experience"]
class CoachCreateView(CreateView):
    model = Coache
    fields=["client","team","experience"]
class CoachDeleteView(DeleteView):
    model = Coache
    success_url = reverse_lazy('coach-list')


#ANUNCIOS
class AnuncioListView(ListView):
    model = Anuncio
class AnuncioDetailView(DetailView):
    queryset = Anuncio.objects.all()
    template_name="VLR_APP/anuncio_detail.html"
class AnuncioUpdateView(UpdateView):
    queryset = Anuncio.objects.all()
    fields=["title","message"]
class AnuncioCreateView(CreateView):
    model = Anuncio
    fields=["title","message","directivo"]
class AnuncioDeleteView(DeleteView):
    model = Anuncio
    success_url = reverse_lazy('anuncios-list')