from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

class CustomUserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('username', 'first_name', 'last_name', 'email', 'is_admin', 'is_active','is_superuser','last_login')
    list_filter = ('is_admin', 'is_active','is_superuser',)
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email',)}),
        ('Permissions', {'fields': ('is_admin','is_active','is_superuser','groups','user_permissions',)}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'first_name', 'last_name', 'email', 'password1', 'password2'),
        }),
    )
    search_fields = ('email','first_name', 'last_name')
    ordering = ('username', 'first_name', 'last_name', 'email')

admin.site.register(CustomUser, CustomUserAdmin)
