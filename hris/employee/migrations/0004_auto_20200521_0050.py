# Generated by Django 2.0.2 on 2020-05-20 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0003_auto_20190605_1811'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='date_updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
