# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('customer_name', models.CharField(max_length=20)),
                ('contact_number', models.CharField(max_length=10)),
                ('address', models.CharField(max_length=10)),
                ('type', models.CharField(max_length=20)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
