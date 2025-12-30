from django.db import models

from apps.appointment.enums import ServiceStatusEnum
from apps.core.models.bases import BaseModelIDTime


class Appointment(BaseModelIDTime):
    class Meta:
        verbose_name = "Бронирование"
        verbose_name_plural = "Бронирования"

    title = models.CharField("Название", max_length=125)
    service = models.ForeignKey(
        "appointment.Service",
        on_delete=models.SET_NULL,
        verbose_name="Услуга",
        related_name="appointment",
        null=True,
        blank=True,
    )
    client = models.ForeignKey(
        "employee.Client",
        on_delete=models.SET_NULL,
        verbose_name="Клиент",
        related_name="appointment",
        null=True,
        blank=True,
    )
    specialist = models.ForeignKey(
        "employee.Specialist",
        on_delete=models.SET_NULL,
        verbose_name="Специалист",
        related_name="appointment",
        null=True,
        blank=True,
    )
    time_slot = models.OneToOneField(
        "appointment.TimeSlot",
        on_delete=models.SET_NULL,
        verbose_name="Слот",
        related_name="appointment",
        null=True,
        blank=True,
    )
    client_notes = models.TextField("Запись клиента", max_length=500, blank=True)
    specialist_notes = models.TextField(
        "Запись специалиста", max_length=500, blank=True
    )
    status_enum = models.PositiveSmallIntegerField(
        "Статус бронирования",
        choices=ServiceStatusEnum.choices,
    )


__all__ = [
    "Appointment",
]
