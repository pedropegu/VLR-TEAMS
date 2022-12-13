

from django.shortcuts import render
from VLR_APP.models import *
from django.views.generic import *
from django.urls import reverse_lazy
from .forms import *
from django.http import HttpResponseRedirect
#AUTORIZACIÓN
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import UserPassesTestMixin
from django.db.models import Q
from django.contrib.auth.forms import AuthenticationForm
# Create your views here.

#DEFAULT VIEW

class DefaultView(TemplateView):
    template_name="index.html"
    model = Team

class MarketplaceListView(ListView):
    model = Player
    template_name="VLR_APP/marketplace.html"

class search(ListView):
    model = User
    template_name="VLR_APP/search.html"
    def get_queryset(self):
        query = self.request.GET.get("q")
        object_list=User.objects.filter(Q(username__in=[query]))
        return object_list
#TEAMS <--TERMINADO-->
class TeamListView(ListView):
    model = Team
class TeamListViewDetail(DetailView):
    queryset = Team.objects.all()

class TeamUpdateView(UserPassesTestMixin,UpdateView):
    queryset = Team.objects.all()
    fields=["name","foundation_date","city","info"]

    def test_func(self): #COMPROBAR SI ES PROPIETARIO (ERROR 403: FORBIDDEN)
        try:
            return self.request.user.directivo.team==Team.objects.get(pk=self.kwargs.get("pk"))
        except:
            return False

class TeamCreateView(UserPassesTestMixin,CreateView):
    model = Team
    fields=["name","foundation_date","city","info"]

    def test_func(self): #COMPROBAR SI ES DIRECTIVO (ERROR 403: FORBIDDEN)
        try:
            if self.request.user.directivo:
                return True
        except:
            return False

class TeamDeleteView(UserPassesTestMixin,DeleteView):
    model = Team
    success_url = reverse_lazy('vlr:teams-list')

    def test_func(self): #COMPROBAR SI ES PROPIETARIO (ERROR 403: FORBIDDEN)
        try:
            return self.request.user.directivo.team==Team.objects.get(pk=self.kwargs.get("pk"))
        except:
            return False
#CLIENTES <--TERMINADOS-->
class ClientListView(ListView):
    model = User
    template_name="VLR_APP/client_list.html"
class ClientDetailView(DetailView):
    queryset = User.objects.all()
    template_name="VLR_APP/client_detail.html"
class ClientUpdateView(UserPassesTestMixin,UpdateView):
    queryset = User.objects.all()
    template_name="VLR_APP/client_edit.html"
    fields=["username","email","first_name","last_name","fnac","description","image"]
    def test_func(self): #COMPROBAR SI ES EL USUARIO (ERROR 403: FORBIDDEN)
        try:
            return User.objects.get(pk=self.request.user.pk)==User.objects.get(pk=self.kwargs.get("pk"))
        except:
            return False

class ClientCreateView(CreateView):
    model = User
    form_class = SignUpForm  
    template_name="VLR_APP/client_form.html"

class ClientDeleteView(UserPassesTestMixin,DeleteView):
    model = User
    template_name="VLR_APP/client_confirm_delete.html"
    success_url = reverse_lazy('vlr:client-list')
    def test_func(self): #COMPROBAR SI ES EL USUARIO (ERROR 403: FORBIDDEN)
        try:
            return User.objects.get(pk=self.request.user.pk)==User.objects.get(pk=self.kwargs.get("pk"))
        except:
            return False


#DIRECTIVOS
class DirectivoListView(ListView):
    model = Directivo
class DirectivoDetailView(DetailView):
    queryset = Directivo.objects.all()
    template_name="VLR_APP/directivo_detail.html"
class DirectivoUpdateView(UpdateView):
    queryset = Directivo.objects.all()
    fields=["position","experience"]
class DirectivoCreateView(CreateView):
    model = Directivo
    fields=["position","experience"]
class DirectivoDeleteView(DeleteView):
    model = Directivo
    success_url = reverse_lazy('directivo-list')


#JUGADORES
class PlayerListView(ListView):
    model = Player

class PlayerDetailView(DetailView):
    queryset = Player.objects.all()
    template_name="VLR_APP/player_detail.html"

class PlayerUpdateView(UserPassesTestMixin,UpdateView):
    queryset = Player.objects.all()
    fields=["riot","primary_rol","horarios","experience","searching"]
    success_url = reverse_lazy('vlr:players-list')
    def test_func(self): #COMPROBAR SI ES EL USUARIO (ERROR 403: FORBIDDEN)
        try:
            return Player.objects.get(pk=self.request.user.pk)==Player.objects.get(pk=self.kwargs.get("pk"))
        except:
            return False

class PlayerCreateView(LoginRequiredMixin,CreateView):
    model = Player
    fields=["riot","primary_rol","horarios","experience","searching"]
    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        obj.save()
        return HttpResponseRedirect(reverse_lazy('vlr:home'))

class PlayerDeleteView(UserPassesTestMixin,DeleteView):
    model = Player
    success_url = reverse_lazy('vlr:players-list')
    def test_func(self): #COMPROBAR SI ES EL USUARIO (ERROR 403: FORBIDDEN)
        try:
            return Player.objects.get(pk=self.request.user.pk)==Player.objects.get(pk=self.kwargs.get("pk"))
        except:
            return False


#ENTRENADORES
class CoachListView(ListView):
    model = Coache
class CoachDetailView(DetailView):
    queryset = Coache.objects.all()
    template_name="VLR_APP/coach_detail.html"
class CoachUpdateView(UpdateView):
    queryset = Coache.objects.all()
    fields=["user","team","experience"]
class CoachCreateView(CreateView):
    model = Coache
    fields=["user","team","experience"]
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
