from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from Post import models
from Post.forms import PostForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

def redirect_home(request):
    print("Hola")
    return HttpResponseRedirect("/inicio")

def inicio_view(request):
    print(request.user)
    posts = models.Post.objects.order_by("-visited")[:6]
    
    return render(request, "inicio.html", {"posts": posts})

def nosotros(request):
    nosotros_list = models.Nosotros.objects.all()
    return render(request, 'nosotros.html',{'nosotros':nosotros_list})

# CREATE
@login_required
def new_post(request):
    if request.method == "POST":
        
        formPost = PostForm(request.POST, request.FILES)
        
        if formPost.is_valid():
            
            dataImage = formPost.cleaned_data["image"]
            dataTitle = formPost.cleaned_data["title"];
            dataSubtitle = formPost.cleaned_data["subtitle"];
            dataDescription = formPost.cleaned_data["description"];
            dataSummary = formPost.cleaned_data["summary"];
            dataUser = request.user;
            
            post = models.Post(image=dataImage, title=dataTitle, subtitle=dataSubtitle, description=dataDescription, user=dataUser, summary=dataSummary)
            post.save()
            return redirect("/inicio")
    else:
        
        form = PostForm()
        print(form)
        return render(request, "new_post.html", {"form": form})
    
# GET
def post_view(request, post_id):
    
    post = models.Post.objects.get(pk=post_id)
    
    #Solamente se tendrá en cuenta la visitas de los usuarios, pero no del creador.
    if post.user != request.user:
        post.visited += 1
        post.save();
    
    userActually = request.user == post.user
    print(userActually)
    
    return render(request, "post.html", {"post": post, "userActually": userActually})

# POST
@login_required
def edit_post(request, post_id):
    post = models.Post.objects.get(pk=post_id)
    
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        
        #En caso de que el usuario tarde en actualizar, tomamaos las visitas que tienen al realizar el POST
        postActually = models.Post.objects.get(pk=post_id)
        if form.is_valid():
            
            post.id = post_id
            post.visited = postActually.visited
            post.image = post.image
            post.title = form.cleaned_data["title"]
            post.subtitle = form.cleaned_data["subtitle"]
            post.summary = form.cleaned_data["summary"]
            post.description = form.cleaned_data["description"]
            post.save()
            
            return redirect(f"/post/{post.id}")
    else:
        print(post.image)
        form = PostForm(initial={"image": post.image, "title": post.title, "subtitle": post.subtitle, "summary": post.summary, "description": post.description})
        return render( request, "edit_post.html", {"form": form, "post": post})
   
# DELETE 
@login_required
def delete_post(request, post_id):
    post = models.Post.objects.get(pk=post_id)
    post.delete()
    
    return render(request, "post-delete.html")

def post_view_page(request, page):
    
    posts = models.Post.objects.order_by("-visited")
    paginator = Paginator(posts, 6)
    post_page = paginator.get_page(int(page))
    
    arrayPage = [];
    numPage = paginator.num_pages;
    for i in range(numPage):
        arrayPage.append(i + 1)
    
    return render(request, "postPage.html", {"posts": post_page, "arrayPage": arrayPage})
    