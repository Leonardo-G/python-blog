from django.urls import path
from Post import views

urlpatterns = [
    path("", views.redirect_home, name="inicio"),
    path("inicio/", views.inicio_view, name="inicio"),
    path('nosotros/', views.nosotros, name="nosotros"),
    path("new_post/", views.new_post, name="new_post"),
    path("post/<int:post_id>/", views.post_view, name="post"),
    path("post-edit/<int:post_id>", views.edit_post, name="post-edit"),
    path("post-delete/<int:post_id>", views.delete_post, name="post-delete"),
    path("post-page/<int:page>", views.post_view_page, name="post-page"),
]
