from django.contrib import admin
from .models import Workweek, Workhour, Nowsong, Nowteam

# Register your models here.


class WorkweekAdmin(admin.ModelAdmin):
    list_display = ('day',)


class WorkhourAdmin(admin.ModelAdmin):
    list_display = ('clock',)


class NowsongAdmin(admin.ModelAdmin):
    list_display = ('title', 'band',)


class NowteamAdmin(admin.ModelAdmin):
    list_display = ('name',)


admin.site.register(Workweek, WorkweekAdmin)
admin.site.register(Workhour, WorkhourAdmin)
admin.site.register(Nowsong, NowsongAdmin)
admin.site.register(Nowteam, NowteamAdmin)
