# Generated by Django 3.0 on 2020-05-12 14:51

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('tukangkuapp', '0036_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='buat',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
