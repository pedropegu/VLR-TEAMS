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
class TeamCreateForm(forms.ModelForm):

   class Meta:
      model = Team  
      fields = ('name', 'foundation_date', 'city','info','image')


class TeamAdd(forms.Form):
    añadir = forms.CharField(max_length=50,required=False)
    eliminar = forms.CharField(max_length=50,required=False)