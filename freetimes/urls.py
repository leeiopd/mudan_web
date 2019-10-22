from django.urls import path
from . import views

app_name = 'freetimes'

urlpatterns = [
    path('list/', views.list, name='list'),
    path('<int:weekId>/<int:hourId>/timeInfo/', views.detail, name='detail')
]
