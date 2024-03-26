from django.urls import path
from . import views.py

urlpatterns = [ 
    path('', views.post_list, name='post_list'),
]