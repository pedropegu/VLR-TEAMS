from django.contrib.auth.forms import UserCreationForm
from .models import User,Player  
from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
class SignUpForm(UserCreationForm):

   class Meta:
      model = User  
      fields = ('username', 'password1', 'password2','email','fnac','description','image')
      labels = {
            'fnac': _('Date of birth'),
        }

from django.forms import ModelForm

class AuthorForm(ModelForm):
    class Meta:
        model = Player
        fields = ['user', 'team']