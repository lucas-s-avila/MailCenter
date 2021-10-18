from django.db import models
from django.utils.translation import gettext_lazy as _
from psqlextra.models import PostgresModel
from psqlextra.manager import PostgresManager

from mail_sender.tasks import send_email

class Account(PostgresModel):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=False)
    domain = models.TextField(blank=False)
    key = models.TextField(blank=False)

    objects = PostgresManager()

    class Meta:
        db_table = 'Account'

    def __str__(self):
        return self.name

class Email(PostgresModel):

    class EmailStatus(models.TextChoices):
        PENDING = 'PE', _('Pending')
        SENT = 'SE', _('Sent')
        FAILED = 'FA', _('Failed')

    id = models.BigAutoField(primary_key=True)
    sender = models.ForeignKey(Account, on_delete=models.CASCADE)
    subject = models.TextField(blank=False)
    status = models.CharField(max_length=2, choices=EmailStatus.choices, default=EmailStatus.PENDING)
    receivers = models.TextField(blank=False)
    body = models.TextField(blank=False)

    objects = PostgresManager()

    class Meta:
        db_table = 'Email'

    @property
    def get_receivers_list(self):
        return self.receivers.split('\n')

    @classmethod
    def post_create(cls, sender, instance, created, *args, **kwargs):
        if not created:
            return
        send_email.delay(
            instance.id, 
            instance.sender.name, 
            instance.get_receivers_list, 
            instance.subject, 
            instance.body,
            instance.sender.key,
            instance.sender.domain)

models.signals.post_save.connect(Email.post_create, sender=Email)