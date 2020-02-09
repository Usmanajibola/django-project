from django.urls import path, include
from . import views


urlpatterns = [
path('test/', views.test, name='test'),
path('disconnect/', views.disconnect),
path('connect/', views.connect),
path('send_message/', views.send_message),
path('get_recentmessages/', views.get_recentmessages),
]
