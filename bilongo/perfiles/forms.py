from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


from perfiles.models import Avatar

class UserRegisterForms(UserCreationForm):
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Your password again", widget=forms.PasswordInput)

    class Meta:
       model = User
       fields = ['last_name', 'first_name', 'username', 'email', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):

   class Meta:
       model = User
       fields = ['last_name', 'first_name', 'email']

# Agregar al final del archivo
class AvatarFormulario(forms.ModelForm):

   class Meta:
       model = Avatar
       fields = ['imagen']