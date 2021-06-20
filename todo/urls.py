from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('folders/<int:id>/tasks', views.index, name='tasks.index'),
    path('folders/create', views.create_folder, name='folders.create'),
    path('folders/<int:id>/tasks/create', views.create_task, name='tasks.create'),
    path('folders/<int:id>/tasks/feedback', views.feedback, name='tasks.feedback'),
    path('folders/<int:id>/tasks/<int:task_id>', views.edit_task, name='tasks.edit'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
