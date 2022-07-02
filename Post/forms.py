from django import forms

from Post.models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ('user','created_post',)