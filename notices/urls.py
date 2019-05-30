from django.urls import path
from . import views

app_name = 'notices'

urlpatterns = [
    path('', views.list, name='list'),
    path('create/', views.create, name='create'),
    path('<int:notice_pk>/detail/', views.detail, name='detail'),
    path('<int:notice_pk>/delete/', views.delete, name='delete'),
    path('<int:notice_pk>/update/', views.update, name='update'),
    path('onenotice/', views.onenotice, name='onenotice')
]