# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('score_book', '0002_auto_20150811_0325'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instructor',
            name='ucinetid',
            field=models.TextField(unique=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='studentid',
            field=models.PositiveIntegerField(unique=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='ucinetid',
            field=models.TextField(unique=True),
        ),
    ]
