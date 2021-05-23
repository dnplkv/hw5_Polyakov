from datetime import timedelta
from decimal import Decimal

from celery import shared_task
from django.utils.timezone import now
import requests

from .models import Log, Rate, Subscriber
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
    string = adress.content.decode('utf-8')
    emails = Subscriber.objects.values_list('email_to', flat=True)

    for email in set(emails):
        email_send_string(email, string)


@shared_task
def parse_privatbank():
    url = 'https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5'
    response = requests.get(url)

    response.raise_for_status()

    data = response.json()
    source = 1
    currency_map = {
        'USD': 1,
        'EUR': 2,
    }

    TWOPLACES = Decimal(10) ** -2

    for row in data:
        if row['ccy'] in currency_map:
            buy = Decimal(row['buy']).quantize(TWOPLACES)
            sale = Decimal(row['sale']).quantize(TWOPLACES)
            currency = currency_map[row['ccy']]

            last_rate = Rate.objects.filter(source=source, currency=currency).last()
            if last_rate is None or buy != last_rate.buy or sale != last_rate.sale:
                Rate.objects.create(
                    currency=currency,
                    source=source,
                    buy=buy,
                    sale=sale,
                )
