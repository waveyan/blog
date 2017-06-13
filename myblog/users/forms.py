from django.contrib.auth.forms import UserCreationForm
from .models import User

class RegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model=User
        fields=('username','nickname','email')

        #widgets={
        #    'username':UserCreationForm.TextInput(attrs={'padding':''}),
        #    'password':UserCreationForm.PasswordInput(attrs={'width':'100%'})
        #}
