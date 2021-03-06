# Generated by Django 3.1.3 on 2020-12-03 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_name', models.CharField(max_length=200)),
                ('task_url', models.CharField(max_length=200)),
            ],
        ),
        migrations.RenameField(
            model_name='student',
            old_name='student_name',
            new_name='family_name',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='student_surname',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='student_index',
            new_name='index',
        ),
        migrations.RemoveField(
            model_name='student',
            name='create_date',
        ),
    ]
