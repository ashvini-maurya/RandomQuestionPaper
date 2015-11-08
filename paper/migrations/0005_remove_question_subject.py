# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('paper', '0004_remove_question_marks'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='subject',
        ),
    ]
