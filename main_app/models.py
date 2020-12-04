import datetime
from django.db import models 
from django.contrib.auth.models import Group
from django.utils import timezone
from django.contrib.auth.models import User


class Task(models.Model): 
    task_name = models.CharField(max_length=200)
    task_url = models.CharField(max_length=200)
    
    def __str__(self):
        return self.task_name 