# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='playlist',
            name='SessionId',
            field=models.CharField(default=b'NULL', max_length=250),
        ),
    ]
