# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wah_test', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CheckIn',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('when', models.DateTimeField(auto_now_add=True, verbose_name=b'date created')),
                ('user', models.CharField(default=b'', max_length=100, blank=True)),
                ('room', models.CharField(default=b'', max_length=100, blank=True)),
            ],
            options={
                'ordering': ('when',),
            },
            bases=(models.Model,),
        ),
        migrations.DeleteModel(
            name='Greeting',
        ),
    ]
