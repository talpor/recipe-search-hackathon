# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=128)),
                ('description', models.TextField(null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='recipe',
            name='categories',
            field=models.ManyToManyField(to='recipe.Category'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='recipe',
            name='description',
            field=models.TextField(null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='recipe',
            name='name',
            field=models.CharField(default='default_name', unique=True, max_length=128),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='ingrediententry',
            name='quantity',
            field=models.FloatField(default=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='ingrediententry',
            name='unit',
            field=models.CharField(max_length=16, choices=[(b'kg', b'kilogram'), (b'gr', b'gram'), (b'mg', b'miligrams'), (b'lb', b'pound'), (b'oz', b'ounce'), (b'gr', b'gram'), (b'lt', b'liter'), (b'ml', b'mililiter'), (b'gal', b'gallon'), (b'1', b'one'), (b'2', b'half'), (b'3', b'third'), (b'4', b'quarter'), (b'tsp', b'teaspoon'), (b'tbsp', b'tablespoon'), (b'cup', b'cup'), (b'scp', b'scoop'), (b'pch', b'pinch'), (b'dsh', b'dash')]),
            preserve_default=True,
        ),
    ]
