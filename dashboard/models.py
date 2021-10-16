from django.db import models
from django.utils.translation import gettext_lazy as _

class Email(models.Model):

    class EmailStatus(models.TextChoices):
        PENDING = 'PE', _('Pending')
        SENT = 'SE', _('Sent')
        FAILED = 'FA', _('Failed')

    id = models.BigAutoField(primary_key=True)
    tittle = models.TextField(blank=False)
    status = models.CharField(max_length=2, choices=EmailStatus.choices, default=EmailStatus.PENDING)
    receivers = models.TextField(blank=False)
    body = models.TextField(blank=False)

    class Meta:
        db_table = 'Email'
