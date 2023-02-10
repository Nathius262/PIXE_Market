from django.contrib import admin
from django.contrib.auth.models import Group
from .models import CustomUser


# Register your models here.
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'phone', 'is_admin', 'is_staff')
    search_fields = ('email', 'phone')
    readonly_fields = ()
    list_editable = ()

    filter_horizontal = ()
    list_filter = ('is_admin', 'is_staff')
    fieldsets = ()


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.unregister(Group)