# Generated by Django 3.0 on 2020-05-13 14:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tukangkuapp', '0049_auto_20200513_2117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='daftar',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author', to=settings.AUTH_USER_MODEL),
        ),
    ]
