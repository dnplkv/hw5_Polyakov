# Generated by Django 3.1.7 on 2021-04-13 17:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_log'),
    ]

    operations = [
        migrations.RenameField(
            model_name='log',
            old_name='ip_address',
            new_name='user_ip',
        ),
    ]