from django.dispatch import Signal

payment_received = Signal(providing_args=['bill_id'])
