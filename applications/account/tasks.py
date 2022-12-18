from config.celery import app
from django.core.mail import send_mail

@app.task
def send_confirmation_email_celery(email, code):
    full_link = f'http://localhost:8000/account/activate/{code}'
    send_mail(
        'Активация  пользователя',
        full_link,
        'read87488@gmail.com',
        [email]

    )

@app.task
def spam_message():
    full_link = f'http://localhost:8000/books/'
    send_mail(
        'Привет новые товары пришли можешь глануть',
        full_link,
        'read87488@gmail.com',
        ['read87488@gmail.com']

    )