from django.urls import path

from . import views

# path can recieve 4 arguments
# will focus on the arguments that are required:
# this are the route,view,name
# route allows for setting endpoint to view content
# view to access view.py and display content in the uri enpoint
# name wich allows for the global access to the url patteens
urlpatterns = [
    path('', views.index, name='index')
]