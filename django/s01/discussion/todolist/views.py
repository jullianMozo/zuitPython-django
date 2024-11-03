from django.shortcuts import render

# Create your views here.
# from keyword allows importing of classes application, methods
from django.http import HttpResponse

def index(request):
    return HttpResponse("hello from the views.py file.")

