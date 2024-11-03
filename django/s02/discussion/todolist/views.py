from django.shortcuts import render
from django.template import loader

# Create your views here.
# from keyword allows importing of classes application, methods
# import keyword defines what we are importing from the package
from django.http import HttpResponse
from .models import ToDoItem 
def index(request):
    todoitem_list = ToDoItem.objects.all()
    # output = ','.join([todoitem.task_name for todoitem in todoitem_list])
    # return HttpResponse(output)
    # template = loader.get_template("todolist/index.html")
    context = {"todoitem_list": todoitem_list}
    return render(request, "todolist/index.html", context)

def todoitem(request, todoitem_id):
    response = "you are view the details of %s"
    return HttpResponse(response % todoitem_id)