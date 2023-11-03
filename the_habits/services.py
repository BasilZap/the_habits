import requests

from config.settings import TELEGRAM_BOT_TOKEN


def send_message(message, telegram_id):
    """
    Отправка сообщения пользователю
    :param message: текст сообщения -> str
    :param telegram_id: telegram id -> str
    :return: response -> json
    """
    url = f'https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage'
    data = {'chat_id': telegram_id, 'text': message, "parse_mode": "HTML"}
    response = requests.post(url, data=data)
    return response.json()

