from django.urls import path
from . import views

app_name = 'freetimes'

urlpatterns = [
    path('', views.list, name='list'),
    path('<int:weekId>/<int:hourId>/', views.detail, name='detail')
]
