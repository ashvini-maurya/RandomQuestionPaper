# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('paper', '0003_auto_20151107_0007'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='marks',
        ),
    ]
