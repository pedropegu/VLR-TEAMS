
from django.utils.translation import gettext_lazy as _
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse

# Create your models here.

class User(AbstractUser):

    fnac = models.DateField(null=True,blank=True)
    description = models.CharField(max_length=200,blank=True,null=True)

    def get_absolute_url(self):
        return reverse('client-detail', kwargs={'pk': self.pk})
    

    def __str__(self) -> str:
        return self.username

class Team(models.Model):


    #ATRIBUTOS
    name = models.CharField(max_length=30, unique=True)
    foundation_date = models.DateField() 
    city = models.CharField(max_length=30)

    info = models.CharField(max_length=300)
    


    def get_absolute_url(self):
        return reverse('team-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.name

class Directivo(models.Model):

    class Position(models.TextChoices):
        CEO = "CEO", _("Ceo")
        MANAGER = "MANAGER", _("Manager")
    
    
    #RELACIONES

    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    team = models.ForeignKey(Team, on_delete=models.SET_NULL, blank=True, null=True)

    #ATRIBUTOS

    position = models.CharField(
        max_length=7,
        choices=Position.choices,
        default=Position.CEO,
    )
    experience = models.CharField(max_length=300, blank=True) 
    def get_absolute_url(self):
        return reverse('directivo-detail', kwargs={'pk': self.pk})
    def __str__(self):
        return self.user.username

class Player(models.Model):
    
    #OPCIONES

    class Work_Schedule(models.TextChoices):
        AFTERNOON = "AF", _("Afternoon")
        MORNING = "MO", _("Morning")


    class Team_Sarch(models.TextChoices):
        YES = "Y", _("YES")

    #RELACIONES

    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    team = models.ForeignKey(Team, on_delete=models.SET_NULL, blank=True, null=True)

    # ATRIBUTOS

    riot = models.CharField(max_length=50, unique=True)

    primary_rol = models.CharField(max_length=50)

    horarios = models.CharField(
        max_length=2,
        choices=Work_Schedule.choices,
        default=Work_Schedule.MORNING,
    )


    experience = models.CharField(max_length=300)
    def get_absolute_url(self):
        return reverse('player-detail', kwargs={'pk': self.pk})
    def __str__(self):
        return self.User.username

class Coache(models.Model):

    #RELACIONES

    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    team = models.ForeignKey(Team, on_delete=models.SET_NULL, blank=True, null=True)

    #ATRIBUTOS

    experience = models.CharField(max_length=300)
    def get_absolute_url(self):
        return reverse('coach-detail', kwargs={'pk': self.pk})
    def __str__(self):
        return self.user.username

class Anuncio(models.Model):
    
    #RELACIONES

    directivo = models.ForeignKey(Directivo, on_delete=models.CASCADE)

    #ATRIBUTOS

    title = models.CharField(max_length=30)
    message = models.CharField(max_length=500)

    def get_absolute_url(self):
        return reverse('anuncios-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title

