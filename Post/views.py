from django.shortcuts import redirect, render
from Post import models
from Post.forms import PostForm
from django.contrib.auth.decorators import login_required

def inicio_view(request):
    print(request.user)
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
            return redirect("/inicio")
    else:
        
        form = PostForm()
        print(form)
        return render(request, "new_post.html", {"form": form})
    
def post_view(request, post_id):
    
    post = models.Post.objects.get(pk=post_id)
    userActually = request.user == post.user
    print(userActually)
    
    return render(request, "post.html", {"post": post, "userActually": userActually})

@login_required
def edit_post(request, post_id):
    post = models.Post.objects.get(pk=post_id)
    
    if request.method == "POST":
        form = PostForm(request.POST)
        
        if form.is_valid():
            
            post.id = post_id
            post.title = form.cleaned_data["title"]
            post.summary = form.cleaned_data["summary"]
            post.description = form.cleaned_data["description"]
            post.save()
            
            return redirect(f"/post/{post.id}")
    else:
        form = PostForm(initial={"title": post.title, "summary": post.summary, "description": post.description})
        return render( request, "edit_post.html", {"form": form, "post": post})
    
@login_required
def delete_post(request, post_id):
    post = models.Post.objects.get(pk=post_id)
    post.delete()
    
    return render(request, "post-delete.html")
    