from django.contrib import admin
from django.urls import path, include

urlpatterns=[
    path('',views.get_grading_parameters)
]
