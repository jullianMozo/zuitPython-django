from django.shortcuts import render
from django.http import HttpResponse
from .models import GroceryItem

def index(request):
    groceryItem_list = GroceryItem.objects.all()
    context = {"groceryItem_list": groceryItem_list}
    return render(request, "django_practice/index.html", context)

def groceryItem(request, groceryItem_id):
    response = "You are viewing the details of %s"
    return HttpResponse(response % groceryItem_id)

