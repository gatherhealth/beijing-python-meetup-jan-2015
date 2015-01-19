# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import jsonfield.fields
import django_hstore.fields
import django_hstore.virtual


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HStoreExample',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('recording_user', models.PositiveIntegerField(null=True, blank=True)),
                ('flex_column', django_hstore.fields.DictionaryField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='HStoreSchemaExample',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('recording_user', models.PositiveIntegerField(null=True, blank=True)),
                ('flex_column', django_hstore.fields.DictionaryField(null=True, editable=False)),
                ('my_number', django_hstore.virtual.VirtualField(default=b'')),
                ('my_float', django_hstore.virtual.VirtualField(default=b'')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='JSONFieldExample',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('recording_user', models.PositiveIntegerField(null=True, blank=True)),
                ('flex_column', jsonfield.fields.JSONField(default=dict)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
