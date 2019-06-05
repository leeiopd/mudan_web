from django.contrib import admin
from .models import Freeweek, Freehour, Table

# Register your models here.
class TableAdmin(admin.ModelAdmin):
    list_display = ('week', 'hour')

admin.site.register(Table, TableAdmin)

