# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations

from lxml import etree

import re

COOKBOOK_FILE = "../uploads/cookbook_import_pages_current.xml"
GLOBAL_PATTERN = '[^=]*=+\s?[Ii]ngredients\s?=+([^=]+)=+\s?[Dd]irections\s?=+([^=]+?)(?:\n\s*\[.*)|[^=]*=+\s?[Ii]ngredients\s?=+([^=]+)=+\s?[Dd]irections\s?=+([^=]+)'


def parse_ingredients(text):
    result = []

    for l in text.splitlines():
        p_quant='\d?(¾|½|¼|⅓|⅔|⅕|⅖|⅗|⅘|\d)'
        p_unit='oz|dash|dashes|ounce'
        p_ing='\[\[([a-zA-Z\d\s\'\áéíóúÁÉÍÓÚ]+)\]\]'

        m = re.search(p_quant, l)
        quant = m.group() if m else None

        m = re.search(p_unit, l)
        unit = m.group() if m else None

        m = re.search(p_ing, l)
        ing = m.groups()[0] if m and m.groups() else None

        if ing:
            result.append((quant if quant else '1',
                           unit if unit else '',
                           ing.lower()))
        else:
            result.append(None)

    return result


def load_data(apps, schema_editor):
    Ingredient = apps.get_model("recipe", "Ingredient")
    IngredientEntry = apps.get_model("recipe", "IngredientEntry")
    Recipe = apps.get_model("recipe", "Recipe")

    root = etree.parse(COOKBOOK_FILE).getroot()
    count = 0

    for cookbook in root:
        children = cookbook.getchildren()

        title = ''
        text = ''
        valid_recipe = False

        for child in children:
            if 'title' in child.tag:
                title = child.text.lower()

            if 'revision' in child.tag:
                real_content = child.getchildren()
                for content in real_content:
                    if content.text and 'text' in content.tag and \
                       ('Ingredients' in content.text or 'ingredients' in content.text) and \
                       ('Directions' in content.text or 'directions' in content.text):
                        text = content.text
                        # Here, we know that is a valid recipe
                        valid_recipe = True

        if valid_recipe:
            match = re.match(GLOBAL_PATTERN, text)

            if not match:
                continue

            groups = match.groups()

            entries = groups[0] or groups[2]
            instructions = groups[1] or groups[3]

            # parse ingredients
            ingredients_list = parse_ingredients(entries)
            recipe, recipe_created = Recipe.objects.get_or_create(name = title)

            if not recipe_created:
                continue

            count += 1
            print "Loaded (%s, %s)"%(count, title)
            for element in ingredients_list:

                if not element:
                    continue

                ingredient, _ = Ingredient.objects.get_or_create(name = element[2])
                unit = element[1]
                quantity = element[0]

                ingredient_entry, _ = IngredientEntry.objects\
                                                     .get_or_create(ingredient = ingredient,
                                                                    unit = unit,
                                                                    quantity = quantity)
                recipe.ingredients.add(ingredient_entry)

            # parse instructions
            instructions = filter(None, instructions.split('\n'))
            for n, instruction in enumerate(instructions):
                instructions[n] = instruction.replace('#','')\
                                             .replace('[','')\
                                             .replace(']','')\
                                             .strip()

            json_instructions = {'instructions': instructions}
            recipe.instructions = json_instructions
            recipe.save()

    print "Number of Cookbook loaded:",count

def load_data_backwards(apps, schema_editor):
    pass

class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0004_auto_20150221_2100'),
    ]

    operations = [
        migrations.RunPython(load_data, load_data_backwards),
    ]
