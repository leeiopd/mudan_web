from django.contrib import admin
from .models import Year, Concert, Video, Team

# Register your models here.


class YearAdmin(admin.ModelAdmin):
    list_display = ('name',)


class ConcertAdmin(admin.ModelAdmin):
    list_display = ('name',)


class VideoAdmin(admin.ModelAdmin):
    list_display = ('song_title', )


class TeamAdmin(admin.ModelAdmin):
    list_display = ('name',)


admin.site.register(Year, YearAdmin)
admin.site.register(Concert, ConcertAdmin)
admin.site.register(Video, VideoAdmin)
admin.site.register(Team, TeamAdmin)
