# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import uuid


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.UUIDField(serialize=False, primary_key=True, default=uuid.uuid4, editable=False)),
                ('title', models.TextField()),
                ('total_value', models.DecimalField(max_digits=10, decimal_places=5)),
                ('is_discrete', models.BooleanField()),
                ('upper_bound', models.DecimalField(decimal_places=5, max_digits=10, default=0.0)),
                ('lower_bound', models.DecimalField(decimal_places=5, max_digits=10, default=100.0)),
            ],
        ),
        migrations.CreateModel(
            name='AssignmentType',
            fields=[
                ('id', models.UUIDField(serialize=False, primary_key=True, default=uuid.uuid4, editable=False)),
                ('name', models.TextField()),
                ('weight', models.DecimalField(max_digits=10, decimal_places=5)),
            ],
        ),
        migrations.CreateModel(
            name='ContinuousScore',
            fields=[
                ('id', models.UUIDField(serialize=False, primary_key=True, default=uuid.uuid4, editable=False)),
                ('value', models.DecimalField(max_digits=10, decimal_places=5)),
                ('assignment', models.ForeignKey(to='score_book.Assignment')),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.UUIDField(serialize=False, primary_key=True, default=uuid.uuid4, editable=False)),
                ('year', models.IntegerField()),
                ('full_name', models.TextField()),
                ('abbr_name', models.TextField()),
                ('location', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='DiscreteScore',
            fields=[
                ('id', models.UUIDField(serialize=False, primary_key=True, default=uuid.uuid4, editable=False)),
                ('assignment', models.ForeignKey(to='score_book.Assignment')),
            ],
        ),
        migrations.CreateModel(
            name='DiscreteScoreSystem',
            fields=[
                ('id', models.UUIDField(serialize=False, primary_key=True, default=uuid.uuid4, editable=False)),
                ('course', models.ForeignKey(to='score_book.Course')),
            ],
        ),
        migrations.CreateModel(
            name='DiscreteScoreType',
            fields=[
                ('id', models.UUIDField(serialize=False, primary_key=True, default=uuid.uuid4, editable=False)),
                ('numeric_value', models.DecimalField(max_digits=10, decimal_places=5)),
                ('text_value', models.TextField()),
                ('image_value', models.ImageField(upload_to='')),
                ('real_value', models.DecimalField(max_digits=10, decimal_places=5)),
                ('course', models.ForeignKey(to='score_book.Course')),
                ('score_system', models.ManyToManyField(to='score_book.DiscreteScoreSystem')),
            ],
        ),
        migrations.CreateModel(
            name='Instructor',
            fields=[
                ('id', models.UUIDField(serialize=False, primary_key=True, default=uuid.uuid4, editable=False)),
                ('ucinetid', models.TextField()),
                ('email', models.EmailField(max_length=254)),
                ('first_name', models.TextField()),
                ('last_name', models.TextField()),
                ('courses', models.ManyToManyField(to='score_book.Course')),
            ],
        ),
        migrations.CreateModel(
            name='Quarter',
            fields=[
                ('id', models.UUIDField(serialize=False, primary_key=True, default=uuid.uuid4, editable=False)),
                ('name', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.UUIDField(serialize=False, primary_key=True, default=uuid.uuid4, editable=False)),
                ('name', models.TextField()),
                ('number', models.IntegerField()),
                ('course', models.ForeignKey(to='score_book.Course')),
                ('instructors', models.ManyToManyField(to='score_book.Instructor')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.UUIDField(serialize=False, primary_key=True, default=uuid.uuid4, editable=False)),
                ('ucinetid', models.TextField()),
                ('email', models.EmailField(max_length=254)),
                ('first_name', models.TextField()),
                ('last_name', models.TextField()),
                ('studentid', models.PositiveIntegerField()),
                ('courses', models.ManyToManyField(to='score_book.Course')),
                ('sections', models.ManyToManyField(to='score_book.Section')),
            ],
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
