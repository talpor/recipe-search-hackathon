# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0002_auto_20150221_2013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingrediententry',
            name='quantity',
            field=models.CharField(default=b'', max_length=16),
            preserve_default=True,
        ),
    ]
