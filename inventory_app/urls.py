# inventory_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_movement, name='add_movement'),
    path('list/', views.movement_list, name='movement_list'),
    path('summary/', views.stock_summary, name='stock_summary'),
]
