# Generated by Django 3.0.6 on 2020-07-05 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('study', '0003_auto_20200705_1511'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='edit_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='date edited'),
        ),
    ]
