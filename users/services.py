from django.core.mail import send_mail
import random, string
from config import settings


def random_key():
    """
    Генерация ключа
    """
    characters = string.ascii_letters + string.digits
    return ''.join(random.sample(characters, 30))


def _send_mail(subject: str, text: str, mail: list) -> None:
    """
    Отправка письма
    """
    send_mail(
        subject,
        text,
        settings.EMAIL_HOST_USER,
        [mail]
    )


def create_password():
    """
    Генерация пароля
    """
    characters = string.ascii_letters + string.digits
    return ''.join(random.sample(characters, 12))