from django.conf import settings
from qiwi_payments.kassa import QiwiKassa


def cancel_invoice(modeladmin, request, queryset):
    kassa = QiwiKassa(settings.QIWI_KASSA_SECRET_KEY)
    for item in queryset:
        invoice = kassa.cancel_bill(item.bill_id)
        item.status = invoice.status.value
        item.save()


def update_status(modeladmin, request, queryset):
    kassa = QiwiKassa(settings.QIWI_KASSA_SECRET_KEY)
    for item in queryset:
        invoice = kassa.check_bill(item.bill_id)
        item.status = invoice.status.value
        item.save()
