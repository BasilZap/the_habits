import datetime

from celery import shared_task
from django.utils import timezone

from the_habits.models import Habit
from the_habits.services import send_message


@shared_task
def send_habit_task():
    """
    Функция формирования сообщений пользователю
    :return: None
    """
    current_date = timezone.now()  # Получаем текущую дату и время
    print(current_date)
    # Получаем все привычки, которые должны выполниться и не имеют признака приятной привычки
    tasks = Habit.objects.filter(habit_datetime__lte=current_date, pleasant_sign=False)

    # Если список не пуст - перебираем объекты класса "Привычка"
    if tasks is not None:
        for task in tasks:
            # Получаем необходимые для рассылки пользователю данные
            habit_datetime = task.habit_datetime
            time_to_complete = task.time_to_complete
            frequency = task.frequency
            # Получаем время на выполнение задания
            time_delta = habit_datetime + datetime.timedelta(seconds=time_to_complete)
            # Получаем время, когда задание должно быть запущено в следующий раз
            next_date = habit_datetime + datetime.timedelta(days=frequency)
            place = task.place
            action = task.action
            launched = task.launched

            # Если задание запущено и время на выполнение вышло
            if launched and time_delta <= current_date:

                # Формируем сообщение о том, как пользователь может себя вознаградить
                if task.related_habit:
                    message = f'Ваше вознаграждение {task.related_habit.action}, место: {task.related_habit.place}'
                elif task.reward:
                    message = f'Ваше вознаграждение {task.reward}'
                else:
                    message = f'Вы выполнили приятную привычку'

                # Проверяем указал ли пользователь свой ID telegram
                if task.owner.telegram_id:
                    send_message(message, task.owner.telegram_id)
                print(message)

                # Завершаем выполнение задания, в поле даты записываем дату следующего выполнения
                task.launched = False
                task.habit_datetime = next_date
                task.save()

            # Если задание не запущено - формируем сообщение о начале задания
            elif not launched:
                message = f'Настало время {habit_datetime}! Выполните {action}, место: {place}'

                # Проверяем указал ли пользователь свой ID telegram
                if task.owner.telegram_id:
                    send_message(message, task.owner.telegram_id)
                print(message)

                # Устанавливаем флаг - задание выполняется
                task.launched = True
                task.save()

            # В противном случае ничего не делаем, пропускаем цикл
            else:
                continue
