from dataclasses import fields
from django import forms

from Post.models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "summary", "description"]
        exclude = ('user','created_post',)
        widgets = {
            "title": forms.TextInput(attrs={"placeholder": "Escribe tu título aquí", "class": "campo--title"}),
            "summary": forms.TextInput(attrs={"placeholder": "Añade información que aparecerá en el resumen de sus post", "class": "campo--summary"}),
            "description": forms.Textarea(attrs={"placeholder": "Esciba su post...", "class": "campo--description"})
        }