from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponseNotAllowed, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login
from django.shortcuts import get_object_or_404


from .forms import TaskForm, TimeEntryForm, RegisterForm
from .models import TimeEntry, Tasks

from datetime import datetime
from django.db.models import Sum


# Create your views here.
@login_required
def home(request):
    tasks = Tasks.objects.filter(user=request.user)
    times = TimeEntry.objects.filter(task__user=request.user).order_by("-pk")
    return render(request, 'tracker/home.html', {'tasks': tasks, 'times': times})


@login_required
def add_task(request):
    if request.method == 'POST':
        form = TaskForm()
        instance = form.save(commit=False)

        # Checking if the data has been received. Else redirecting to home with a message
        try:
            instance.name = request.POST.get("name")
            instance.user = request.user
        except Exception:
            return HttpResponseRedirect(reverse('home'), {'error': "Error while saving new project. Please enter all the fields properly."})
        instance.save()
        return HttpResponseRedirect(reverse('home'))
    else:
        return HttpResponseRedirect(reverse('home'),)


@login_required
def record_time(request):
    if request.method == 'POST':
        try:
            start_time = int(request.POST.get("start_time"))
            end_time = int(request.POST.get("end_time"))
            task = request.POST.get("task")
            description = request.POST.get("description")
            # Changing time from timestamp to datetime instance
            start_time = datetime.utcfromtimestamp(start_time/1000)
            end_time = datetime.utcfromtimestamp(end_time/1000)

            form = TimeEntryForm()
            instance = form.save(commit=False)
            instance.start_time = start_time
            instance.end_time = end_time
            instance.task = Tasks.objects.get(pk=task)
            instance.description = description
            instance.save()
            return HttpResponseRedirect(reverse('home'),)

        except Exception:
            return HttpResponseRedirect(reverse('home'), {'error': "Error while saving new time. Please check if project has been selected from dropdown menu."})
    return HttpResponseRedirect(reverse('home'),)


@login_required
def detail(request, *args, **kwargs):
    id = kwargs["id"]
    tasks = Tasks.objects.filter(user=request.user)
    if Tasks.objects.get(pk=id).user == request.user:
        times = TimeEntry.objects.filter(task=id).order_by("-pk")
        taskname = Tasks.objects.get(pk=id)
        return render(request, 'tracker/detail.html', {'tasks': tasks, 'times': times, 'taskname':taskname})
    else:
        return HttpResponseRedirect(reverse('home'), {'error': "Unauthorized to access"})


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = request.POST['username']
            password = request.POST['password1']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('home'),)

    form = RegisterForm()
    return render(request, "registration/register.html", {"form": form})


@login_required
def signout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'),)



