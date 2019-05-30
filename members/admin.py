from django.contrib import admin
from .models import Member, Part, MudanNo, UniveNo, Alive, Major

# Register your models here.


class MemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'mudanNo', 'part',)


class PartAdmin(admin.ModelAdmin):
    list_display = ('name',)


class MudanNoAdmin(admin.ModelAdmin):
    list_display = ('num',)


class UniveNoAdmin(admin.ModelAdmin):
    list_display = ('num',)


class AliveAdmin(admin.ModelAdmin):
    list_display = ('content',)


class MajorAdmin(admin.ModelAdmin):
    list_display = ('title',)


admin.site.register(Member, MemberAdmin)
admin.site.register(Part, PartAdmin)
admin.site.register(MudanNo, MudanNoAdmin)
admin.site.register(UniveNo, UniveNoAdmin)
admin.site.register(Alive, AliveAdmin)
admin.site.register(Major, MajorAdmin)
