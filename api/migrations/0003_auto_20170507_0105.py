# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20170506_1430'),
    ]

    operations = [
        migrations.AlterField(
            model_name='playlist',
            name='SessionId',
            field=models.CharField(default=b'0', max_length=250),
        ),
        migrations.AlterField(
            model_name='song',
            name='SongName',
            field=models.CharField(default=b'NULL', max_length=450),
        ),
    ]
