'use strict';

/* global angular, _ */

angular.module('RecipeSearch.controllers', ['RecipeSearch.services', 'ionic.rating'])
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
        ['$scope','$state', '$ionicLoading', '$ionicModal', 'Ingredients', 'Search',
         function($scope, $state, $ionicLoading, $ionicModal, Ingredients, Search){
             $scope.loadingIndicator = $ionicLoading.show({
	         content: 'Loading Ingredients',
	         animation: 'fade-in',
	         showBackdrop: true,
	     });

             $scope.allIngredients = [];
             $scope.availableTime = 4;
             $scope.ingredientsData = [];
             $scope.selectedIngredients = [];
             $scope.searchTerm = '';

             Ingredients.query().then(
                 function(response){
                     $scope.allIngredients = response.data;
                     $ionicLoading.hide();
                 }
             );

             $ionicModal.fromTemplateUrl('ingredient-modal.html', {
                 scope: $scope,
                 animation: 'slide-in-up'
             }).then(function(modal) {
                 $scope.modal = modal;
             });

             $scope.showModal = function() {
                 $scope.modal.show();
             };

             $scope.closeModal = function() {
                 $scope.modal.hide();
             };

             $scope.notSelected = function(ingredient, index){
                 return _.indexOf($scope.selectedIngredients, ingredient) === -1;
             };

             $scope.addIngredient = function(ingredient){
                 $scope.selectedIngredients.push(ingredient);
                 $scope.searchTerm = '';
                 $scope.modal.hide();
             };

             $scope.deleteIngredient = function(ingredient){
                 _.pull($scope.selectedIngredients, ingredient);
             };

             $scope.getRandomRecipe = function(){
                 $state.go('recipe', {'recipeId': 1});
             };

             $scope.showSearchResults = function(){
                 Search.setSearchParameters($scope.selectedIngredients,
                                            $scope.availableTime);
                 $state.go('results');
             };
         }]
    )
    .controller(
        'SearchResultsCtrl',
        ['$scope', '$ionicLoading', 'Search',
         function($scope, $ionicLoading, Search){
             $scope.loadingIndicator = $ionicLoading.show({
	         content: 'Loading Results',
	         animation: 'fade-in',
	         showBackdrop: true,
	     });

             $scope.recipes = [];
             Search.searchQuery().then(
                 function(response){
                     $scope.recipes = response.data;
                     $ionicLoading.hide();
                 }
             );
         }]
    )
    .controller(
        'RecipeDetailCtrl',
        ['$scope', '$stateParams', '$ionicLoading', 'Recipe',
         function($scope, $stateParams, $ionicLoading, Recipe){
             $scope.loadingIndicator = $ionicLoading.show({
	         content: 'Loading Recipe',
	         animation: 'fade-in',
	         showBackdrop: true,
	     });

             $scope.recipe = {};

             Recipe.getById($stateParams.recipeId).then(
                 function(response){
                     $scope.recipe = response.data;
                     // TODO: Do this on the server
                     $scope.recipe.instructions = JSON.parse($scope.recipe.instructions.replace(/u\'/g, "'").replace(/\'/g, "\"").replace(/\\xa0/g, ""));
                     $ionicLoading.hide();
                 }
             );
         }]
    );
