from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from .models import Folder,Task, Image
from .forms import *
from django.contrib.auth import get_user_model
from django.contrib.auth.views import (
    LoginView, LogoutView
)
from django.views import generic
# from .forms import LoginForm


User = get_user_model()

def index(request, id):
    folders = Folder.objects.filter(created_at__lte=timezone.now()).order_by('created_at')
    current_folder = get_object_or_404(Folder, id=id)
    tasks = Task.objects.filter(folder_id = current_folder.id)


    return render(request, 'index.html', {
        'folders':folders,
        'tasks':tasks,
        'current_folder_id': current_folder.id,
        })

def create_folder(request):
    if request.method == "POST":
        form = FolderForm(request.POST)
        if form.is_valid():
            folder = form.save(commit=False)
            folder.created_at = timezone.now()
            folder.save()
            return redirect('tasks.index', id=folder.id)
    else:
        form = FolderForm()
    return render(request, 'create_folders.html', {'form': form})



def create_task(request, id):
    #選ばれたフォルダを取得する
    current_folder = get_object_or_404(Folder, id=id)
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.created_at = timezone.now()
            task.folder_id = current_folder
            task.save()
            return redirect('tasks.index', id=current_folder.id)
    else:
        form = TaskForm()
    return render(request, 'create_tasks.html', {'form': form}, {'id':current_folder.id})


def edit_task(request, id, task_id):
    #選ばれたタスクを取得する
    task = get_object_or_404(Task, id=task_id)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            task = form.save(commit=False)
            task.save()
            return redirect('tasks.index', id=task.folder_id.id)
    else:
        form = TaskForm(instance=task)
    return render(request, 'edit.html', {'form': form}, {'task':task})

def feedback(request, id):
    current_task = get_object_or_404(Task, id=id)

    return render(request, 'feedback.html', {'id':current_task.id})

def signin(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(to='users/signin')
    else:
        form = SignUpForm()
        images = Image.objects.all()
        image = images[0]
    return render(request, 'signin.html', {'form': form,'image':image})

# Create your views here.
