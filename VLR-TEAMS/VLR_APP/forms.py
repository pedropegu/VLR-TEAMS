from django.contrib.auth.forms import UserCreationForm
from .models import User  
class SignUpForm(UserCreationForm):

   class Meta:
      model = User #this is the "YourCustomUser" that you imported at the top of the file  
      fields = ('username', 'password1', 'password2','email','fnac','description')