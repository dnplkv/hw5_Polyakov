# Generated by Django 3.1.7 on 2021-04-17 16:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_auto_20210417_1517'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80, verbose_name='Name of category')),
            ],
        ),
        migrations.AlterField(
            model_name='books',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='books',
                                    to='main.author'),
        ),
        migrations.AlterField(
            model_name='books',
            name='title',
            field=models.CharField(max_length=50, verbose_name='Title'),
        ),
        migrations.AddField(
            model_name='books',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='books',
                                    to='main.category'),
        ),
    ]
