# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0006_auto_20150222_1158'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipe',
            old_name='time',
            new_name='cook_time',
        ),
        migrations.AddField(
            model_name='recipe',
            name='prep_time',
            field=models.PositiveSmallIntegerField(null=True),
            preserve_default=True,
        ),
    ]
