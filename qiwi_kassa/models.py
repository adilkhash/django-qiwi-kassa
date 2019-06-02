from django.db import models
from django.utils.translation import ugettext as _
from qiwi_payments.constants import PaymentStatus


class Invoice(models.Model):
    bill_id = models.UUIDField(_('Bill ID'), db_index=True, unique=True)
    status = models.CharField(_('Status'), max_length=16, choices=PaymentStatus.choices())
    amount = models.DecimalField(_('Amount'), max_digits=11, decimal_places=2)
    currency = models.CharField(_('Currency Code'), max_length=3, default='RUB')
    payment_url = models.URLField(_('Payment URL'), max_length=254)
    expiration_dt = models.DateTimeField(_('Expiration Date & Time'))
    created = models.DateTimeField(_('Created'), auto_now_add=True)
    updated = models.DateTimeField(_('Updated'), auto_now=True)

    def __str__(self):
        return str(self.bill_id)

    class Meta:
        verbose_name = _('Invoice')
        verbose_name_plural = _('Invoices')
