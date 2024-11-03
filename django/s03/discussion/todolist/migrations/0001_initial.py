# Generated by Django 5.1.1 on 2024-10-07 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ToDoItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=200)),
                ('status', models.CharField(default='pending', max_length=50)),
                ('date_created', models.DateTimeField(verbose_name='date created')),
            ],
        ),
    ]