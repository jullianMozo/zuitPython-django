from django.shortcuts import render, redirect, get_object_or_404
# from django.template import loader
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.forms.models import model_to_dict
from django.utils import timezone

# Create your views here.
# from keyword allows importing of classes application, methods
# import keyword defines what we are importing from the package

from django.http import HttpResponse
from .models import ToDoItem
from .forms import LoginForm, AddTaskForm, UpdateTaskForm, RegisterForm


def index(request):
     todoitem_list = ToDoItem.objects.filter(user_id = request.user.id)
     # output = ','.join([todoitem.task_name for todoitem in todoitem_list])
     # return HttpResponse(output)
     # template = loader.get_template("todolist/index.html")
     context = {
          "todoitem_list": todoitem_list,
          'user': request.user
          }
     return render(request, "todolist/index.html", context)

def todoitem(request, todoitem_id):
    todoitem = get_object_or_404(ToDoItem, pk=todoitem_id)
    context = model_to_dict(todoitem)
    return render(request, "todolist/todoitem.html", context)



def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')

            if not User.objects.filter(username=username).exists():
                user = User.objects.create_user(
                    username=username,
                    first_name=first_name,
                    last_name=last_name,
                    email=email,
                    password=password
                )
                user.save()

                context = {
                    'first_name': user.first_name,
                    'last_name': user.last_name,
                    'is_user_registered': True
                }
                return render(request, 'todolist/register.html', context)

    else:
        form = RegisterForm()
    
    return render(request, 'todolist/register.html', {'form': form, 'is_user_registered': False})

def change_password(request):
    is_user_authenticated = False

    user = authenticate(username='johndoe', password='john1234')
    print(user)

    if user is not None:
        authenticated_user = User.objects.get(username='johndoe')
        authenticated_user = user.set_password('johndoe1')
        is_user_authenticated = True
    context = {
            'is_user_authenticated': is_user_authenticated
        }
    return render(request, 'todolist/change_password.html', context)

def login_view(request):
	context = {}

	if request.method == 'POST':
		form = LoginForm(request.POST)

		if form.is_valid() == False:
			form == LoginForm()

		else:
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			user = authenticate(username=username, password=password)
			context = {
				'username': username,
				'password': password
			}

			if user is not None:
				login(request, user)
				return redirect("todolist:index")
			else:
				context = {
					'error':True
				}
	return render(request, 'todolist/login.html', context)
     
def logout_view(request):
     logout(request)
     return redirect("todolist:index")

def add_task(request):

    context = {}

    if request.method == 'POST':

        form = AddTaskForm(request.POST)

        if form.is_valid() == False:

            form = AddTaskForm()

        else:

            task_name = form.cleaned_data['task_name']
            description = form.cleaned_data['description']

            # Checks the database if a task already exists
            # By default the "filter" method searches for records that are case insensitive
            duplicates = ToDoItem.objects.filter(task_name=task_name, user_id = request.user.id)
            
            # if todoitem does not contain any duplicates
            if not duplicates:

                # Creates an object based on the "ToDoItem" model and saves the record in the database
                ToDoItem.objects.create(task_name=task_name, description=description, date_created=timezone.now(), user_id = request.user.id)
                return redirect("todolist:index")

            else:

                context = {
                    "error": True
                }

    return render(request, "todolist/add_task.html", context)

def update_task(request, todoitem_id):
	todoitem = ToDoItem.objects.filter(pk=todoitem_id)

	context = {
		"user": request.user,
		"todoitem_id": todoitem_id,
		"task_name": todoitem[0].task_name,
		"description":todoitem[0].description,
		"status": todoitem[0].status
	}

	if request.method == "POST":
		form = UpdateTaskForm(request.POST)

		if form.is_valid()== False:
			form.UpdateTaskForm()
		else:
			task_name = form.cleaned_data['task_name']
			description = form.cleaned_data['description']
			status = form.cleaned_data['status']

			if todoitem:
				todoitem[0].task_name = task_name
				todoitem[0].description	= description
				todoitem[0].status = status

				todoitem[0].save()
				return redirect('todolist:index')
			else:
				context = {
					'error': True
				}
	return render(request, 'todolist/update_task.html', context)


def delete_task(request, todoitem_id):
    todoitem = ToDoItem.objects.filter(pk=todoitem_id).delete()
    return redirect("todolist:index")