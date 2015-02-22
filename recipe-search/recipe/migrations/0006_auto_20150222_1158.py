# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0005_auto_20150221_2300'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingrediententry',
            name='unit',
            field=models.CharField(max_length=16),
            preserve_default=True,
        ),
    ]
