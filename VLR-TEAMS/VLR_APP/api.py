from VLR_APP.models import *
from django.urls import path, include
from rest_framework import routers, serializers, viewsets

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
        fields = ['name','foundation_date','city','info']

class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

#Directivos

class DirectivoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Directivo
        fields = ['team','position','experience']

class DirectivoViewSet(viewsets.ModelViewSet):
    queryset = Directivo.objects.all()
    serializer_class = DirectivoSerializer

#ROUTER
router = routers.DefaultRouter()

router.register(r'users', UserViewSet)
router.register(r'teams', TeamViewSet)
router.register(r'directivos', DirectivoViewSet)
