from django.shortcuts import render
from django.utils import timezone
from .models import Folder

def index(request, id):
    folders = Folder.objects.filter(created_at__lte=timezone.now()).order_by('created_at')
    return render(request, 'index.html', {'folders':folders})

# Create your views here.
