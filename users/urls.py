from django.urls import path
from .views import register, profile, edit_profile
from django.contrib.auth.views import LoginView, LogoutView
urlpatterns = [
    path("register/", register, name= 'register'),
    path("profile/", profile, name= 'profile'),
    path("profile/update/", edit_profile, name= 'edit-profile'),
    path("login/", LoginView.as_view(template_name="users/login.html"), name= 'login'),
    path("logout/", LogoutView.as_view(template_name="users/logout.html"), name= 'logout'),

]
