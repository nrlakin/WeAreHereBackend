# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wah_test', '0003_auto_20141120_2211'),
    ]

    operations = [
        migrations.CreateModel(
            name='Occupant',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'', max_length=100, blank=True)),
                ('room', models.CharField(default=b'', max_length=100, blank=True)),
                ('last_update', models.DateTimeField(auto_now_add=True, verbose_name=b'date created')),
            ],
            options={
                'ordering': ('name',),
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='checkin',
            name='when',
            field=models.DateTimeField(auto_now_add=True, verbose_name=b'checked in'),
            preserve_default=True,
        ),
    ]
