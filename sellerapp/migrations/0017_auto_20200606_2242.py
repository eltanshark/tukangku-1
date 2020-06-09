# Generated by Django 3.0 on 2020-06-06 15:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sellerapp', '0016_auto_20200606_2233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proinfo',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sellerProfile', to=settings.AUTH_USER_MODEL),
        ),
    ]
