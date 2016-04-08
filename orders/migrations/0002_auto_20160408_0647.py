# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='date',
            field=models.CharField(default='asd', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='time',
            field=models.CharField(default='asd', max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='order',
            name='address',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='order',
            name='customer_name',
            field=models.CharField(max_length=200),
        ),
    ]
