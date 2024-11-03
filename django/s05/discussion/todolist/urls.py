from django.urls import path

from . import views

app_name="todolist"
# path can recieve 4 arguments
# will focus on the arguments that are required:
# this are the route,view,name
# route allows for setting endpoint to view content
# view to access view.py and display content in the uri enpoint
# name wich allows for the global access to the url patteens
urlpatterns = [
	# index route
	path('', views.index, name='index'),
	# /todoitem/todoitem_id' route
	# the '<int:todoitem_id>/' allows for creating a dynamic link where the todoitem_id is provided
	path('<int:todoitem_id>/', views.todoitem, name='viewtodoitem'),
    # register route
    path('register', views.register, name='register'),
    # change_password route
    path('change_password', views.change_password, name='change_password'),
    # login route
    path('login', views.login_view, name='login'),
    
	path('logout', views.logout_view, name='logout'),

    path('add_task', views.add_task, name='add_task'),

    path('<int:todoitem_id>/edit', views.update_task, name='update_task'),
    
    path('<int:todoitem_id>/delete', views.delete_task, name='delete_task'),

    path('add_event', views.add_Event, name='add_event'),

     path('event/<int:event_id>/', views.eventlist, name='vieweventlist'), 
]