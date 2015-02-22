# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import patterns, url, include

from rest_framework.routers import DefaultRouter

from serializers import RecipeViewSet

router = DefaultRouter()
router.register('recipes', RecipeViewSet)

recipe_list = RecipeViewSet.as_view({
    'get': 'list',
})

urlpatterns = patterns('',
    url(r'^', include(router.urls)),
    url(r'^recipes/$', recipe_list, name="all-recipes"),
)
