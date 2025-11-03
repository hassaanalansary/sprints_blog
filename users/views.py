from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from users.models import User
from django.contrib import messages
from django import forms
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
            messages.success(request, "User Created Successfully")
            return redirect("blog-home")
    else:
        form = UserRegistrationForm()
    return render(request, 'users/register.html', context={'form': form})

@login_required
def profile(request):
    return render(request, 'users/profile.html')

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["name", "email", "username", "profile_image"]
        widgets = {
           "name": forms.TextInput(attrs= {"class": "validate"}),
           "email": forms.EmailInput(attrs= {"class": "validate"}),
           "username": forms.TextInput(attrs= {"class": "validate"}),
        }


def edit_profile(request):
    if request.method == "POST":
        form = UserUpdateForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully.")
            return redirect('profile')
    else:
        form  = UserUpdateForm(instance=request.user)
    return render(request, "users/edit_profile.html", {'form':form})