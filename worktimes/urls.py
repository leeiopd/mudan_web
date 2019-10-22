from django.urls import path
from . import views

app_name = 'worktimes'

urlpatterns = [
    path('list/', views.list, name='list'),
    path('teamInfo/<int:teamId>/detail/', views.detail, name='detail')
]
