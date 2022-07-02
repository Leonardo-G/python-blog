from django.urls import path
from Auth import views

urlpatterns = [
    path("login/", views.login_user, name="login"),
    path("register/", views.register_user, name="register"),
    path("edit_profile/", views.edit_profile, name="edit_profile"),
]
