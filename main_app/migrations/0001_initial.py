# Generated by Django 3.1.3 on 2020-11-30 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_index', models.CharField(max_length=6)),
                ('student_name', models.CharField(max_length=30)),
                ('student_surname', models.CharField(max_length=30)),
                ('create_date', models.DateTimeField(verbose_name='Creation Date')),
            ],
        ),
    ]
