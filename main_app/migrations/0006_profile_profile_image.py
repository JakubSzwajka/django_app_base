# Generated by Django 3.1.3 on 2020-12-08 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='profile_image',
            field=models.ImageField(default='/assets/user.png', upload_to='user_images/'),
        ),
    ]
