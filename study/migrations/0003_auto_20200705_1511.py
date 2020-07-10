# Generated by Django 3.0.6 on 2020-07-05 06:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('study', '0002_memberinfo'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='popular',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='blog',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
