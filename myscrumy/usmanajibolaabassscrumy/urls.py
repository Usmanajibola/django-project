from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth import urls

app_name = 'usmanajibolaabassscrumy'

urlpatterns=[
    #path('',views.get_grading_parameters),
    path('accounts/login', views.index, name='about'),
    path('movegoal/<int:goal_id>', views.move_goal),
    path('addgoal', views.add_goal, name='addgoal'),
    path('home', views.home),
    path('accounts/', include(urls))
]
