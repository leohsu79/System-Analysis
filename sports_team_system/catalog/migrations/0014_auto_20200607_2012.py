# Generated by Django 3.0.5 on 2020-06-07 12:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0013_auto_20200607_2012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticing',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 7, 20, 12, 51, 183817)),
        ),
        migrations.AlterField(
            model_name='training',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 7, 20, 12, 51, 180817)),
        ),
        migrations.AlterField(
            model_name='training',
            name='participant',
            field=models.ManyToManyField(blank=True, to='catalog.Playing_Sport'),
        ),
        migrations.AlterField(
            model_name='voting',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 7, 20, 12, 51, 182816)),
        ),
        migrations.AlterField(
            model_name='voting',
            name='participant',
            field=models.ManyToManyField(blank=True, to='catalog.Playing_Sport'),
        ),
    ]