from django.core.validators import MaxLengthValidator
from django.db import models

from apps.core.models.bases import BaseModelIDTime


class Review(BaseModelIDTime):
    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"

    appointment = models.OneToOneField(
        "appointment.Appointment",
        on_delete=models.SET_NULL,
        verbose_name="Бронь",
        related_name="review",
        null=True,
        blank=True,
    )
    client = models.ForeignKey(
        "employee.Client",
        on_delete=models.SET_NULL,
        verbose_name="Клиент",
        related_name="review",
        null=True,
        blank=True,
    )
    specialist = models.ForeignKey(
        "employee.Specialist",
        on_delete=models.SET_NULL,
        verbose_name="Специалист",
        related_name="review",
        null=True,
        blank=True,
    )
    rating = models.DecimalField(
        "Рейтинг",
        max_digits=3,
        decimal_places=2,
        default=0.0,
    )
    comment = models.TextField("Комментарий", validators=[MaxLengthValidator(510)])
    is_published = models.BooleanField("Опуликовано", default=False)


__all__ = [
    "Review",
]
