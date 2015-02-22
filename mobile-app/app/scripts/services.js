'use strict';

/* global facebookConnectPlugin, _, SockJS, localNotification, angular */

angular.module('RecipeSearch.services', ['settings'])
  .factory(
      'Ingredients',
      ['$http', '$q', '$timeout',
       function($http, $q, $timeout) {
           var ingredientsUrl = '/ingredients/';
           var queryIngredients = function(params){
               return $http.get(ingredientsUrl, {'apiRequest': true,
                                                 'params': params});
           };
           var getAllIngredients = function(){
               var deferred = $q.defer();

               $timeout( function(){
                   deferred.resolve([
                       { name: 'Paprika' },
                       { name: 'Black Pepper' },
                       { name: 'White Rice' },
                   ]);
               }, 1500);

               return deferred.promise;
           };

           return {
               query: queryIngredients,
               getAll: getAllIngredients
           };
       }]
  )
    .factory('Search',
      ['$http', '$q', '$timeout',
       function($http, $q, $timeout) {
           var searchUrl = '/search/';
           var selectedIngredients = [];
           var availableTime = 0;
           var searchQuery = function(params){
               return $http.get(searchUrl, {'apiRequest': true,
                                            'ingredients': selectedIngredients,
                                            'available_time': availableTime});
           };

           var setSearchParameters = function(ingredients, time){
               selectedIngredients = ingredients;
               availableTime = time;
           };

           var getSearchResults = function(){
               var deferred = $q.defer();
               $timeout( function(){
                   deferred.resolve([
                       { name: 'Chicken Parmesan',
                         rating: '4',
                         thumbnail: 'http://d1ujpofy5vmb70.cloudfront.net/wp-content/uploads/featured_image/GuiltlessChickenParmesan_article.jpg',
                         cook_time: '20 mins',
                         prep_time: '10 mins',
                         id: 1
                       },
                       { name: 'Grilled Salmon',
                         rating: '4',
                         thumbnail: 'http://www.flavour.ca/~/media/Flavour-Hub/Recipe-Images/500x500/Club-House/grilled-salmon-asparagus-salad_500x500.ashx',
                         cook_time: '15 mins',
                         prep_time: '0 mins',
                         id: 3
                       },
                       { name: 'Cuba Libre',
                         rating: '1',
                         thumbnail: 'http://i1.cpcache.com/product_zoom/68615043/cuba_libre_free_cuba_postcards_package_of_8.jpg?height=250&width=250&padToSquare=true',
                         id: 4
                       },
                       { name: 'Appletini',
                         rating: '4',
                         thumbnail: 'http://www.mixednotstirred.net/images/products/cocktail_wine_mixes_sour_appletini_cocktail_mix.jpg',
                         id: 5
                       },
                       { name: 'Chicken Parmesan',
                         rating: '4',
                         thumbnail: 'http://d1ujpofy5vmb70.cloudfront.net/wp-content/uploads/featured_image/GuiltlessChickenParmesan_article.jpg',
                         cook_time: '20 mins',
                         prep_time: '10 mins',
                         id: 1
                       },
                       { name: 'Chicken Parmesan',
                         rating: '4',
                         thumbnail: 'http://d1ujpofy5vmb70.cloudfront.net/wp-content/uploads/featured_image/GuiltlessChickenParmesan_article.jpg',
                         cook_time: '20 mins',
                         prep_time: '10 mins',
                         id: 1
                       },
                       { name: 'Chicken Parmesan',
                         rating: '4',
                         thumbnail: 'http://d1ujpofy5vmb70.cloudfront.net/wp-content/uploads/featured_image/GuiltlessChickenParmesan_article.jpg',
                         cook_time: '20 mins',
                         prep_time: '10 mins',
                         id: 1
                       }
                   ]);
               }, 1500);

               return deferred.promise;
           };

           return {
               setSearchParameters: setSearchParameters,
               getSearchResults: getSearchResults
           };
       }]
  );

/**
 * Utilities for localstorage, notifications and popups
 */
angular.module('ionic.utils', [])
  .factory('$localstorage', ['$window', function($window) {
    return {
      set: function(key, value) {
        $window.localStorage[key] = value;
      },
      unset: function(key) {
        $window.localStorage.removeItem(key);
      },
      get: function(key, defaultValue) {
        return $window.localStorage[key] || defaultValue;
      },
      setObject: function(key, value) {
        $window.localStorage[key] = JSON.stringify(value);
      },
      getObject: function(key) {
        return JSON.parse($window.localStorage[key] || '{}');
      }
    };
  }])
  .factory('$popup', ['$ionicPopup', function($ionicPopup) {
    var alert = function(message, title) {
      $ionicPopup.alert({ title: title, template: message });
    };
    return {
      alert: alert
    };
  }]);
