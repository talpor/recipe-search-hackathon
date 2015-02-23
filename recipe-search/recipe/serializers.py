from django.db.models import Q
from rest_framework import viewsets, serializers
from rest_framework.filters import SearchFilter
from rest_framework.response import Response
from rest_framework.views import APIView

from django.db.models import Q, F

from models import Recipe, Ingredient


class IngredientSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()

    def get_name(self, obj):
        return obj.name.strip().title()

    class Meta:
        model = Ingredient
        depth = 1
        exclude = ['description', 'substitutes']


class IngredientViewSet(viewsets.ModelViewSet):
    """
    Default endpoints to view/search/create/modify/delete ingredients
    """
    queryset = Ingredient.objects.all().order_by('name')
    serializer_class = IngredientSerializer
    paginate_by = None
    filter_backends = (SearchFilter,)
    search_fields = ('name', 'description', 'substitutes__name')


class RecipeSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    def get_image(self, obj):
        if obj.image:
            from sorl.thumbnail import get_thumbnail
            thumbnail_url = get_thumbnail(
                obj.image, '500x500', crop='center', format='PNG'
            ).url

            return self.context['request'].build_absolute_uri(thumbnail_url)

    class Meta:
        model = Recipe
        depth = 2


class RecipeSearchSerializer(serializers.ModelSerializer):
    thumbnail = serializers.SerializerMethodField()

    def get_thumbnail(self, obj):
        if obj.image:
            from sorl.thumbnail import get_thumbnail
            thumbnail_url = get_thumbnail(
                obj.image, '200x200', crop='center', format='PNG'
            ).url

            return self.context['request'].build_absolute_uri(thumbnail_url)

    class Meta:
        model = Recipe
        depth = 2
        exclude = ['description', 'ingredients', 'instructions', 'notes']


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

    # Time intervals for the search
    TIME_CHOICES = [(-1, 30), (30, 60), (60, 120), (120, 240), (-1, 999999)]

    queryset = Recipe.objects.all()
    serializer_class = RecipeSearchSerializer

    def get(self, request, format=None):
        # Get parameters
        params = request.query_params
        ingredients = [int(i) for i in params.getlist('ings')]
        time = params.get('time')

        recipes = self.queryset

        # Filter by ingredients
        recipes = recipes.filter(
            ingredients__ingredient__in=ingredients
        ).distinct()

        if time:
            time = int(time)
            lower_time = self.TIME_CHOICES[time][0]
            upper_time = self.TIME_CHOICES[time][1]

            recipes = recipes.filter(
                (Q(cook_time__gt=lower_time - F('prep_time')) &
                 Q(cook_time__lte=upper_time - F('prep_time'))) |
                (Q(cook_time__isnull=True) & Q(prep_time__isnull=True))
            )

        # Weed out the recipes that require at least one
        # ingredient not in the list
        for r in recipes:
            for i in r.ingredients.all():
                if i.ingredient.pk not in ingredients:
                    recipes = recipes.exclude(pk=r.pk)
                    break

        return Response(self.serializer_class(
            recipes, many=True, context={'request': request}
        ).data)
