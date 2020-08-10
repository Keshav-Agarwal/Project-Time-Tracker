from django.forms import ModelForm, ModelChoiceField, DateInput, EmailField
from .models import Tasks, TimeEntry
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class TaskForm(ModelForm):
    class Meta:
        model = Tasks
        exclude = ['started']

class TimeEntryForm(ModelForm):
    class Meta:
        model = TimeEntry
        fields = '__all__'


class RegisterForm(UserCreationForm):
    email = EmailField()

    class Meta:
	    model = User
	    fields = ["username", "email", "password1", "password2"]