'use strict';

/* global angular */

angular.module('RecipeSearch.controllers', ['RecipeSearch.services'])
  .controller('AppCtrl', [
    '$ionicPlatform',
    '$rootScope',
    '$state',
    '$ionicSideMenuDelegate',
    '$ionicModal',
    'settings',
    function(
      $ionicPlatform,
      $rootScope,
      $state,
      $ionicSideMenuDelegate,
      $ionicModal,
      settings
    ){
      //////////////////////////////
      //           INIT           //
      //////////////////////////////
      $ionicPlatform.ready();
    }
  ])
    .controller(
        'SearchRecipeCtrl',
        ['$scope', 'Ingredients',
         function($scope, Ingredients) {
         }]
    );
