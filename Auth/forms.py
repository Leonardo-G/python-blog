from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model

User = get_user_model()


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label="Nombre de Usuario");
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput);
    password2 = forms.CharField(label="Repetir la contraseña", widget=forms.PasswordInput);
   
    class Meta:
       model = User 
       fields = ["username", "password1", "password2"]
       
       help_texts = {k:"" for k in fields}
       
class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label="Nombre de usuario", widget=forms.TextInput({"autocomplete": "off"}))
    password = forms.CharField(label="Contraseña", widget=forms.PasswordInput({"autocomplete": "off"}))
    
    class Meta:
        model = User 
        fields = ["username", "password"]
        
class UserEditForm(UserCreationForm):

    email = forms.EmailField(label="Tu Email", widget=forms.EmailInput, required=False);
    last_name = forms.CharField(label="Apellido", widget=forms.TextInput, required=False);
    first_name = forms.CharField(label="Nombre", widget=forms.TextInput, required=False);
    password1 = forms.CharField( widget=forms.PasswordInput, required=False);
    password2 = forms.CharField(widget=forms.PasswordInput, required=False);

    class Meta:
       model = User 
       fields = ["email", "last_name", "first_name"]
       
       help_texts = {k:"" for k in fields}
