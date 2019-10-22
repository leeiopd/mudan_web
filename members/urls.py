from django.urls import path
from . import views

app_name = 'members'

urlpatterns = [
    path('list/', views.list, name='list'),
    path('<int:member_pk>/detail/', views.detail, name='detail')
]
