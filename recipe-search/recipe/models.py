from jsonfield import JSONField

from django.db import models

MASS_UNITS = (
    ('kg', 'kilogram'),
    ('gr', 'gram'),
    ('mg', 'miligrams'),
    ('lb', 'pound'),
    ('oz', 'ounce'),
    ('gr', 'gram'),
    ('lt', 'liter'),
    ('ml', 'mililiter'),
    ('gal', 'gallon'),
    ('1', 'one'),
    ('2', 'half'),
    ('3', 'third'),
    ('4', 'quarter'),
    ('tsp', 'teaspoon'),
    ('tbsp', 'tablespoon'),
    ('cup', 'cup'),
    ('scp', 'scoop'),
    ('pch', 'pinch'),
    ('dsh', 'dash'),
)

UNITS = (
    ('f', 'fahrenheit'),
    ('c', 'celcius'),
    ('sec', 'second'),
    ('min', 'minute'),
    ('hr', 'hour'),
    ('lw', 'low'),
    ('md', 'medium'),
    ('hg', 'high'),
) + MASS_UNITS


class Ingredient(models.Model):
    name = models.CharField(max_length=64, unique=True)
    substitutes = models.ManyToManyField('Ingredient', null=True)
    description = models.TextField(null=True)

    def __unicode__(self):
        return self.name


class IngredientEntry(models.Model):
    ingredient = models.ForeignKey('Ingredient')
    unit = models.CharField(choices=MASS_UNITS, max_length=16)
    quantity = models.FloatField(default=0)

    def __unicode__(self):
        return "%s %s %s" % (self.ingredient.name, self.quantity, self.unit)


class Recipe(models.Model):
    name = models.CharField(max_length=128, unique=True)
    categories = models.ManyToManyField('Category')
    description = models.TextField(null=True)
    ingredients = models.ManyToManyField('IngredientEntry')
    time = models.PositiveSmallIntegerField(null=True)
    instructions = JSONField(null=True)
    notes = JSONField(null=True)

    def __unicode__(self):
        return "%s" % self.name


class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)
    description = models.TextField(null=True)

    def __unicode__(self):
        return "%s" % self.name
