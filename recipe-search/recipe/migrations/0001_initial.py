# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=64)),
                ('description', models.TextField(null=True)),
                ('substitutes', models.ManyToManyField(to='recipe.Ingredient', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='IngredientEntry',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('unit', models.CharField(max_length=16, choices=[(b'kg', b'kilogram'), (b'gr', b'gram'), (b'mg', b'miligrams'), (b'lb', b'pound'), (b'oz', b'ounce'), (b'gr', b'gram'), (b'lt', b'liter'), (b'ml', b'mililiter'), (b'gal', b'gallon'), (b'1', b'one'), (b'2', b'half'), (b'3', b'third'), (b'4', b'quarter'), (b'tsp', b'teaspoon'), (b'tbsp', b'tablespoon'), (b'cup', b'cup'), (b'pch', b'pinch')])),
                ('quantity', models.PositiveSmallIntegerField(default=0)),
                ('ingredient', models.ForeignKey(to='recipe.Ingredient')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('time', models.PositiveSmallIntegerField(null=True)),
                ('instructions', jsonfield.fields.JSONField(null=True)),
                ('notes', jsonfield.fields.JSONField(null=True)),
                ('ingredients', models.ManyToManyField(to='recipe.IngredientEntry')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
