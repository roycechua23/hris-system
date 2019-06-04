# Generated by Django 2.2 on 2019-06-04 10:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='hr',
            name='date_lastlogin',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='hr',
            name='is_loggedin',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]