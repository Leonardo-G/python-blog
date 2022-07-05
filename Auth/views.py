from django.shortcuts import redirect, render;
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

from django.contrib.auth.decorators import login_required
from Auth.forms import UserLoginForm, UserRegisterForm

def login_user(request):
    if request.method == "POST":
        form = UserLoginForm(request, data = request.POST);
        
        if form.is_valid():
            nombre = form.cleaned_data.get("username");
            password = form.cleaned_data.get("password");
            
            user = authenticate(username=nombre, password=password)
            
            if user is not None:
                login(request, user)
                return redirect("/inicio")
            else:
                return render(request, "login.html", {"form": form, "mensaje": "error"})
        else:
            print(form)
            return render(request, "login.html", {"form": form, "mensaje": "Usuario/Contraseña invalido"})
    
    form = UserLoginForm();
    return render(request, "login.html", {"form": form});

def register_user(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        
        if form.is_valid():
            
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]
            
            form.save()
            user = authenticate(username=username, password=password)
            
            if user is not None:
                login(request, user)
                print(form)
                return redirect("/inicio")
            else:
                print("Error")
                return render(request, "register.html", {"form": form, "mensaje": "Error al registrarse"})
        else:
            error = form.errors.as_data
            print(error)
            return render(request, "register.html", {"form": form, "mensaje": error})
    else:
        form = UserRegisterForm()
    return render(request, "register.html", {"form": form})

@login_required
def edit_profile(request):
    
    user = User.objects.get(username=request.user)
    print(user.email)
    
    return render(request, "edit_profile.html")