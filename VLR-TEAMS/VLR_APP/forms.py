from django.contrib.auth.forms import UserCreationForm
from .models import User  
from django.utils.translation import gettext_lazy as _
class SignUpForm(UserCreationForm):

   class Meta:
      model = User  
      fields = ('username', 'password1', 'password2','email','fnac','description','image')
      labels = {
            'fnac': _('Date of birth'),
        }