# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('added_at', models.DateTimeField(auto_now=True)),
                ('description', models.TextField(null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('question', models.TextField()),
                ('question_type', models.CharField(max_length=20, choices=[(b'A', b'Sec A'), (b'B', b'Sec B'), (b'C', b'Sec C')])),
                ('unit_number', models.PositiveSmallIntegerField(null=True, blank=True)),
                ('comments', models.TextField(null=True, blank=True)),
                ('added_at', models.DateTimeField(auto_now=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('subject_code', models.CharField(max_length=200, null=True, blank=True)),
                ('name', models.CharField(max_length=200)),
                ('added_at', models.DateTimeField(auto_now=True)),
                ('description', models.TextField(null=True, blank=True)),
                ('category', models.ForeignKey(to='paper.Category')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='question',
            name='subject',
            field=models.ForeignKey(to='paper.Subject'),
            preserve_default=True,
        ),
    ]
