from django.contrib import admin
from django.utils import timezone
from .models import Folder, Task, Image

admin.site.register(Folder)
admin.site.register(Task)
admin.site.register(Image)
# Register your models here.
