
from django.utils.translation import gettext_lazy as _
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birthdate = models.DateField()


    def __str__(self) -> str:
        return self.user.username

class directivo(models.Model):
    client = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    class Position(models.TextChoices):
        CEO = "CEO", _("Ceo")
        MANAGER = "MANAGER", _("Manager")
    
    
    position = models.CharField(
        max_length=7,
        choices=Position.choices,
        default=Position.CEO,
    )

    experience = models.CharField(max_length=150, blank=True) 

    def __str__(self):
        return self.client.username

class team(models.Model):
    name = models.CharField(max_length=30, unique=True)
    foundation_date = models.DateField() 
    city = models.CharField(max_length=30)
    
    founder = models.OneToOneField(directivo,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class player(models.Model):

    class Work_Schedule(models.TextChoices):
        AFTERNOON = "AF", _("Afternoon")
        MORNING = "MO", _("Morning")

    client = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    riot = models.CharField(max_length=30, unique=True)

    horarios = models.CharField(
        max_length=2,
        choices=Work_Schedule.choices,
        default=Work_Schedule.MORNING,
    )

    experience = models.CharField(max_length=400)

    team = models.ForeignKey(team, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.client.username

class coache(models.Model):
    client = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    experience = models.CharField(max_length=300)
    team = models.ForeignKey(team, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.client.username

class anuncio(models.Model):
    title = models.CharField(max_length=30)
    message = models.CharField(max_length=500)
    
    directivo = models.ForeignKey(directivo, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


