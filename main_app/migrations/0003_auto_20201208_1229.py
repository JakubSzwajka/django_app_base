# Generated by Django 3.1.3 on 2020-12-08 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_auto_20201203_1352'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Student',
        ),
        migrations.AddField(
            model_name='task',
            name='description',
            field=models.CharField(default='Default Content', max_length=1000),
            preserve_default=False,
        ),
    ]
