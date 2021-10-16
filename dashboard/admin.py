from django.contrib import admin
from dashboard.models import Email

@admin.register(Email)
class EmailAdmin(admin.ModelAdmin):
    list_display = ('subject', 'status', 'sender_name', 'receivers')
    fields = ('sender_name', 'subject', 'receivers', 'body')
    #TODO: button to send email
    search_fields = ('subject', 'receivers', 'body','sender_name', )