from django.db.models import IntegerChoices


class SpecializationEnum(IntegerChoices):
    therapist_general = 0, "Терапевт(общая)"
    cardiologist = 1, "Кардиолог"
    neurologist = 2, "Невролог"
    dermatologist = 3, "Дерматолог"
    dentist = 4, "Стоматолог"
    pediatrician = 5, "Педиатр"
    surgeon = 6, "Хирург"
    psychologist = 7, "Психолог"
    gynecologist = 8, "Гинеколог"
    ophthalmologist = 9, "Офтальмолог"


class QualificationsEnum(IntegerChoices):
    intern = 0, "Интерн"
    junior_specialist = 1, "Младший специалист"
    specialist = 2, "Специалист"
    senior_specialist = 3, "Старший специалист"
    leading_specialist = 4, "Ведущий специалист"
    main_expert = 5, "Главный специалист"
    doctor_high = 6, "Врач высшей категории"
    candidate_sciences = 7, "Кандидат наук"
    doctor_sciences = 8, "Доктор наук"
    professor = 9, "Профессор"


class EducationEnum(IntegerChoices):
    avg_prof = 0, "Среднее профессиональное"
    unfinish_high = 1, "Неоконченное высшее"
    bachelor = 2, "Бакалавр"
    specialist = 3, "Специалист"
    master = 4, "Магистр"
    aspir = 5, "Аспирантура"
    doctor = 6, "Докторнатура"
    mba = 7, "MBA"


__all__ = [
    "SpecializationEnum",
    "QualificationsEnum",
    "EducationEnum",
]
