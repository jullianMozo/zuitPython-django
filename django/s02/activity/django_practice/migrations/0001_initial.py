# Generated by Django 5.0.6 on 2024-10-08 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GroceryItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=50)),
                ('category', models.CharField(max_length=50)),
                ('status', models.CharField(default='pending', max_length=50)),
                ('date_created', models.DateTimeField(verbose_name='date created')),
            ],
        ),
    ]