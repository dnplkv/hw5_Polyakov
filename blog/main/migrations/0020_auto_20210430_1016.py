# Generated by Django 3.1.7 on 2021-04-30 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0019_auto_20210424_0925'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=80, verbose_name='Заголовок'),
        ),
    ]