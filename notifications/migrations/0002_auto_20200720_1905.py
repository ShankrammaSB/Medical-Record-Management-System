# Generated by Django 3.0.8 on 2020-07-20 13:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='select_time',
            field=models.TimeField(default=datetime.datetime(2020, 7, 20, 19, 5, 50, 472569)),
        ),
    ]
