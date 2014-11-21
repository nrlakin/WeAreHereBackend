# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wah_test', '0002_auto_20141120_2109'),
    ]

    operations = [
        migrations.RenameField(
            model_name='checkin',
            old_name='user',
            new_name='name',
        ),
    ]
