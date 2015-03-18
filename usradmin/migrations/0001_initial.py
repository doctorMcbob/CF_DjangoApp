# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BasicUser',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('first', models.CharField(max_length=20)),
                ('last', models.CharField(blank=True, max_length=20)),
                ('email', models.EmailField(max_length=254)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
