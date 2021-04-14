from datetime import timedelta

from celery import shared_task
from django.utils.timezone import now
import requests

from .models import Log, Subscriber
from .notify_service import email_send, email_send_string


@shared_task
def notify_async(email_to, author_name):
    email_send(email_to, author_name)


@shared_task
def delete_all_logs_3days():
    Log.objects.filter(created=now() - timedelta(days=3)).delete()


@shared_task
def email_send_to_subs():
    adress = requests.get("https://tproger.ru/wp-content/plugins/citation-widget/get-quote.php")
    string = str(adress.content)
    emails = Subscriber.objects.values_list('email_to', flat=True)

    for email in set(emails):
        email_send_string(email, string)
