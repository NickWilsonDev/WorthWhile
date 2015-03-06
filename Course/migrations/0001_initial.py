# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(help_text=b'Name it something good.', max_length=30, verbose_name=b'Course Title')),
                ('description', models.CharField(max_length=200, verbose_name=b'Description')),
                ('instructor', models.CharField(max_length=30, verbose_name=b'Instructor')),
                ('duration', models.CharField(max_length=10, verbose_name=b'Duration')),
                ('art', models.FileField(null=True, upload_to=b'', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
