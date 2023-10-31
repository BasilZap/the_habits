from django.db import models

from config import settings
from users.models import NULLABLE

FREQUENCY_STATES = (
    ('1:1', 'Раз в день'),
    ('1:2', 'Раз в 2 дня'),
    ('1:3', 'Раз в 3 дня'),
    ('1:4', 'Раз в 4 дня'),
    ('1:5', 'Раз в 5 дня'),
    ('1:6', 'Раз в 6 дня'),
    ('1:7', 'Раз в 7 дня')
)


class Habit(models.Model):
    action = models.CharField(max_length=250, verbose_name='Действие')
    habit_datetime = models.DateTimeField(verbose_name='Дата выполнения')
    place = models.CharField(max_length=200, verbose_name='Место')
    pleasant_sign = models.BooleanField(default=False, verbose_name='Признак полезной привычки', **NULLABLE)
    frequency = models.CharField(max_length=3, default='1:1', choices=FREQUENCY_STATES, verbose_name='Периодичность',
                                 **NULLABLE)
    related_habit = models.ForeignKey('Habit', on_delete=models.DO_NOTHING, verbose_name='Связанная привычка',
                                      **NULLABLE)
    reward = models.CharField(max_length=200, verbose_name='Вознаграждение', **NULLABLE)
    time_to_complete = models.IntegerField(verbose_name='Время на выполнение')
    public_sign = models.BooleanField(default=False, verbose_name='Публичный', **NULLABLE)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Владелеец', **NULLABLE)

    def __str__(self):
        return f'{self.action} - {self.habit_datetime} в {self.place}'

    class Meta:
        verbose_name = 'Привычка'
        verbose_name_plural = 'Привычки'
