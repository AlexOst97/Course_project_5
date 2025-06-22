from datetime import timedelta
from rest_framework.exceptions import ValidationError


class SimultaneousSelectionValidator:
    """Одновременный выбор связанной привычки и указания вознаграждения"""

    def __init__(self, field):
        self.field = field

    def __call__(self, habit):
        if habit.get('associted_habit') and habit.get('reward'):
            raise ValidationError("Недопустимо одновременный выбор связанной привычки и указания вознаграждения")


class LeadTimeValidator:
    """Время выполнения должно быть не больше 120 секунд"""

    def __init__(self, field):
        self.field = field

    def __call__(self, habit):
        if habit.get('time_to_complete') > 120:
            raise ValidationError("Время выполнения должно быть не больше 120 секунд")


class NiceHabitAssociatedValidator:
    """В связанные привычки могут попадать только привычки с признаком приятной привычки"""

    def __init__(self, field):
        self.field = field

    def __call__(self, habit):
        if habit.get('associted_habit'):
            if not habit.get('nice_habit'):
                raise ValidationError("В связанные привычки могут попадать только привычки с признаком приятной привычки")


class NiceHabitRewardOrAssocitedValidator:
    """У приятной привычки не может быть вознаграждения или связанной привычки"""

    def __init__(self, field):
        self.field = field

    def __call__(self, habit):
        if habit.get('nice_habit'):
            if habit.get('reward') or habit.get('associted_habit'):
                raise ValidationError("У приятной привычки не может быть вознаграждения или связанной привычки")


class PeriodicityValidator:
    """Нельзя выполнять привычку реже, чем 1 раз в 7 дней"""

    def __init__(self, field):
        self.field = field

    def __call__(self, habit):
        periodicity = habit.get('periodicity')
        if 7 < periodicity or periodicity < 1:
            raise ValidationError("Нельзя выполнять привычку реже, чем 1 раз в 7 дней")