"""mudan_web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from notices import views

urlpatterns = [
    path('', views.list),
    path('admin/', admin.site.urls),
    path('notices/', include('notices.urls')),
    path('freetimes/', include('freetimes.urls')),
    path('worktimes/', include('worktimes.urls')),
    path('videos/', include('videos.urls')),
    path('members/', include('members.urls')),
    path('', include('pwa.urls')),
]