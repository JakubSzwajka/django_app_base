from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login 
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User 
from django.views import generic, View
from django.urls import reverse_lazy
from .forms import RegisterForm


# Create your views here.
def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            new_user = form.save()
            new_user = authenticate(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password1'],)
            login(response, new_user)                       
            return redirect("/")
    else:
        form = RegisterForm()
    return render(response, "register/register.html", {"form":form})
 
class View_User_Page(generic.DetailView):
    template_name = 'register/view_profile_page.html'

    def get(self, request):  
        context = {'user':request.user}
        return render(request, self.template_name , context)


# class Edit_User_Page(generic.UpdateView):
def edit_user_page(request):
    template_name = 'register/edit_profile_page.html'
    success_url = reverse_lazy('index')

    # def get(self, request):
    if request.method == "POST":
        form = UserChangeForm(request.POST, instance = request.user)

        if form.is_valid():
            form.save()
            return redirect('/view_profile_page')

    else: 
        form = UserChangeForm(instance = request.user)
        context = {'form':form}
        return render(request, template_name, context)  