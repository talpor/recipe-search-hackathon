# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0007_auto_20150222_1536'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='image',
            field=models.FileField(null=True, upload_to=b'recipe_images'),
            preserve_default=True,
        ),
    ]
