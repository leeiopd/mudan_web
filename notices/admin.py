from django.contrib import admin
from .models import Onenotice

# Register your models here.


class OnenoticeAdmin(admin.ModelAdmin):
    list_display = ('content',)


admin.site.register(Onenotice, OnenoticeAdmin)
