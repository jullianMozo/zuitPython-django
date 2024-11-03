from django.urls import path

from . import views

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
	path('<int:todoitem_id>/', views.todoitem, name='viewtodoitem')
]