from django.urls import path
from django.contrib.auth import views as auth_views


from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add_task', views.add_task, name='add_task'),
    path('record_time', views.record_time, name='record_time'),
    path('detail/<int:id>', views.detail, name='detail'),
    path("register/", views.register, name="register"),  
    path("signout/", views.signout, name="signout"),  
]
