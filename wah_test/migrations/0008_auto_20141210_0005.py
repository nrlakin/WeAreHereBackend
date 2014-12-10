# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('wah_test', '0007_auto_20141209_2337'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkin',
            name='user',
            field=models.ForeignKey(related_name='checkins', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
