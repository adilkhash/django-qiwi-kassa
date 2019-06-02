from django.contrib import admin
from django.utils.translation import ugettext as _

from qiwi_kassa.models import Invoice
from qiwi_kassa.actions import cancel_invoice, update_status


cancel_invoice.short_description = _('Cancel invoice')
update_status.short_description = _('Update invoice status')


class InvoiceAdmin(admin.ModelAdmin):
    list_display = ['bill_id', 'status', 'currency', 'amount', 'created']
    actions = [cancel_invoice, update_status]


admin.site.register(Invoice, InvoiceAdmin)
