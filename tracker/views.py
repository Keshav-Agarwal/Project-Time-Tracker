from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login


from .forms import TaskForm, TimeEntryForm, RegisterForm
from .models import TimeEntry, Tasks

from datetime import datetime
from django.db.models import Sum



# Create your views here.
@login_required
def home(request):
    tasks = Tasks.objects.filter(user = request.user)
    times = TimeEntry.objects.filter(task__user = request.user).order_by("-pk")
    print("\n\n**********************\n\n")
    print(request)
    return render(request, 'tracker/home.html', {'tasks':tasks, 'times':times})

@login_required
def add_task(request):
    print(request)
    if request.method == 'POST':
        form = TaskForm()
        instance = form.save(commit=False)
        instance.name = request.POST.get("name")
        instance.user = request.user
        instance.save()
        return HttpResponseRedirect(reverse('home'))

        
    else:
        print("not post")




@login_required
def record_time(request):
    if request.method == 'POST':
        start_time = int(request.POST.get("start_time"))
        end_time = int(request.POST.get("end_time"))
        task = request.POST.get("task")
        start_time = datetime.utcfromtimestamp(start_time/1000)
        end_time = datetime.utcfromtimestamp(end_time/1000)
    
        form = TimeEntryForm()
        instance=form.save(commit=False)
        instance.start_time = start_time
        instance.end_time = end_time
        instance.task = Tasks.objects.get(pk=task)
        instance.save()
        return HttpResponseRedirect(reverse('home'),)


    return HttpResponseRedirect(reverse('home'),)

@login_required
def detail(request, *args, **kwargs):
    print("\n\n\n\n\n\n")
    id = kwargs["id"]
    print("here")
    print(id)
    tasks = Tasks.objects.filter(user = request.user)
    if Tasks.objects.get(pk=id).user == request.user:
        times = TimeEntry.objects.filter(task=id).order_by("-pk")
        return render(request, 'tracker/detail.html', {'tasks':tasks, 'times':times})
    else:
        ("bruh")
    print("\n\n\n\n\n\n")



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
    return render(request, "registration/register.html", {"form":form})


@login_required
def signout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'),)