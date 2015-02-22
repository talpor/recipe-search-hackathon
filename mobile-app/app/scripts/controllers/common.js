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

             Ingredients.getAll($scope.search_term).then(
                 function(ingredients){
                     $scope.allIngredients = ingredients;
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

             $scope.showSearchResults = function(){
                 Search.setSearchParameters($scope.selectedIngredients,
                                            $scope.availableTime);
                 $state.go('search-results');
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
             Search.getSearchResults().then(
                 function(recipes){
                     $scope.recipes = recipes;
                     $ionicLoading.hide();
                 }
             );
         }]
    );
