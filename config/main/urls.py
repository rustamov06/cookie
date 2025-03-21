from django.contrib import admin
from django.urls import path
from .views import index, add_to_session, view_session, update_session, delete_session

urlpatterns = [
    path('', index, name='index'),
    path('add/', add_to_session, name='add_to_session'),
    path('view/', view_session, name='view_session'),
    path('update/', update_session, name='update_session'),
    path('delete/', delete_session, name='delete_session'),
]
