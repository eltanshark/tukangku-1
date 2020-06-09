# Generated by Django 3.0 on 2020-06-06 15:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sellerapp', '0013_auto_20200606_2218'),
    ]

    operations = [
        migrations.AddField(
            model_name='proinfo',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sellerAuthor', to=settings.AUTH_USER_MODEL),
        ),
    ]
