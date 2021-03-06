# Generated by Django 3.0.5 on 2020-06-07 11:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0009_auto_20200606_0756'),
    ]

    operations = [
        migrations.AddField(
            model_name='voting',
            name='option_one',
            field=models.TextField(default='test'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='voting',
            name='option_one_cnt',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='voting',
            name='option_three',
            field=models.TextField(default='test'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='voting',
            name='option_three_cnt',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='voting',
            name='option_two',
            field=models.TextField(default='test'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='voting',
            name='option_two_cnt',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='noticing',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 7, 19, 38, 3, 249894)),
        ),
        migrations.AlterField(
            model_name='training',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 7, 19, 38, 3, 246904)),
        ),
        migrations.AlterField(
            model_name='voting',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 7, 19, 38, 3, 248897)),
        ),
    ]
