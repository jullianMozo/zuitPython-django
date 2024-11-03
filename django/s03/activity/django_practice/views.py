from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.forms.models import model_to_dict


from django.http import HttpResponse
from .models import GroceryItem

def index(request):
    groceryItem_list = GroceryItem.objects.all()
    context = {
        "groceryItem_list": groceryItem_list,
        'user': request.user
        }
    return render(request, "django_practice/index.html", context)

from django.forms.models import model_to_dict

def grocery_Item(request, groceryItem_id):
    grocery_item = model_to_dict(GroceryItem.objects.get(pk=groceryItem_id))
    return render(request, "django_practice/groceryitem.html", grocery_item)



def register(request):
    
    users = User.objects.all()
    is_user_registered = False
    context = {
         "is_user_registered": is_user_registered
    }

    for indiv_user in users:
         if indiv_user.username == 'johndoe':
              is_user_registered = True
              break
    if is_user_registered == False:          
        user = User()
        user.username = 'johndoe'
        user.first_name = 'john'
        user.last_name = 'doe'
        user.email = 'johndoe@mail.com'
        user.set_password('john1234')
        user.is_staff = 'False'
        user.is_active = 'True'
        user.save()
        context = {
            'first_name': user.first_name,
            'last_name': user.last_name
        }       

    return render(request, 'django_practice/register.html', context) 

def change_password(request):
    is_user_authenticated = False

    user = authenticate(username='johndoe', password='john1234')
    print(user)

    if user is not None:
        authenticated_user = User.objects.get(username='johndoe')
        authenticated_user = user.set_password('johndoe1')
        user.save()
        is_user_authenticated = True
    context = {
            'is_user_authenticated': is_user_authenticated
        }
    return render(request, 'django_practice/change_password.html', context)

def login_view(request):
     username = 'johndoe'
     password = 'john1234'
     user = authenticate(username = username, password = password)
     context = {
          'is_user_authenticated': False
     }
     print(user)
     if user is not None:
        #   saves the users id in the sessions django session framwork
          login(request, user)
          return redirect("index")
     else:
         return render(request, 'django_practice/login.html', context)
     
def logout_view(request):
     logout(request)
     return redirect('index')

