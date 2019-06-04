from django.urls import path
from . import views

app_name = 'videos'

urlpatterns = [
    path('', views.list, name='list'),
    path('<int:video_pk>/watch/', views.watch, name='watch'),
    path('<int:team_pk>/detail/', views.detail, name='detail')
]