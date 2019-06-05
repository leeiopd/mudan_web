from django.urls import path
from . import views

app_name = 'worktimes'

urlpatterns = [
    path('', views.list, name='list'),
]