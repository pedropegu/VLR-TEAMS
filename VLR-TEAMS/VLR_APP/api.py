from VLR_APP.models import *
from rest_framework import routers,serializers, viewsets

#CLIENTES

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

#EQUIPOS

class TeamSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Team
        fields = ['url','name','foundation_date','city','info']

class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

#Directivos

class DirectivoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Directivo
        fields = ['url','team','position','experience']

class DirectivoViewSet(viewsets.ModelViewSet):
    queryset = Directivo.objects.all()
    serializer_class = DirectivoSerializer

#PLAYERS
class PlayerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Player
        fields = ['url','team','position','experience']

class PlayerViewSet(viewsets.ModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
#COACHES
class CoachesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Coache
        fields = ['url','team','position','experience']

class CoacheViewSet(viewsets.ModelViewSet):
    queryset = Coache.objects.all()
    serializer_class = CoachesSerializer

#ANUNCIOS
class AnunciosSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Anuncio
        fields = ['url','team','position','experience']

class AnuncioViewSet(viewsets.ModelViewSet):
    queryset = Anuncio.objects.all()
    serializer_class = AnunciosSerializer

#REGISTER
api = routers.DefaultRouter()
api.register(r'users', UserViewSet)
api.register(r'teams', TeamViewSet)
api.register(r'executives', DirectivoViewSet)
api.register(r'players', PlayerViewSet)
api.register(r'coaches', CoacheViewSet)
api.register(r'anuncios', AnuncioViewSet)

