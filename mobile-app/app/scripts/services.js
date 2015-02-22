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
