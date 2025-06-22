from django.db import models
from users.models import User


class Habit(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="habits",
        blank=True,
        null=True,
        help_text="Пользователь, создатель привычки",
    )
    place = models.CharField(
        blank=True,
        null=True,
        max_length=50,
        verbose_name="Место",
        help_text="Место, в котором необходимо выполнять привычку",
    )
    time = models.TimeField(
        blank=True,
        null=True,
        auto_now=False,
        auto_now_add=False,
        verbose_name="Время",
        help_text="Время, когда надо выполнить привычку",
    )
    action = models.CharField(
        max_length=50,
        verbose_name="Действие",
        help_text="Действие, которое представляет собой привычка",
    )
    nice_habit = models.BooleanField(
        default=True,
        verbose_name="Признак приятной привычки",
        help_text="Привычка, которую можно привязать к выполнению полезной привычки",
    )
    associted_habit = models.ForeignKey(
        "self",
        verbose_name="Связанная привычка",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        help_text="Привычка, которая связана с полезной привычкой (не с приятной)",
    )
    periodicity = models.IntegerField(
        default=1,
        verbose_name="Периодичность",
        help_text="Периодичность выполнения привычки для напоминания в днях",
    )
    reward = models.CharField(
        blank=True,
        null=True,
        verbose_name="Вознаграждение",
        help_text="Чем пользователь должен себя вознаградить после выполнения",
    )
    time_to_complete = models.TimeField(
        blank=True,
        null=True,
        auto_now=False,
        auto_now_add=False,
        verbose_name="Время на выполнение",
        help_text="Время, которое предположительно потратит пользователь на выполнение привычки",
    )
    is_published = models.BooleanField(
        blank=True,
        null=True,
        default=True,
        verbose_name="Признак публичности",
        help_text="Признак публикации в общий доступ",
    )

    class Meta:
        verbose_name = "Привычка"
        verbose_name_plural = "Привычки"
        ordering = ("id",)

    def __str__(self):
        return f"Я буду {self.action} в {self.time} в {self.place}"
