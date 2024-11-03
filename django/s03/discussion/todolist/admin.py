from django.contrib import admin

# Register your models here.

from . models import ToDoItem

# interact with todoitems through django admin
admin.site.register(ToDoItem)
