# Generated by Django 5.0.6 on 2024-10-08 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_practice', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groceryitem',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
