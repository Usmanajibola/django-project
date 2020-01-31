from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth import urls
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import TemplateView

app_name = 'usmanajibolaabassscrumy'

urlpatterns=[
    path('',views.get_grading_parameters),
    path('accounts/signup', views.sign_up, name='signup'),
    path('login', views.login, name='login'),
    path('movegoal/<int:goal_id>', views.move_goal),
    path('addgoal', views.add_goal, name='addgoal'),
    path('home', views.home),
    path('accounts/', include(urls)),
    path('accounts/signupsuccess', views.signupsuccess, name='signupsuccess')
]
