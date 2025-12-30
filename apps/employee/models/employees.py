from django.db import models

from apps.employee.enums import SpecializationEnum, EducationEnum
from apps.core.models.bases import BaseModelIDTime, BaseModelID
from apps.core.models.profiles import BaseProfile


class Specialist(BaseModelIDTime):
    class Meta:
        verbose_name = "Специалист"
        verbose_name_plural = "Специалисты"

    user = models.ForeignKey(
        "account.CustomUser",
        on_delete=models.SET_NULL,
        verbose_name="Пользователь",
        related_name="specialists",
        null=True,
        blank=True,
    )
    profile = models.OneToOneField(
        "employee.SpecialistProfile",
        on_delete=models.CASCADE,
        verbose_name="Профиль",
        related_name="specialists",
    )

    def __str__(self):
        return f"{self.profile.fio_name} - {self.profile.prof_info.get_specialization_enum_display()}"


class SpecialistProfile(BaseProfile):
    class Meta:
        verbose_name = "Профиль специалиста"
        verbose_name_plural = "Профили специалистов"

    prof_info = models.OneToOneField(
        "employee.SpecialistProfessionalInfo",
        on_delete=models.CASCADE,
        verbose_name="Профессиональные данные",
        related_name="profiles",
    )
    settings = models.OneToOneField(
        "employee.SpecialistSettings",
        on_delete=models.CASCADE,
        verbose_name="Настройки",
        related_name="profiles",
        null=True,
        blank=True,
    )
    rating = models.DecimalField(
        "Рейтинг",
        max_digits=3,
        decimal_places=2,
        default=0.0,
    )
    review_count = models.PositiveIntegerField("Количество отзывов", default=0)

    @property
    def fio_name(self) -> str:
        return f"№{self.pk}: {self.last_name} {self.first_name} {self.middle_name}"

    def __str__(self):
        return f"Профиль №{self.pk}"


class SpecialistProfessionalInfo(BaseModelID):
    class Meta:
        verbose_name = "Профессиональные данные"
        verbose_name_plural = "Профессиональные данные"

    specialization_enum = models.PositiveSmallIntegerField(
        "Специализация",
        choices=SpecializationEnum.choices,
        default=SpecializationEnum.therapist_general,
    )
    education_enum = models.PositiveSmallIntegerField(
        "Образование",
        choices=EducationEnum.choices,
        default=EducationEnum.specialist,
    )
    work_exp = models.PositiveIntegerField("Опыт работы", default=0)

    def __str__(self):
        return f"№{self.pk}: {self.get_specialization_enum_display()}"


class SpecialistSettings(BaseModelIDTime):
    class Meta:
        verbose_name = "Настройки специалиста"
        verbose_name_plural = "Настройки специалиста"

    is_add = models.BooleanField("Принимает новый клиентов", default=True)
    time_to_answer = models.PositiveIntegerField("Время ответа на запрос", default=2)
    auto_confirm = models.BooleanField("Автоподтверждение", default=False)


class ProfileClient(BaseProfile):
    class Meta:
        verbose_name = "Профиль клиента"
        verbose_name_plural = "Профили клиентов"

    first_booking_date = models.DateTimeField("Первое бронирование", auto_now_add=True)

    @property
    def fio_name(self) -> str:
        return f"№{self.pk}: {self.last_name} {self.first_name} {self.middle_name}"

    def __str__(self):
        return f"Профиль №{self.pk}"


class Client(BaseModelIDTime):
    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"

    user = models.ForeignKey(
        "account.CustomUser",
        on_delete=models.SET_NULL,
        verbose_name="Пользователь",
        related_name="client",
        null=True,
        blank=True,
    )
    profile = models.ForeignKey(
        "employee.ProfileClient",
        on_delete=models.CASCADE,
        verbose_name="Профиль клиента",
        related_name="client",
    )

    def __str__(self):
        return f"{self.profile.fio_name}"


__all__ = [
    "Specialist",
    "SpecialistProfile",
    "SpecialistProfessionalInfo",
    "SpecialistSettings",
    "ProfileClient",
    "Client",
]
