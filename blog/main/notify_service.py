from django.core.mail import send_mail


def notify(email_to):
    email_send(email_to)
    telegram_notify(email_to)


def email_send(email_to, author_name):
    send_mail(
        'Blog',
        f'You have subscribed on Author: {author_name}',
        'uchetkanyash@gmail.com',
        [email_to],
        fail_silently=False,
    )


def email_send_string(email_to, string):
    send_mail(
        'Blog',
        f'{string}',
        'uchetkanyash@gmail.com',
        [email_to],
        fail_silently=False,
    )


def telegram_notify(email_to):
    pass
