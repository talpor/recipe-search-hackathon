'use strict';

/* global StatusBar */

// Ionic Starter App, v0.9.20

// angular.module is a global place for creating, registering and retrieving Angular modules
// 'starter' is the name of this angular module example (also set in a <body> attribute in index.html)
// the 2nd parameter is an array of 'requires'
// 'starter.services' is found in services.js
// 'starter.controllers' is found in controllers.js

(function(){

  angular.module('RecipeSearch', ['ionic', 'ionic.utils',  'settings', 'RecipeSearch.controllers'])

  .run(
    ['$ionicPlatform', '$rootScope', '$state', 'settings',
    function($ionicPlatform, $rootScope, $state, settings) {
      $ionicPlatform.ready(function() {
        // inject settings into scope
        $rootScope.settings = settings;

        if(navigator.splashscreen){
          setTimeout(function() {
            navigator.splashscreen.hide();
          }, 1000);
        }

        // Hide the accessory bar by default (remove this to show the accessory bar above the keyboard
        // for form inputs)
        if(window.cordova && window.cordova.plugins && window.cordova.plugins.Keyboard) {
          window.cordova.plugins.Keyboard.hideKeyboardAccessoryBar(true);
        }

        // hide the status bar (org.apache.cordova.statusbar required)
        if(typeof StatusBar !== 'undefined') {
          // org.apache.cordova.statusbar required
          StatusBar.styleDefault();
        }
      });
    }]
  )

  .config(['$stateProvider', '$urlRouterProvider', '$httpProvider', function($stateProvider, $urlRouterProvider, $httpProvider) {

    $stateProvider
      .state('search', {
          url: '/recipe/search/',
          templateUrl: 'templates/recipe_search.html',
          controller: 'SearchRecipeCtrl'
      })
      .state('results', {
          url: '/recipe/search-results/',
          templateUrl: 'templates/search_results.html',
          controller: 'SearchResultsCtrl'
      })
      .state('recipe', {
          url: '/recipe/{recipeId}',
          templateUrl: 'templates/recipe_detail.html',
          controller: 'RecipeDetailCtrl'
      });

    // if none of the above states are matched, use this as the fallback
    // Example of using function rule as param
    $urlRouterProvider.otherwise('/recipe/search/');

    // Register an interceptor (via an anonymous factory) for handle
    // appropriately the request url using the api endpoints.
    $httpProvider.interceptors.push(['settings', function(settings) {
      return {
        request: function(config) {
          if(config.apiRequest){
            var url = config.url,
                newUrl = /^\//.test(url) ? url.substring(1, url.length) : url;
            config.url = settings.apiEndpoint.url + '/' + newUrl;
          }

          return config;
        }
      };
    }]);
  }]);

})();
