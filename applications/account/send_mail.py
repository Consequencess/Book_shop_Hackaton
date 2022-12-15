from datetime import time

from django.core.mail import send_mail


def send_confirmation_email(email, code):
    full_link = f'http://localhost:8000/account/activate/{code}'
    send_mail(
        'Активация  пользователя',
        full_link,
        'read87488@gmail.com',
        [email]

    )


def send_confirmation_code(email, code):

    send_mail(
        'Восстанавление пароля',
        code,
        'read87488@gmail.com',
        [email]
    )