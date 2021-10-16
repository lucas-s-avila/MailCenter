from django.db import models
from django.utils.translation import gettext_lazy as _

from mail_sender.tasks import send_email

class Email(models.Model):

    class EmailStatus(models.TextChoices):
        PENDING = 'PE', _('Pending')
        SENT = 'SE', _('Sent')
        FAILED = 'FA', _('Failed')

    id = models.BigAutoField(primary_key=True)
    sender_name = models.TextField(blank=False)
    subject = models.TextField(blank=False)
    status = models.CharField(max_length=2, choices=EmailStatus.choices, default=EmailStatus.PENDING)
    receivers = models.TextField(blank=False)
    body = models.TextField(blank=False)

    class Meta:
        db_table = 'Email'

    @property
    def get_receivers_list(self):
        return self.receivers.split('\n')

    @classmethod
    def post_create(cls, sender, instance, created, *args, **kwargs):
        if not created:
            return
        send_email.delay(instance.id, instance.sender_name, instance.subject, instance.get_receivers_list, instance.body)

models.signals.post_save.connect(Email.post_create, sender=Email)