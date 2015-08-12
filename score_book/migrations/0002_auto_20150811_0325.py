# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('score_book', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignment',
            name='discrete_score_system',
            field=models.ForeignKey(blank=True, to='score_book.DiscreteScoreSystem'),
        ),
        migrations.AlterField(
            model_name='course',
            name='instructors',
            field=models.ManyToManyField(blank=True, to='score_book.Instructor'),
        ),
        migrations.AlterField(
            model_name='course',
            name='location',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='students',
            field=models.ManyToManyField(blank=True, to='score_book.Student'),
        ),
        migrations.AlterField(
            model_name='discretescoretype',
            name='score_system',
            field=models.ManyToManyField(blank=True, to='score_book.DiscreteScoreSystem'),
        ),
        migrations.AlterField(
            model_name='instructor',
            name='courses',
            field=models.ManyToManyField(blank=True, to='score_book.Course'),
        ),
        migrations.AlterField(
            model_name='instructor',
            name='sections',
            field=models.ManyToManyField(blank=True, to='score_book.Section'),
        ),
        migrations.AlterField(
            model_name='section',
            name='instructors',
            field=models.ManyToManyField(blank=True, to='score_book.Instructor'),
        ),
        migrations.AlterField(
            model_name='section',
            name='students',
            field=models.ManyToManyField(blank=True, to='score_book.Student'),
        ),
        migrations.AlterField(
            model_name='student',
            name='courses',
            field=models.ManyToManyField(blank=True, to='score_book.Course'),
        ),
        migrations.AlterField(
            model_name='student',
            name='sections',
            field=models.ManyToManyField(blank=True, to='score_book.Section'),
        ),
    ]
