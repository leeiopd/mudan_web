from django.contrib import admin
from .models import Workweek, Workhour, Nowsong, Nowteam, Table

# Register your models here.


class NowsongAdmin(admin.ModelAdmin):
    list_display = ('title', 'band',)


class NowteamAdmin(admin.ModelAdmin):
    list_display = ('name',)

class TableAdmin(admin.ModelAdmin):
    list_display = ('nowteam', 'week', 'hour',)


admin.site.register(Nowsong, NowsongAdmin)
admin.site.register(Nowteam, NowteamAdmin)
admin.site.register(Table, TableAdmin)
