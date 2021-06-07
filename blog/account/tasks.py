from account.models import User
from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail


@shared_task
def send_email_with_activation_link(user_id):
    user = User.objects.get(id=user_id)
    link = settings.DOMAIN + '/activate/' + str(user.confirmation_token)
    body = f'activation link: {link}'
    send_mail(
        'Activate your email',
        body,
        settings.DEFAULT_FROM_EMAIL,
        [user.email],
        fail_silently=False
    )
