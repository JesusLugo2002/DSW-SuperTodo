from django.contrib import admin
from django.urls import path

from . import views

app_name = 'tasks'

urlpatterns = [
    path('', views.task_list, name='task-list'),
    path('add/', views.add_task, name='add-task'),
    path('done/', views.done_tasks, name='done-tasks'),
    path('pending/', views.pending_tasks, name='pending-tasks'),
    path('task/<task_slug>/', views.task_detail, name='task-detail'),
    path('task/<task_slug>/delete/', views.remove_task, name='remove-task'),
    path('task/<task_slug>/edit/', views.edit_task, name='edit-task'),
    path('task/<task_slug>/toggle/', views.toggle_task, name='toggle-task')
]
