# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import patterns, url, include

from rest_framework.routers import DefaultRouter

from serializers import RecipeViewSet, IngredientViewSet, \
    RecipeSearchIngTimeViewSet, RecipeRandomIngTimeViewSet

router = DefaultRouter()
router.register('recipes', RecipeViewSet)
router.register('ingredients', IngredientViewSet)

recipe_list = RecipeViewSet.as_view({
    'get': 'list',
})


recipe_detail = RecipeViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'delete': 'destroy',
})

recipe_search_ingtime = RecipeSearchIngTimeViewSet.as_view()

recipe_random_ingtime = RecipeRandomIngTimeViewSet.as_view()

ingredient_list = IngredientViewSet.as_view({
    'get': 'list',
    'post': 'create',
})


ingredient_detail = IngredientViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'delete': 'destroy',
})


urlpatterns = patterns('',
    # Home
    url(r'^', include(router.urls)),

    # Recipe search by ingredients and time
    url(r'^recipes/search/ingredient_time/$', recipe_search_ingtime,
        name="recipe-search-ingtime"),

    # Random recipe by ingredients and time
    url(r'^recipes/random/ingredient_time/$', recipe_random_ingtime,
        name="recipe-random-ingtime"),
)
