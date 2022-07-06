from django.urls import path, reverse_lazy
from Auth import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("login/", views.login_user, name="login"),
    path("register/", views.register_user, name="register"),
    path("profile/", views.get_profile, name="profile"),
    path("edit_profile/", views.edit_profile, name="edit_profile"),
    path("logout/", LogoutView.as_view(), {'next_page': reverse_lazy("login")}, name='logout')
]
