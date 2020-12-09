from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth import authenticate, login 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Create your views here.
def register(response):

    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            new_user = form.save()
            new_user = authenticate(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password1'],)
            login(response, new_user)                       
            return redirect("/main_app")
    else:
        form = RegisterForm()

    return render(response, "register/register.html", {"form":form})
