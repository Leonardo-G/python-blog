from django.shortcuts import redirect, render;
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User

from django.contrib.auth.decorators import login_required
from Auth.forms import UserRegisterForm

def login_user(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST);
        
        if form.is_valid():
            nombre = form.cleaned_data.get("username");
            password = form.cleaned_data.get("password");
            
            user = authenticate(username=nombre, password=password)
            
            if user is not None:
                login(request, user)
                return redirect("/inicio")
            else:
                return render(request, "login.html", {"mensaje": "error"})
        else:
            return render(request, "login.html", {"mensaje": "error en validar login"})
    
    form = AuthenticationForm();
    return render(request, "login.html", {"form": form, "mensaje": "asdasd"});

def register_user(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        
        if form.is_valid():
            
            form.cleaned_data["email"]
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]
            
            form.save()
            user = authenticate(username=username, password=password)
            
            if user is not None:
                login(request, user)
                return redirect("/inicio")
    else:
        form = UserRegisterForm()
    return render(request, "register.html", {"form": form})

@login_required
def edit_profile(request):
    
    user = User.objects.get(username=request.user)
    print(user.email)
    
    return render(request, "edit_profile.html")