# Django Qiwi Kassa

## Description
Django app to work with Qiwi Kassa


## Install
```
pip install django-qiwi-kassa
```

Add `qiwi_kassa` to INSTALLED_APPS

### Step 1.

Append `qiwi_kassa` to INSTALLED_APPS in settings.py:

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'qiwi_kassa',
]
```

### Step 2.
Add to `settings.py` QIWI_KASSA_SECRET_KEY constant:

```python
QIWI_KASSA_SECRET_KEY = 'QIWI_KASSA_SECRET_KEY'
```

## Payment notifications

If you want to set up POST notifications from Qiwi when payment is received, you have to add `qiwi_kassa.urls` in your project urls:

```python
urlpatterns.append(
    path('qiwi/', include(('qiwi_kassa.urls', 'qiwi_payments'), namespace='qiwi')),
)
```

Then you notification URL will be:
`<your_hostname>/qiwi/notify/`

When payments is received and signatures are OK the `payment_received` signal will be broadcasted.
Here is an example how to handle the signal:

```python
from django.dispatch import receiver
from qiwi_kassa.models import Invoice
from qiwi_kassa.signals import payment_received
from qiwi_payments.constants import PaymentStatus

@receiver(payment_received, sender=Invoice)
def payment_handler(sender, **kwargs):
    bill_id = kwargs.get('bill_id')
    invoice = Invoice.objects.get(bill_id=bill_id)
    invoice.status = PaymentStatus.PAID
    invoice.save()
    print('$$$$!')
```
