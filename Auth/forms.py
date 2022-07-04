from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model

User = get_user_model()


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField();
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput);
    password2 = forms.CharField(label="Repetir la contraseña", widget=forms.PasswordInput);
   
    class Meta:
       model = User 
       fields = ["username", "email", "password1", "password2"]
       
       help_texts = {k:"" for k in fields}
       
class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label="Nombre de usuario", widget=forms.TextInput({"autocomplete": "off"}))
    password = forms.CharField(label="Contraseña", widget=forms.PasswordInput({"autocomplete": "off"}))
    
    class Meta:
        model = User 
        fields = ["username", "password"]