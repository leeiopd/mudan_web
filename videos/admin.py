from django.contrib import admin
from .models import Year, Concert, Video, Team

# Register your models here.

class VideoAdmin(admin.ModelAdmin):
    list_display = ('song_title', )


class TeamAdmin(admin.ModelAdmin):
    list_display = ('name',)

class YearAdmin(admin.ModelAdmin):
    list_display = ('name',)


admin.site.register(Video, VideoAdmin)
admin.site.register(Team, TeamAdmin)
admin.site.register(Year, YearAdmin)
