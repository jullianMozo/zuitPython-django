from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# each model represent a class that subclasses django.db.models.Models

class ToDoItem(models.Model):
    # CharFields(max_length=50) = string data type with 50 max character
    task_name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    status = models.CharField(max_length=50, default="pending")
    date_created = models.DateTimeField('date created')
    user = models.ForeignKey(User, on_delete=models.CASCADE, default="")