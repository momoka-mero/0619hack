from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('folders/<int:id>/tasks', views.index, name='tasks.index'),
    path('folders/create', views.create_folder, name='folders.create'),
    path('folders/<int:id>/tasks/create', views.create_task, name='tasks.create'),
    path('folders/<int:id>/tasks/<int:task_id>', views.edit_task, name='tasks.edit'),
    path('signin/', views.signin, name='signin')
]