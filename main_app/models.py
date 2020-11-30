from django.db import models

# Create your models here.

class Student(models.Model):
    student_index = models.CharField( max_length=6)
    student_name = models.CharField( max_length=30 )
    student_surname = models.CharField( max_length=30 )
    create_date = models.DateTimeField('Creation Date')
    