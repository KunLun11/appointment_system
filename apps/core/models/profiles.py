from django.db import models

from apps.core.models.bases import BaseModelIDTime


class FIOFields(models.Model):
    class Meta:
        verbose_name = "ФИО"
        verbose_name_plural = "ФИО"
        abstract = True

    first_name = models.CharField("Имя", max_length=100)
    last_name = models.CharField("Фамилия", max_length=100)
    middle_name = models.CharField("Отчество", max_length=100, blank=True)

    @property
    def full_name(self):
        return f"{self.last_name} {self.first_name} {self.middle_name}".strip()


class BaseProfile(BaseModelIDTime, FIOFields):
    class Meta:
        verbose_name = "Базовый профиль"
        verbose_name_plural = "Базовые профили"
        abstract = True
        ordering = ["last_name", "first_name"]

    phone = models.CharField("Телефон", max_length=20, blank=True)
    email = models.EmailField("Email", blank=True)
    birth_date = models.DateField("Дата рождения", null=True, blank=True)
    photo = models.ImageField("Фото", upload_to="photo_base_profile/", blank=True)


__all__ = [
    "FIOFields",
    "BaseProfile",
]
