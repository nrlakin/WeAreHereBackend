# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('wah_test', '0005_auto_20141121_0125'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='occupant',
            options={},
        ),
        migrations.RemoveField(
            model_name='occupant',
            name='name',
        ),
        migrations.AddField(
            model_name='occupant',
            name='user',
            field=models.OneToOneField(default=1, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
