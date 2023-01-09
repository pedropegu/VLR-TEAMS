

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
from django.contrib.postgres.search import TrigramWordSimilarity
# Create your views here.

#DEFAULT VIEW

class DefaultView(TemplateView):
    template_name="index.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['anuncios']=Anuncio.objects.all().order_by('-date').values()[0:7]
        context['players']=Player.objects.all()[0:7]
        context['teams']=Team.objects.all()[0:7]
        context['directivos']=Directivo.objects.all()
        return context
class MarketplaceListView(ListView):
    model = Player
    template_name="VLR_APP/marketplace.html"
class search(ListView):
    model = User
    template_name="VLR_APP/search.html"
    def get_queryset(self):
        query = self.request.GET.get("q")
        object_list=User.objects.filter(Q(username__icontains=query))
        return object_list
class search_anuncios(ListView):
    model = Anuncio
    template_name="VLR_APP/search_ann.html"
    def get_queryset(self):
        query = self.request.GET.get("q")
        object_list= Anuncio.objects.annotate(similarity=TrigramWordSimilarity(query, 'title'), ).filter(similarity__gt=0.3).order_by('-similarity') | Anuncio.objects.annotate(similarity=TrigramWordSimilarity(query, 'message'), ).filter(similarity__gt=0.3).order_by('-similarity')
        return object_list
#TEAMS <--TERMINADO-->
class TeamListView(ListView):
    model = Team
class TeamListViewDetail(DetailView):
    queryset = Team.objects.all()
class TeamUpdateView(UserPassesTestMixin,UpdateView):
    model = Team
    fields = '__all__'
    template_name="VLR_APP/team_update.html"
    success_url = reverse_lazy('vlr:team-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["add"] = TeamAdd(prefix="add")
        context["players"] = Players.objects.all()
        context["directivos"] = Directivo.objects.filter(position='MANAGER')
        return context

    def post(self, request, *args, **kwargs):

        self.object = self.get_object()
        context = self.get_context_data(object=self.object)

        if "add" in request.POST:
            form = TeamAdd(request.POST, prefix="add")

            if len(User.objects.filter(username=form.data["add-añadir"]))!=0:
                pk=User.objects.filter(username=form.data["add-añadir"])[0].pk

                if len(Player.objects.filter(user=pk))!=0:
                    user = Player.objects.filter(user=pk)[0]
                    if not user.team:
                        user.team_id = Team.objects.filter(name=form.data["name"])[0].pk
                        user.searching = False
                        user.save()

                elif len(Directivo.objects.filter(user=pk))!=0:
                    user = Directivo.objects.filter(user=pk)[0]
                    if not user.team:
                        user.team_id = Team.objects.filter(name=form.data["name"])[0].pk
                        user.save()

            if len(User.objects.filter(username=form.data["add-eliminar"]))!=0:
                pk=User.objects.filter(username=form.data["add-eliminar"])[0].pk
                
                if len(Player.objects.filter(user=pk))!=0:
                    user = Player.objects.filter(user=pk)[0]

                    if user.team and user.team==Team.objects.filter(name=form.data["name"])[0]:
                        user.team_id = None
                        user.searching = True
                        user.save()

                elif Den(Directivo.objects.filter(user=pk))!=0:
                    user = Directivo.objects.filter(user=pk)[0]

                    if user.team and user.team==Team.objects.filter(name=form.data["name"])[0]:
                        user.team_id = None
                        user.save()
        return self.render_to_response(context)



    def test_func(self): #COMPROBAR SI ES PROPIETARIO (ERROR 403: FORBIDDEN)
        try:
            return self.request.user.directivo.team==Team.objects.get(pk=self.kwargs.get("pk"))
        except:
            return False
class TeamCreateView(UserPassesTestMixin,CreateView): 
    model = Team
    fields='__all__'

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        directivo = Directivo.objects.get(user=self.request.user.pk)
        #AÑADIR EL EQUIPO AL DIRECTIVO.
        directivo.team_id = obj.pk
        directivo.save()
        return HttpResponseRedirect(reverse_lazy('vlr:team-list'))

    def test_func(self): #COMPROBAR SI ES DIRECTIVO (ERROR 403: FORBIDDEN)
        try:
            return Directivo.objects.get(user=self.request.user.pk) and Directivo.objects.get(user=self.request.user.pk).position=='CEO' and not Directivo.objects.get(user=self.request.user.pk).team
        except:
            return False
class TeamDeleteView(UserPassesTestMixin,DeleteView):
    model = Team
    success_url = reverse_lazy('vlr:team-list')
    
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
            return Fals
#DIRECTIVOS
class DirectivoListView(ListView):
    model = Directivo
class DirectivoDetailView(DetailView):
    queryset = Directivo.objects.all()
    template_name="VLR_APP/directivo_detail.html"
class DirectivoUpdateView(UserPassesTestMixin,UpdateView):
    queryset = Directivo.objects.all()
    fields=["position","experience"]
    success_url = reverse_lazy('vlr:home')
    def test_func(self): #COMPROBAR SI ES EL USUARIO (ERROR 403: FORBIDDEN)
        try:
            return Directivo.objects.get(pk=self.request.user.pk)==Directivo.objects.get(pk=self.kwargs.get("pk"))
        except:
            return False
class DirectivoCreateView(LoginRequiredMixin,UserPassesTestMixin,CreateView):
    model = Directivo
    fields=["position","experience"]
    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        obj.save()
        return HttpResponseRedirect(reverse_lazy('vlr:team-list'))
    def test_func(self): #COMPROBAR SI ES EL USUARIO (ERROR 403: FORBIDDEN)

        return True if not Player.objects.filter(user=self.request.user.pk) else False
class DirectivoDeleteView(UserPassesTestMixin,DeleteView):
    model = Directivo
    success_url = reverse_lazy('vlr:directivo-list')
    def form_valid(self,form):
        direct= Directivo.objects.get(pk=self.request.user.directivo.pk)
        if len(Team.objects.filter(pk=self.request.user.directivo.team_id))!=0:
            team = Team.objects.get(pk=self.request.user.directivo.team_id)
            team.delete()
            direct.delete()
        else:
            direct.delete()
        return HttpResponseRedirect(reverse_lazy('vlr:home'))
    def test_func(self): #COMPROBAR SI ES EL USUARIO (ERROR 403: FORBIDDEN)
        try:
            return Directivo.objects.get(user=self.request.user.pk)==Directivo.objects.get(user=self.kwargs.get("pk"))
        except:
            return False
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
class PlayerCreateView(UserPassesTestMixin,LoginRequiredMixin,CreateView):
    model = Player
    fields=["riot","primary_rol","horarios","experience","searching"]
    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        obj.save()
        return HttpResponseRedirect(reverse_lazy('vlr:home'))
    def test_func(self): #COMPROBAR SI ES EL USUARIO (ERROR 403: FORBIDDEN)

        return True if not Directivo.objects.filter(pk=self.request.user.pk) else False
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
class AnuncioCreateView(CreateView, UserPassesTestMixin):
    model = Anuncio
    fields=["title","message"]
    def form_valid(self,form):
        obj = form.save(commit=False)
        obj.directivo = self.request.user.directivo
        obj.save()
        return HttpResponseRedirect(reverse_lazy('vlr:home'))

    def test_func(self): #COMPROBAR SI ES EL USUARIO (DIRECTIVO) (ERROR 403: FORBIDDEN)
        try:
            return Directivo.objects.get(user=self.request.user.pk) and Directivo.objects.get(user=self.request.user.pk).team
        except:
            return False
class AnuncioDeleteView(DeleteView):
    model = Anuncio
    success_url = reverse_lazy('anuncios-list')
    def test_func(self): #COMPROBAR SI ES PROPIETARIO (ERROR 403: FORBIDDEN)
        try:
            return Anuncio.objects.get(directivo=self.request.user.directivo.pk)==Anuncio.objects.get(directivo=self.kwargs.get("pk"))
        except:
            return False
