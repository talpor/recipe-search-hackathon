from rest_framework import viewsets, serializers
from rest_framework.filters import SearchFilter
from rest_framework.response import Response
from rest_framework.views import APIView

from models import Recipe, Ingredient


def search_by_time_ingredients(ingredients, total_time,
                               prep_time, cook_time, queryset):
    '''
    Helper function to search by available ingredients and time
    '''

    recipes = queryset

    # Add valid substitutes to the ingredient list
    subs = []
    for i in ingredients:
        for s in Ingredient.objects.get(pk=i).substitutes.all():
            subs.append(s.pk)
    ingredients = ingredients + subs

    # Filter by ingredients
    recipes = recipes.filter(ingredients__in=ingredients)

    if prep_time:
        recipes = recipes.filter(prep_time__lte=prep_time)
    if cook_time:
        recipes = recipes.filter(cook_time__lte=cook_time)

    # Weed out the recipes that require at least one
    # ingredient not in the list that is not a substitute
    for r in recipes:
        for i in r.ingredients.all():
            if i.ingredient.pk not in ingredients:
                recipes = recipes.exclude(pk=r.pk)
                break

    return recipes


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        depth = 1


class IngredientViewSet(viewsets.ModelViewSet):
    """
    Default endpoints to view/search/create/modify/delete ingredients
    """
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
    filter_backends = (SearchFilter,)
    search_fields = ('name', 'description', 'substitutes__name')


class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        depth = 2


class RecipeViewSet(viewsets.ModelViewSet):
    """
    Default endpoints to view/search/create/modify/delete recipes
    """
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    filter_backends = (SearchFilter,)
    search_fields = ('name', 'description', 'time',
                     'categories__name',
                     'ingredients__ingredient__name',
                     )


class RecipeSearchIngTimeViewSet(APIView):
    """
    Search by ingredients endpoint
    """

    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

    def get(self, request, format=None):

        # Get parameters
        params = request.query_params
        ingredients = [int(i) for i in params.getlist('ings')]
        prep_time = params.get('prep_time')
        cook_time = params.get('cook_time')
        total_time = 0

        recipes = search_by_time_ingredients(ingredients, total_time,
                                             prep_time, cook_time,
                                             self.queryset)

        return Response(self.serializer_class(recipes, many=True).data)


class RecipeRandomIngTimeViewSet(APIView):
    """
    Search by ingredients endpoint
    """

    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

    def get(self, request, format=None):

        # Get parameters
        params = request.query_params
        ingredients = [int(i) for i in params.getlist('ings')]
        prep_time = params.get('prep_time')
        cook_time = params.get('cook_time')
        total_time = 0

        recipes = search_by_time_ingredients(ingredients, total_time,
                                             prep_time, cook_time,
                                             self.queryset)

        recipe = recipes.order_by('?').first()

        return Response(self.serializer_class(recipe).data)
