from django.db import models

from apps.appointment.enums import (
    DayOfWeekEnum,
    ScheduleTypeEnum,
    ServiceTypeEnum,
    TimeSlotStatusEnum,
)
from apps.core.models.bases import BaseModelIDTime


class Service(BaseModelIDTime):
    class Meta:
        verbose_name = "Услуга"
        verbose_name_plural = "Услуги"

    title = models.CharField("Название", max_length=120, blank=True)
    servie_price = models.OneToOneField(
        "appointment.ServicePrice",
        on_delete=models.CASCADE,
        verbose_name="Стоимость услуги",
        related_name="service",
    )

    def __str__(self):
        return f"№{self.pk}:{self.title}"


class ServicePrice(BaseModelIDTime):
    class Meta:
        verbose_name = "Стоимость услуги"
        verbose_name_plural = "Стоимость услуг"

    service_type_enum = models.PositiveSmallIntegerField(
        "Вид услуги",
        choices=ServiceTypeEnum.choices,
    )
    amount = models.DecimalField(
        "Цена",
        max_digits=12,
        decimal_places=2,
    )

    def __str__(self):
        return f"{self.get_service_type_enum_display()}:{(self.amount)} рублей"


class TimeSlot(BaseModelIDTime):
    class Meta:
        verbose_name = "Слот"
        verbose_name_plural = "Слоты"

    specialist = models.ForeignKey(
        "employee.Specialist",
        on_delete=models.SET_NULL,
        verbose_name="Специалист",
        related_name="time_slot",
        null=True,
        blank=True,
    )
    start_at = models.DateTimeField("Начало в")
    end_at = models.DateTimeField("Окончание в")
    status_enum = models.PositiveSmallIntegerField(
        "Статус слота",
        choices=TimeSlotStatusEnum.choices,
        default=TimeSlotStatusEnum.is_free,
    )
    service_type_enum = models.PositiveSmallIntegerField(
        "Вид услуги",
        choices=ServiceTypeEnum.choices,
    )

    def __str__(self):
        return f"№{self.pk}: {self.get_service_type_enum_display()}"


class Schedule(BaseModelIDTime):
    class Meta:
        verbose_name = "Расписание"
        verbose_name_plural = "Расписания"

    specialist = models.ForeignKey(
        "employee.Specialist",
        on_delete=models.CASCADE,
        verbose_name="Специалист",
        related_name="schedule",
    )
    schedule_type = models.PositiveSmallIntegerField(
        "Тип расписания",
        choices=ScheduleTypeEnum.choices,
        default=ScheduleTypeEnum.regular,
    )
    day_of_week = models.PositiveSmallIntegerField(
        "День недели",
        choices=DayOfWeekEnum.choices,
        null=True,
        blank=True,
    )
    start_at = models.TimeField("Время начала")
    end_at = models.TimeField("Время окончания")
    is_active = models.BooleanField("Активно", default=True)

    def __str__(self):
        return f"№{self.pk}: {self.get_day_of_week_display()}"


__all__ = [
    "Service",
    "ServicePrice",
    "TimeSlot",
    "Schedule",
]
