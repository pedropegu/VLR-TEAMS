from django.contrib.auth.forms import UserCreationForm
from .models import User  
from django.utils.translation import gettext_lazy as _
class SignUpForm(UserCreationForm):

   class Meta:
      model = User #this is the "YourCustomUser" that you imported at the top of the file  
      fields = ('username', 'password1', 'password2','email','fnac','description','image')
      labels = {
            'fnac': _('Date of birth'),
        }