from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:groceryItem_id>/', views.groceryItem, name='viewgroceryItem'),  # Corrected view function
]
