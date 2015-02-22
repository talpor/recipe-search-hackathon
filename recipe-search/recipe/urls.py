# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import patterns, url, include

from rest_framework.routers import DefaultRouter

from serializers import RecipeViewSet, IngredientViewSet

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
    url(r'^', include(router.urls)),
    url(r'^recipes/$', recipe_list, name="all-recipes"),
    url(r'^recipes/(?P<pk>[0-9]+)/$', recipe_detail,
        name="detail-recipe"),
    url(r'^ingredients/$', ingredient_detail, name="all-ingredients"),
    url(r'^ingredients/(?P<pk>[0-9]+)/$', ingredient_detail,
        name="detail-ingredients"),
)
