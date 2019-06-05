from django.contrib import admin
from .models import Member, Part, MudanNo, UniveNo, Alive, Major

# Register your models here.


class MemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'mudanNo', 'part',)


class MudanNoAdmin(admin.ModelAdmin):
    list_display = ('num',)


class UniveNoAdmin(admin.ModelAdmin):
    list_display = ('num',)


class MajorAdmin(admin.ModelAdmin):
    list_display = ('title',)


admin.site.register(Member, MemberAdmin)
admin.site.register(MudanNo, MudanNoAdmin)
admin.site.register(UniveNo, UniveNoAdmin)
admin.site.register(Major, MajorAdmin)
