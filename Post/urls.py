from django.urls import path
from Post import views

urlpatterns = [
    path("inicio/", views.inicio_view, name="inicio"),
    path("new_post/", views.new_post, name="new_post"),
    path("post/<int:post_id>/", views.post_view, name="post"),
    path("post-edit/<int:post_id>", views.edit_post, name="post-edit")
]
