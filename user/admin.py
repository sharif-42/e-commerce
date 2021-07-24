from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _

from .models import User
from .forms import UserCreationForm, UserChangeForm


class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserChangeForm
    add_form = UserCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('username', 'email', 'is_admin', 'is_blocked', 'is_active', 'is_pending', 'is_dashboard_user')
    list_filter = ('is_admin', 'is_dashboard_user', 'is_blocked', 'is_pending')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info',
         {'fields': (
             'phone_number', 'email', 'first_name', 'mid_name', 'last_name',
             'is_active', 'is_blocked', 'is_dashboard_user', 'is_pending',
         )
         }),
        ('Permissions', {'fields': ('is_admin', 'user_permissions', 'groups')}),
        (_('Important dates'), {'fields': ('last_login', 'updated_at',)}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2')}
         ),
    )
    search_fields = ('username',)
    ordering = ('username',)
    filter_horizontal = ('groups', 'user_permissions',)


# Now register the new UserAdmin...
admin.site.register(User, UserAdmin)
