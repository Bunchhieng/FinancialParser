# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('finance_parser', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='symbol',
            name='IPOYear',
            field=models.CharField(max_length=200),
        ),
    ]
