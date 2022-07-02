from django.shortcuts import render
from Post import models
from Post.forms import PostForm
from django.contrib.auth.decorators import login_required

def inicio_view(request):
    
    posts = models.Post.objects.all()
    
    return render(request, "inicio.html", {"posts": posts})

@login_required
def new_post(request):
    if request.method == "POST":
        
        formPost = PostForm(request.POST)
        
        if formPost.is_valid():
            
            dataTitle = formPost.cleaned_data["title"];
            dataDescription = formPost.cleaned_data["description"];
            dataSummary = formPost.cleaned_data["summary"];
            dataUser = request.user;
            
            post = models.Post(title=dataTitle, description=dataDescription, user=dataUser, summary=dataSummary)
            post.save()
    else:
        
        form = PostForm()
        return render(request, "new_post.html", {"form": form})
    
def post_view(request, post_id):
    
    post = models.Post.objects.get(pk=post_id)
    userActually = request.user == post.user
    print(userActually)
    
    return render(request, "post.html", {"post": post, "userActually": userActually})