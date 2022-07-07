from django import forms

from Post.models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["image", "title", "subtitle", "summary", "description"]
        exclude = ('user','created_post',)
        labels = {
            "image": "Portada del Post",
            "subtitle": "Sub Titulo",
            "summary": "Resumen",
            "description": "Descripción",
        }
        widgets = {
            "image": forms.FileInput(attrs={"class": "campo--summary", "accept":"image/*", "required": "true"}),
            "title": forms.TextInput(attrs={"placeholder": "Escribe tu título aquí", "class": "campo--title"}),
            "subtitle": forms.TextInput(attrs={"placeholder": "Añade el subtítulo", "class": "campo--summary"}),
            "summary": forms.TextInput(attrs={"placeholder": "Añade información que aparecerá en el resumen de sus post", "class": "campo--summary"}),
            "description": forms.Textarea(attrs={"placeholder": "Esciba su post...", "class": "campo--description"}),
        }