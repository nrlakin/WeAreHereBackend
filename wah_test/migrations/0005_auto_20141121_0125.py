# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wah_test', '0004_auto_20141120_2309'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='checkin',
            name='room',
        ),
        migrations.RemoveField(
            model_name='occupant',
            name='room',
        ),
        migrations.AddField(
            model_name='checkin',
            name='room_id',
            field=models.SmallIntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='occupant',
            name='room_id',
            field=models.SmallIntegerField(default=0),
            preserve_default=True,
        ),
    ]
