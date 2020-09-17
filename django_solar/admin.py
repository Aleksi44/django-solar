from django.contrib import admin

from .models import Mail


class MailAdmin(admin.ModelAdmin):
    search_fields = ('mail',)
    list_display = ('__str__', 'mail', 'is_send', 'send_at')


admin.site.register(Mail, MailAdmin)
