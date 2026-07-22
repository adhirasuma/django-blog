from django.contrib.auth.models import User # default django model (used in django forms)
from django.contrib.auth.forms import UserCreationForm

class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email','username','password1','password2')
        #password1->password
        #password2->confirm password
