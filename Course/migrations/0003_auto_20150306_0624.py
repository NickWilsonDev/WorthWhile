# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Course', '0002_auto_20150306_0608'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='art',
            field=models.ImageField(null=True, upload_to=b'profile/%Y/%m/%d/', blank=True),
            preserve_default=True,
        ),
    ]
