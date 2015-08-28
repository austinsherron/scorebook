# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('score_book', '0004_auto_20150812_0701'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quarter',
            name='end',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='quarter',
            name='start',
            field=models.DateField(),
        ),
    ]
