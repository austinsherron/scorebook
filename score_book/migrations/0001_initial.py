# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.UUIDField(editable=False, primary_key=True, default=uuid.uuid4, serialize=False)),
                ('title', models.TextField()),
                ('total_value', models.DecimalField(decimal_places=5, max_digits=10)),
                ('is_discrete', models.BooleanField()),
                ('upper_bound', models.DecimalField(default=0.0, max_digits=10, decimal_places=5)),
                ('lower_bound', models.DecimalField(default=100.0, max_digits=10, decimal_places=5)),
            ],
            options={
                'verbose_name_plural': 'assignments',
                'verbose_name': 'assignment',
            },
        ),
        migrations.CreateModel(
            name='AssignmentType',
            fields=[
                ('id', models.UUIDField(editable=False, primary_key=True, default=uuid.uuid4, serialize=False)),
                ('name', models.TextField()),
                ('weight', models.DecimalField(decimal_places=5, max_digits=10)),
            ],
            options={
                'verbose_name_plural': 'assignments types',
                'verbose_name': 'assignment type',
            },
        ),
        migrations.CreateModel(
            name='ContinuousScore',
            fields=[
                ('id', models.UUIDField(editable=False, primary_key=True, default=uuid.uuid4, serialize=False)),
                ('value', models.DecimalField(decimal_places=5, max_digits=10)),
                ('assignment', models.ForeignKey(to='score_book.Assignment')),
            ],
            options={
                'verbose_name_plural': 'scores',
                'verbose_name': 'score',
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.UUIDField(editable=False, primary_key=True, default=uuid.uuid4, serialize=False)),
                ('year', models.IntegerField()),
                ('full_name', models.TextField()),
                ('abbr_name', models.TextField()),
                ('location', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'courses',
                'verbose_name': 'course',
            },
        ),
        migrations.CreateModel(
            name='DiscreteScore',
            fields=[
                ('id', models.UUIDField(editable=False, primary_key=True, default=uuid.uuid4, serialize=False)),
                ('assignment', models.ForeignKey(to='score_book.Assignment')),
            ],
            options={
                'verbose_name_plural': 'scores',
                'verbose_name': 'score',
            },
        ),
        migrations.CreateModel(
            name='DiscreteScoreSystem',
            fields=[
                ('id', models.UUIDField(editable=False, primary_key=True, default=uuid.uuid4, serialize=False)),
                ('course', models.ForeignKey(to='score_book.Course')),
            ],
            options={
                'verbose_name_plural': 'score systems',
                'verbose_name': 'score system',
            },
        ),
        migrations.CreateModel(
            name='DiscreteScoreType',
            fields=[
                ('id', models.UUIDField(editable=False, primary_key=True, default=uuid.uuid4, serialize=False)),
                ('numeric_value', models.DecimalField(decimal_places=5, max_digits=10)),
                ('text_value', models.TextField()),
                ('image_value', models.ImageField(upload_to='')),
                ('real_value', models.DecimalField(decimal_places=5, max_digits=10)),
                ('course', models.ForeignKey(to='score_book.Course')),
                ('score_system', models.ManyToManyField(to='score_book.DiscreteScoreSystem')),
            ],
            options={
                'verbose_name_plural': 'score types',
                'verbose_name': 'score type',
            },
        ),
        migrations.CreateModel(
            name='Instructor',
            fields=[
                ('id', models.UUIDField(editable=False, primary_key=True, default=uuid.uuid4, serialize=False)),
                ('ucinetid', models.TextField()),
                ('preferred_name', models.TextField(default='')),
                ('courses', models.ManyToManyField(to='score_book.Course')),
            ],
            options={
                'ordering': ['ucinetid'],
                'verbose_name': 'instructor',
                'verbose_name_plural': 'instructors',
            },
        ),
        migrations.CreateModel(
            name='Quarter',
            fields=[
                ('id', models.UUIDField(editable=False, primary_key=True, default=uuid.uuid4, serialize=False)),
                ('name', models.TextField()),
                ('number', models.IntegerField()),
            ],
            options={
                'ordering': ['number'],
                'verbose_name': 'quarter',
                'verbose_name_plural': 'quarters',
            },
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.UUIDField(editable=False, primary_key=True, default=uuid.uuid4, serialize=False)),
                ('name', models.TextField()),
                ('number', models.IntegerField()),
                ('course', models.ForeignKey(to='score_book.Course')),
                ('instructors', models.ManyToManyField(to='score_book.Instructor')),
            ],
            options={
                'verbose_name_plural': 'sections',
                'verbose_name': 'section',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.UUIDField(editable=False, primary_key=True, default=uuid.uuid4, serialize=False)),
                ('ucinetid', models.TextField()),
                ('preferred_name', models.TextField(default='')),
                ('studentid', models.PositiveIntegerField()),
                ('courses', models.ManyToManyField(to='score_book.Course')),
                ('sections', models.ManyToManyField(to='score_book.Section')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['ucinetid'],
                'verbose_name': 'student',
                'verbose_name_plural': 'students',
            },
        ),
        migrations.AddField(
            model_name='section',
            name='students',
            field=models.ManyToManyField(to='score_book.Student'),
        ),
        migrations.AddField(
            model_name='instructor',
            name='sections',
            field=models.ManyToManyField(to='score_book.Section'),
        ),
        migrations.AddField(
            model_name='instructor',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='discretescoresystem',
            name='possible_values',
            field=models.ManyToManyField(to='score_book.DiscreteScoreType'),
        ),
        migrations.AddField(
            model_name='discretescore',
            name='student',
            field=models.ForeignKey(to='score_book.Student'),
        ),
        migrations.AddField(
            model_name='discretescore',
            name='value',
            field=models.ForeignKey(to='score_book.DiscreteScoreType'),
        ),
        migrations.AddField(
            model_name='course',
            name='instructors',
            field=models.ManyToManyField(to='score_book.Instructor'),
        ),
        migrations.AddField(
            model_name='course',
            name='quarter',
            field=models.ForeignKey(to='score_book.Quarter'),
        ),
        migrations.AddField(
            model_name='course',
            name='students',
            field=models.ManyToManyField(to='score_book.Student'),
        ),
        migrations.AddField(
            model_name='continuousscore',
            name='student',
            field=models.ForeignKey(to='score_book.Student'),
        ),
        migrations.AddField(
            model_name='assignmenttype',
            name='course',
            field=models.ForeignKey(to='score_book.Course'),
        ),
        migrations.AddField(
            model_name='assignment',
            name='assignment_type',
            field=models.ForeignKey(to='score_book.AssignmentType'),
        ),
        migrations.AddField(
            model_name='assignment',
            name='course',
            field=models.ForeignKey(to='score_book.Course'),
        ),
        migrations.AddField(
            model_name='assignment',
            name='discrete_score_system',
            field=models.ForeignKey(to='score_book.DiscreteScoreSystem'),
        ),
    ]
