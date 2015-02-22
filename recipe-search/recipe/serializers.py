from rest_framework import viewsets, serializers
from rest_framework.filters import SearchFilter
from rest_framework.response import Response
from rest_framework.views import APIView

from models import Recipe, Ingredient


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
        params = request.query_params
        ingredients = [int(i) for i in params.getlist('ings')]
        time = params.get('time')

        ret = self.queryset
        ret = ret.filter(ingredients__ingredient__in=ingredients)

        if time:
            ret = ret.filter(time__lte=time)

        return Response(self.serializer_class(ret, many=True).data)
