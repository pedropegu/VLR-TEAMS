from django.contrib.auth.forms import UserCreationForm
from .models import *
from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from django import forms
class SignUpForm(UserCreationForm):

   class Meta:
      model = User  
      fields = ('username', 'password1', 'password2','email','fnac','description','image')
      labels = {
            'fnac': _('Date of birth'),
        }

choice_player = {}
queryset = Player.objects.all()
for query in queryset:
    choice_player[query]=query
choice_player = [(k, v) for k, v in choice_player.items()]
class PlayerTeam(forms.Form):
    user = forms.MultipleChoiceField(choices = choice_player, required=False)
class PlayerTeamDelete(forms.Form):
    user = forms.MultipleChoiceField(choices = choice_player, required=False)