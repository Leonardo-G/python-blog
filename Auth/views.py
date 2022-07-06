from django.shortcuts import redirect, render;
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

from django.contrib.auth.decorators import login_required
from Auth.forms import UserEditForm, UserLoginForm, UserRegisterForm
from Auth import models

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
                avatar = models.Avatar(user=request.user, imagen = None)
                avatar.save();
                
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
def get_profile(request):
    user = User.objects.get(username=request.user)
    avatar = models.Avatar.objects.get(user=request.user.id)
    print(avatar.imagen)
    return render(request, "profile.html", {"avatar": avatar, "user": user})

@login_required
def edit_profile(request):
    
    # Instancia del login
    user = User.objects.get(username=request.user)
    avatar = models.Avatar.objects.get(user=request.user.id)
    
    if request.method == "POST":
        miFormulario = UserEditForm(request.POST)
        if miFormulario.is_valid():
            
            user.id = user.id
            user.username = user.username
            user.last_name = miFormulario.cleaned_data["last_name"]
            user.first_name = miFormulario.cleaned_data["first_name"]
            user.email = miFormulario.cleaned_data["email"]
            user.password = user.password
            user.save()
            
            avatar.id = avatar.id
            avatar.user_id = user.id;
            
            if request.FILES:
                avatar.imagen = request.FILES["image"]
            else:
                avatar.imagen = avatar.imagen
                
            avatar.save()

            return redirect("/account/profile")
    
    else:
        form = UserEditForm(initial={"email": user.email, "last_name": user.last_name, "first_name": user.first_name})
        print(user.last_name)
        return render(request, "edit_profile.html", {"form":form,"user":user})

