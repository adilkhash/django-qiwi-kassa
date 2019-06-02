from django.urls import path

from qiwi_kassa.views import PaymentNotificationView

urlpatterns = [
    path('notify/', PaymentNotificationView.as_view(), name='notification')
]
