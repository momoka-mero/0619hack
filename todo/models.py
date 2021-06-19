from django.conf import settings
from django.db import models
from django.utils import timezone






class Folder(models.Model):
    now_date = timezone.localtime(timezone.now())
    title = models.CharField(max_length=20)
    created_at = models.DateTimeField(default=now_date)

    def __str__(self):
        return self.title