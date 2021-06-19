from django.contrib import admin
from django.utils import timezone
from .models import Folder, Task

admin.site.register(Folder)
admin.site.register(Task)

# Register your models here.
