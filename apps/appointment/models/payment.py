from django.db import models

from apps.appointment.enums import PaymentStatusEnum
from apps.core.models.bases import BaseModelIDTime


class Payment(BaseModelIDTime):
    class Meta:
        verbose_name = "Оплата"
        verbose_name_plural = "Оплата"

    appointment = models.OneToOneField(
        "appointment.Appointment",
        on_delete=models.SET_NULL,
        verbose_name="Бронь",
        related_name="payment",
        null=True,
        blank=True,
    )
    amount = models.DecimalField(
        "Стоимость услуги",
        max_digits=12,
        decimal_places=2,
    )
    status_enum = models.PositiveSmallIntegerField(
        "Статус оплаты",
        choices=PaymentStatusEnum.choices,
        default=PaymentStatusEnum.is_wait,
    )
    payment_method = models.CharField("Метод оплаты", max_length=125)
    transaction_id = models.CharField("id транзакции", max_length=128, blank=True)


__all__ = [
    "Payment",
]
