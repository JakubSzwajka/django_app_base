from django.db import models 
from django.contrib.auth.models import Group, User
from django.utils import timezone
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save 

import datetime
import os

class Task(models.Model): 
    task_name = models.CharField(max_length=200)
    task_url = models.CharField(max_length=200)
    description = models.TextField(max_length=1000)

    def __str__(self):
        return self.task_name 

class Profile(models.Model):
    user = models.OneToOneField(User,
            on_delete=models.CASCADE)
    birth_date = models.DateField( null=True, blank=True)
    profile_image = models.ImageField(upload_to='user_images/', default='main_app/assets/user.png', max_length=200 )

# Below two methods are for Prifile <-> User update when created
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs): 
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()