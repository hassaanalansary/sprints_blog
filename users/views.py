from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from users.models import User

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["name", "email", "username", "password1", "password2"]

def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password1")
            email = form.cleaned_data.get("email")
            name = form.cleaned_data.get("name")
            user = User(username=username, name=name, email=email)
            user.set_password(password)
            user.save()
            return redirect("blog-home")
    form = UserRegistrationForm()
    return render(request, 'users/register.html', context={'form': form})
