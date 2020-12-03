from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .models import Task

class IndexView(generic.ListView):
    template_name = 'main_app/index.html'
    context_object_name = 'task_list'

    def get_queryset(self):
        #Return the last 5 published questions. 
        return Task.objects.order_by('task_name')