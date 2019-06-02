import json
import logging

from django.conf import settings
from django.views.generic import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.http import HttpResponseBadRequest, JsonResponse
from qiwi_payments.models import Invoice as QiwiInvoice
from qiwi_payments.utils import generate_hmac_hash

from qiwi_kassa.signals import payment_received
from qiwi_kassa.models import Invoice


logger = logging.getLogger(__name__)


class PaymentNotificationView(View):
    """
        Payment notification URL
        Read the docs: https://developer.qiwi.com/ru/bill-payments/?shell#notification
        If payment was successful, payment_received signal will be send
    """
    def post(self, request):
        try:
            payload = json.loads(request.body)
        except json.JSONDecodeError:
            logger.error('Invalid payload {}'.format(request.body))
            return HttpResponseBadRequest('Invalid json')
        else:
            logger.debug('Received following payload: {}'.format(request.body))
            invoice = QiwiInvoice.prepare(payload['bill'])
            signature = generate_hmac_hash(invoice, settings.QIWI_KASSA_SECRET_KEY)
            if signature == request.META['HTTP_X_API_SIGNATURE_SHA256']:
                logger.debug('Payment for {} has been received'.format(invoice.bill_id))
                payment_received.send(
                    sender=Invoice,
                    bill_id=invoice.bill_id
                )
            return JsonResponse({'error': 0})  # OK

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
