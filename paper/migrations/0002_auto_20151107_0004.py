# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('paper', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='comments',
        ),
        migrations.RemoveField(
            model_name='question',
            name='unit_number',
        ),
        migrations.AddField(
            model_name='question',
            name='difficult_level',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='question',
            name='marks',
            field=models.IntegerField(default=datetime.date(2015, 11, 7)),
            preserve_default=False,
        ),
    ]
