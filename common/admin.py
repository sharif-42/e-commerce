from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from .models import EmailTemplate


class ReadOnlyAdmin(admin.ModelAdmin):
    readonly_fields = ('uuid', 'created_at', 'updated_at')


class EmailTemplateAdmin(ReadOnlyAdmin):
    list_display = ('mail_type', 'subject', 'mail_text')

    fieldsets = (
        ('Required Fields', {'fields': ('uuid', 'mail_type', 'subject', 'mail_text')}),
        ('Additional Fields', {'fields': ('created_by', 'updated_by')}),
        (_('Important dates'), {'fields': ('created_at', 'updated_at',)}),
    )


admin.site.register(EmailTemplate, EmailTemplateAdmin)
