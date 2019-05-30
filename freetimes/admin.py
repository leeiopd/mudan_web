from django.contrib import admin
from .models import Freeweek, Freehour, Table

# Register your models here.


class FreeweekAdmin(admin.ModelAdmin):
    list_display = ('day',)


class FreehourAdmin(admin.ModelAdmin):
    list_display = ('clock',)


class TableAdmin(admin.ModelAdmin):
    list_display = ('week', 'hour')


admin.site.register(Freeweek, FreeweekAdmin)
admin.site.register(Freehour, FreehourAdmin)
admin.site.register(Table, TableAdmin)

