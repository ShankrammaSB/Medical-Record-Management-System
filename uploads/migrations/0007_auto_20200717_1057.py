# Generated by Django 3.0.7 on 2020-07-17 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uploads', '0006_queries'),
    ]

    operations = [
        migrations.AlterField(
            model_name='queries',
            name='mobile',
            field=models.IntegerField(),
        ),
    ]
