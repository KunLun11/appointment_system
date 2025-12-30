from django.db.models import IntegerChoices


class ServiceStatusEnum(IntegerChoices):
    # created = 100, "Создана"
    active = 200, "Активна"
    booked = 300, "Забронирована"
    in_progress = 400, "Выполняется"
    completed = 500, "Завершена"
    cancelled = 600, "Отменена"


class TimeSlotStatusEnum(IntegerChoices):
    is_free = 1, "Свободен"
    is_book = 2, "Забронирован"
    is_cancel = 3, "Отменен"


class PaymentStatusEnum(IntegerChoices):
    is_wait = 1, "Ожидает"
    is_payed = 2, "Оплачен"
    is_return = 3, "Возврат"


class ScheduleTypeEnum(IntegerChoices):
    regular = 1, "Регулярное"
    one_time = 2, "Разовое"


class DayOfWeekEnum(IntegerChoices):
    monday = 1, "Понедельник"
    tuesday = 2, "Вторник"
    wednesday = 3, "Среда"
    thursday = 4, "Четверг"
    friday = 5, "Пятница"
    saturday = 6, "Суббота"
    sunday = 7, "Воскресенье"


class ServiceTypeEnum(IntegerChoices):
    # Терапевт
    terapy_primary = 101, "Первичная консультация терапевта"
    terapy_repeat = 102, "Повторная консультция терапевта"
    terapy_prevention = 103, "Профилактический осмотр"
    terapy_analysis = 104, "Расшифровка анализов"
    terapy_sick_leave = 105, "Выдача справки/больничного"
    terapy_vaccination = 106, "Вакцинация"
    terapy_ecg = 107, "ЭКГ с расшифровкой"
    terapy_pressure = 108, "Измерение давления/пульса"
    terapy_plan = 109, "Составление плана лечения"
    # Кардиолог
    cardio_primary = 201, "Первичная консультация кардиолога"
    cardio_repeat = 202, "Повторная консультация кардиолога"
    cardio_holter = 203, "Суточный мониторинг ЭКГ"
    cardio_echo = 204, "Эхокардиограмма (УЗИ сердца)"
    cardio_stress_test = 205, "Нагрузочные тесты"
    cardio_therapy = 206, "Подбор гипотензивной терапии"
    # Невролог
    neuro_primary = 301, "Консультация невролога"
    neuro_eeg = 302, "ЭЭГ"
    neuro_usg_vessels = 303, "УЗИ сосудов шеи/головы"
    neuro_blockade = 304, "Блокада при остеохондрозе"
    neuro_migraine = 305, "Лечение мигрени"
    neuro_reflex = 306, "Рефлексотерапия"
    # Стоматолог
    dentist_consult = 401, "Консултация стоматолога"
    dentist_hygiene = 402, "Профессиональная гигиена"
    dentist_caries = 403, "Лечение кариеса"
    dentist_simple = 404, "Удаление зуба простое"
    dentist_complex = 405, "Удаление зуба сложное"
    dentist_whitening = 406, "Отбеливание зубов"
    dentist_filling = 407, "Установка пломбы световой"
    # Офтальмолог
    ophthalmo_consult = 501, "Консультация офтальмолога"
    ophthalmo_glasses = 502, "Подбор очков/линз"
    ophthalmo_pressure = 503, "Измерение внутриглазного давления"
    ophthalmo_fundus = 504, "Осмотр глазного дна"
    ophthalmo_conjunctivitis = 505, "Лечение конъюнктивита"
    # Дерматолог
    derma_consult = 601, "Консультация дерматолога"
    derma_mole_removal = 602, "Удаление родинки/папилломы"
    derma_acne = 603, "Лечение акне"
    derma_cryotherapy = 604, "Криодеструкция"
    derma_biopsy = 605, "Биопсия кожи"
    # Педиатр
    pediatric_consult = 701, "Консультация педиатра"
    pediatric_newborn = 702, "Патронаж новорожденного"
    pediatric_vaccination = 703, "Вакцинация по календарю"
    pediatric_school_check = 704, "Осмотр перед садом/школой"
    # Хирург
    surgeon_consult = 801, "Консультация хирурга"
    surgeon_bandage = 802, "Перевязка"
    surgeon_abscess = 803, "Вскрытие абсцесса"
    surgeon_sutures = 804, "Наложение швов"
    surgeon_nail = 805, "Удаление вросшего ногтя"
    # Психолог/психтерапевт
    psych_consult = 901, "Консультация психолога"
    psych_therapy = 902, "Сеанс психотерапии"
    psych_medication = 903, "Подбор антидепрессантов"
    psych_family = 904, "Семейная консультация"
    # Гинеколог
    gynecologist_consult = 1001, "Консультация гинеколога"
    gynecologist_usg = 1002, "УЗИ органов малого таза"
    gynecologist_smear = 1003, "Взятие мазков"
    gynecologist_iud = 1004, "Установка/снятие ВМС"
    # Диашгностика
    diag_blood_general = 1101, "Общий анализ крови"
    diag_blood_biochem = 1102, "Биохимический анализ крови"
    diag_usg_abdomen = 1103, "УЗИ брюшной полости"
    diag_xray_chest = 1104, "Рентген грудной клетки"
    diag_mri_consult = 1105, "МРТ/КТ (консультация по результатам)"
    # Доп услуги
    online_consult = 1201, "Онлайн-консультация"
    home_visit = 1202, "Вызов врача на дом"
    home_analysis = 1203, "Забор анализов на дому"
    medical_docs = 1204, "Медицинская документация"


__all__ = [
    "ServiceStatusEnum",
    "TimeSlotStatusEnum",
    "PaymentStatusEnum",
    "ScheduleTypeEnum",
    "DayOfWeekEnum",
    "ServiceTypeEnum",
]
