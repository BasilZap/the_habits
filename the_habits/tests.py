from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from the_habits.models import Habit
from users.models import User


class HabitTestCase(APITestCase):
    """
    Класс тестирования эндпоинтов привычек
    """

    def setUp(self) -> None:
        self.client = APIClient()
        self.user = User.objects.create(email='test@test.com', password='test', is_staff=True, is_superuser=True)
        self.client.force_authenticate(user=self.user)
        self.habit = Habit.objects.create(
            action='test action',
            habit_datetime='2023-11-02T23:53:57.486000Z',
            place='test place',
            frequency=2,
            reward='test reward',
            time_to_complete=120,
            public_sign=True,
            launched=False,
            related_habit=None
        )

    def test_create_habit(self):
        """
        Метод тестирования эндпоинта создания привычки
        :return:
        """
        data = {
            "action": "test action",
            "habit_datetime": "2023-11-02 23:53:57,486",
            "place": "test place",
            "frequency": 2,
            "reward": "test reward",
            "time_to_complete": 120

        }
        response = self.client.post(
            reverse('the_habits:create'),
            data=data
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

        print(response.json())

        self.assertEqual(
            Habit.objects.all().count(),
            2
        )
        self.assertEqual(
            response.json(),
            {
                'id': 2,
                'action': 'test action',
                'habit_datetime': '2023-11-02T23:53:57.486000Z',
                'place': 'test place',
                'pleasant_sign': False,
                'frequency': 2,
                'reward': 'test reward',
                'time_to_complete': 120,
                'public_sign': False,
                'launched': False,
                'related_habit': None,
                'owner': 1
            }
        )

    def test_update_habit(self):
        """
        Метод тестирования эндпоинта изменения привычки
        :return:
        """

        new_data = {
            "action": "test action2",
            "habit_datetime": "2023-11-02 23:53:57,486",
            "place": "test place2",
            "frequency": 4,
            "reward": "test reward",
            "time_to_complete": 120

        }
        print(self.habit.pk)
        response = self.client.put(
            reverse('the_habits:update', args=str(self.habit.pk)),
            data=new_data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json(),
            {
                'id': self.habit.pk,
                'action': 'test action2',
                'habit_datetime': '2023-11-02T23:53:57.486000Z',
                'place': 'test place2',
                'pleasant_sign': False,
                'frequency': 4,
                'reward': 'test reward',
                'time_to_complete': 120,
                'public_sign': False,
                'launched': False,
                'related_habit': None,
                'owner': None
            }
        )
        print(self.habit.pk)

    def test_list_habit(self):
        """
        Метод тестирования эндпоинта изменения привычки
        :return:
        """

        response = self.client.get(
            reverse('the_habits:list'),
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json(),
            {
                'count': 0,
                'next': None,
                'previous': None,
                'results': []
            }
        )

    def test_public_habit(self):
        """
        Метод тестирования эндпоинта изменения привычки
        :return:
        """

        response = self.client.get(
            reverse('the_habits:public'),
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json(),
            {
                'count': 1,
                'next': None,
                'previous': None,
                'results': [
                    {
                        'action': 'test action',
                        'frequency': 2,
                        'habit_datetime': '2023-11-02T23:53:57.486000Z',
                        'id': 5,
                        'launched': False,
                        'owner': None,
                        'place': 'test place',
                        'pleasant_sign': False,
                        'public_sign': True,
                        'related_habit': None,
                        'reward': 'test reward',
                        'time_to_complete': 120
                    }
                ]
            }
        )

    def test_delete_habit(self):
        """
        Метод тестирования эндпоинта удаления привычки
        :return:
        """
        response = self.client.delete(
            reverse('the_habits:delete', args=str(3)),
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )

    def tearDown(self):
        Habit.objects.all().delete()
        self.habit.delete()
