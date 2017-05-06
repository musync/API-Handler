# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DjSessions',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('SessionName', models.CharField(default=b'NULL', max_length=250)),
                ('NetworkName', models.CharField(default=b'NULL', max_length=250)),
                ('SessionId', models.CharField(default=b'NULL', max_length=250)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Playlist',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('SongName', models.CharField(default=b'NULL', max_length=250)),
                ('SongUrl', models.CharField(default=b'NULL', max_length=250)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('YoutubeToken', models.CharField(default=b'NULL', max_length=250)),
                ('Name', models.CharField(default=b'NULL', max_length=250)),
                ('Email', models.CharField(default=b'NULL', max_length=250)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='playlist',
            name='Email',
            field=models.ForeignKey(to='api.user'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='playlist',
            name='SessionId',
            field=models.ForeignKey(to='api.DjSessions'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='playlist',
            name='SongName',
            field=models.ForeignKey(to='api.Song'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='djsessions',
            name='Email',
            field=models.ForeignKey(to='api.user'),
            preserve_default=True,
        ),
    ]
