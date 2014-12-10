# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('wah_test', '0006_auto_20141209_0221'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='checkin',
            name='name',
        ),
        migrations.AddField(
            model_name='checkin',
            name='user',
            field=models.ForeignKey(related_name='users', default=1, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='checkin',
            name='when',
            field=models.DateTimeField(auto_now_add=True),
            preserve_default=True,
        ),
    ]
