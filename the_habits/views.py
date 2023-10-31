from django.shortcuts import render
from rest_framework import generics

from the_habits.models import Habit
from the_habits.serializers import HabitSerializer


class HabitCreateAPIView(generics.CreateAPIView):
    """ Представление создания новой привычки """
    serializer_class = HabitSerializer

    def perform_create(self, serializer):
        """
        Метод присвоения владельца каждой привычке
        :param serializer:
        :return:
        """
        new_habit = serializer.save()
        new_habit.owner = self.request.user
        new_habit.save()


class HabitUpdateAPIView(generics.UpdateAPIView):
    """ Представление изменения привычки """
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()


class HabitListAPIView(generics.ListAPIView):
    """ Представление вывода всех привычек пользователя """
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()

    def get_queryset(self):
        """
        Переопределение метода get_queryset,
        выводим только привычки, созданные пользователем
        :return: набор объектов класса Habit
        """
        queryset = super().get_queryset()
        queryset = queryset.filter(owner=self.request.user)
        return queryset


class HabitPublicListAPIView(generics.ListAPIView):
    """ Представление вывода всех публичных привычек """
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()

    def get_queryset(self):
        """
        Переопределение метода get_queryset,
        выводим только привычки с признаком 'Публичная'
        :return: набор объектов класса Habit
        """
        queryset = super().get_queryset()
        queryset = queryset.filter(public_sign=True)
        return queryset


class HabitDestroyAPIView(generics.DestroyAPIView):
    """ Представление удаления привычки пользователя """
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
