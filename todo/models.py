from django.conf import settings
from django.db import models
from django.utils import timezone

class Image(models.Model):
    picture = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title

class Folder(models.Model):
    now_date = timezone.localtime(timezone.now())
    title = models.CharField(max_length=20)
    created_at = models.DateTimeField(default=now_date)



class Task(models.Model):
    STATUS_CHOICES = [(1, '未完了'),(2, '作業中'),(3, '完了')]

    title = models.CharField(max_length=100)
    status = models.IntegerField(choices=STATUS_CHOICES, default=1)
    due_date =  models.DateField(default=timezone.now)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(blank=True, null=True)
    folder_id = models.ForeignKey(Folder, on_delete = models.CASCADE)

    def publish(self):
        self.update_at = timezone.now()
        self.save()




    def __str__(self):
        return self.title