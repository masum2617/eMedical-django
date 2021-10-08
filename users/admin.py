from django.contrib import admin
from .models import Account
from django.contrib.auth.admin import UserAdmin
# Register your models here.

class AccountAdmin(UserAdmin):
    list_display = ('email', 'first_name', 'last_name', 'user_type', 'last_login', 'date_joined', 'is_active')
    list_display_links = ('email', 'first_name', 'last_name')
    readonly_fields = ('last_login', 'date_joined')
    ordering = ('-date_joined',)

    # add_fieldsets = (
    #     (None, {
    #         'classes': ('wide',),
    #         'fields': ('email', 'first_name', 'last_name', 'user_type', 'phone_number' ,'password','is_staff', 'is_active','is_admin'),
    #     }),
    # )

    # fieldsets = (
    #     (None, {'fields': ('email', 'password', )}),
    #     ('Personal info', {'fields': ('first_name', 'last_name')}),
    #     ('Permissions', {'fields': ('is_admin','is_staff')}),
    # )

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Account, AccountAdmin)