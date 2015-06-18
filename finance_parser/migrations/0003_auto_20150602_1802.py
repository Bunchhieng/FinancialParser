# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('finance_parser', '0002_auto_20150602_1800'),
    ]

    operations = [
        migrations.AlterField(
            model_name='symbol',
            name='name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='symbol',
            name='symbol',
            field=models.CharField(max_length=100),
        ),
    ]
