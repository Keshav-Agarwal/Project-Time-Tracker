from django.contrib import admin
from .models import Tasks, TimeEntry

# Register your models here.
admin.site.register(Tasks)
admin.site.register(TimeEntry)