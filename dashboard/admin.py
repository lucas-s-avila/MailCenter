from django.contrib import admin

from dashboard.models import Email

@admin.register(Email)
class EmailAdmin(admin.ModelAdmin):
    fields = ('tittle', 'receivers', 'body')
    list_display = ('tittle', 'status', 'receivers')
    #TODO: button to send email
    search_fields = ('tittle', 'receivers', 'body',)