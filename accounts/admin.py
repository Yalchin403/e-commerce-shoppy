from django.contrib import admin
from .models import Account
from django.contrib.auth.admin import UserAdmin


class AccountAdmin(UserAdmin):
    # list display - names that will be shown in view of account rows not in detailed view
    list_display = ('email', 'first_name', 'last_name', 'username',
                    'last_login', 'is_active', 'is_superadmin')
    list_display_links = ('email', 'first_name', 'last_name', 'username')
    readonly_fields = ('date_joined', 'last_login')
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
    ordering = ("-date_joined",)


admin.site.register(Account, AccountAdmin)
