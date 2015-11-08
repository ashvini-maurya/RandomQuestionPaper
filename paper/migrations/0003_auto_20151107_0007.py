# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('paper', '0002_auto_20151107_0004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='marks',
            field=models.IntegerField(default=0),
        ),
    ]
