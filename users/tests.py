from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient


class HabitTestCase(APITestCase):
    """
    Класс тестирования эндпоинтов пользователя
    """

    def setUp(self) -> None:
        self.client = APIClient()

    def test_create_user(self):
        """
        Тестирование эндпоинта создания пользователя
        :return: None
        """
        data = {
            "email": "test@test.ru",
            "password": "123456",
        }

        response = self.client.post(
            reverse('users:user_create'),
            data=data
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )
        print(response.json())

        self.assertEqual(
            response.json(),
            {
                'id': 6, 'first_name': '', 'email': 'test@test.ru'
            }
        )
