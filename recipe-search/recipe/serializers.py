from rest_framework import viewsets, serializers
from rest_framework.filters import SearchFilter

from models import Recipe, Ingredient


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        depth = 1


class IngredientViewSet(viewsets.ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
    filter_backends = (SearchFilter,)
    search_fields = ('name', 'description', 'substitutes__name')


class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        depth = 2


class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    filter_backends = (SearchFilter,)
    search_fields = ('name', 'description', 'time',
                     'categories__name',
                     'ingredients__ingredient__name',
                     )
