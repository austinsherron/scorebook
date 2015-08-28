# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('score_book', '0003_auto_20150812_0428'),
    ]

    operations = [
        migrations.AddField(
            model_name='quarter',
            name='end',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 12, 7, 1, 7, 308752), blank=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='quarter',
            name='start',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 12, 7, 1, 19, 842384), blank=True),
            preserve_default=False,
        ),
    ]
