from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import User
#_
from django.utils.translation import ugettext_lazy as _


class RegisterForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model=User
        fields=('username','nickname','email')

        #widgets={
        #    'username':UserCreationForm.TextInput(attrs={'padding':''}),
        #    'password':UserCreationForm.PasswordInput(attrs={'width':'100%'})
        #}

        #{{field.label_tag}}
        labels={
            'nickname':_('昵称')
        }
        #{{field.help_text}}
        help_texts={
            'nickname':_('必填。150个字符或者更少。包含字母，数字和仅有的@/./+/-/_符号。')
        }



class LoginForm(forms.Form):
    username=forms.CharField(label='用户名',required=True)
    password=forms.CharField(label='密码',required=True,help_text='至少8个字符以上',widget=forms.PasswordInput())





