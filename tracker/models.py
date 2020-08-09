from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Tasks(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200, default="-") 
    started = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class TimeEntry(models.Model):
    task = models.ForeignKey(Tasks, on_delete=models.CASCADE)
    start_time = models.DateTimeField(auto_now=False, auto_now_add=False)
    end_time = models.DateTimeField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return (str(self.task) + str(self.start_time) + str(self.end_time))