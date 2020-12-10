from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic, View
from .models import Task, User


class MainPage(View):
    template_name = 'main_app/content_page.html'
    context_object_name = 'task_list'

    def get(self, request):
        if self.request.user.is_authenticated:
            #Return the last 5 published questions. 
            tasks = Task.objects.order_by('task_name')
            return render( template_name= self.template_name, request=request , context={"task_list":tasks})
        else: 
            return HttpResponseRedirect(reverse('login'))
