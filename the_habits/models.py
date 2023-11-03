from django.db import models

from config import settings
from users.models import NULLABLE


class Habit(models.Model):
    action = models.CharField(max_length=250, verbose_name='Действие')
    habit_datetime = models.DateTimeField(verbose_name='Дата выполнения')
    place = models.CharField(max_length=200, verbose_name='Место')
    pleasant_sign = models.BooleanField(default=False, verbose_name='Признак приятной привычки', **NULLABLE)
    frequency = models.IntegerField(default=1, verbose_name='Интервал (дней)', **NULLABLE)
    related_habit = models.ForeignKey('Habit', on_delete=models.DO_NOTHING, verbose_name='Связанная привычка',
                                      **NULLABLE)
    reward = models.CharField(max_length=200, verbose_name='Вознаграждение', **NULLABLE)
    time_to_complete = models.IntegerField(verbose_name='Время на выполнение')
    public_sign = models.BooleanField(default=False, verbose_name='Публичный', **NULLABLE)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Владелец', **NULLABLE)
    launched = models.BooleanField(default=False, verbose_name='Задание выполняется', **NULLABLE)

    def __str__(self):
        return f'{self.action} - {self.habit_datetime} в {self.place}'

    class Meta:
        verbose_name = 'Привычка'
        verbose_name_plural = 'Привычки'
