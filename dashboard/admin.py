from django.contrib import admin
from django.contrib.auth import models
from dashboard.models import Email, Account

admin.site.unregister(models.User)
admin.site.unregister(models.Group)

@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ('name', 'domain')
    fields = ('name', 'domain', 'key')
    search_fields = ('name', 'domain',)

@admin.register(Email)
class EmailAdmin(admin.ModelAdmin):
    list_display = ('subject', 'status', 'get_name', 'get_domain', 'receivers')
    fields = ('sender', 'subject', 'receivers', 'body')
    search_fields = ('subject', 'receivers', 'body', )

    @admin.display(ordering='sender__name', description='name')
    def get_name(self, obj):
        return obj.sender.name

    @admin.display(ordering='sender__domain', description='domain')
    def get_domain(self, obj):
        return obj.sender.domain