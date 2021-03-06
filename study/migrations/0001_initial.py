# Generated by Django 3.0.6 on 2020-07-04 05:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('create_date', models.DateTimeField(verbose_name='date created')),
                ('edit_date', models.DateTimeField(blank=True, verbose_name='date edited')),
                ('deleted', models.BooleanField(default=False)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='study.Category')),
            ],
        ),
    ]
