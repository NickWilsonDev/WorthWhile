# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Course', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='art',
            field=models.FileField(null=True, upload_to=b'documents/', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='course',
            name='duration',
            field=models.CharField(max_length=10, verbose_name=b'Course Duration'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='course',
            name='instructor',
            field=models.CharField(default=b'Django Guru', max_length=60, verbose_name=b'Instructor'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='course',
            name='title',
            field=models.CharField(default=b'Name it something good.', max_length=60, verbose_name=b'Course Title'),
            preserve_default=True,
        ),
    ]
