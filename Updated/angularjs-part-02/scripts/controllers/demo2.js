'use strict';
// Firstly, we need to wire this controller into the myApp module
angular.module('myApp')
  // Here we see the name of the controller defined.
  // Following the name, we see an anonymous function with two arguments.
  // These arguments are functionality being injected into the controller.
  // Think of this as being like including scripts in HTML. 
  // Unless they are referenced here, you cannot utilize them.
  .controller('DemoController2', function ($scope, $http, DemoService, Tools) {
    // The rest of the function defines the behavior & data that the controller will manage.
    // Let's ask the tools service what 5 times 6 is.
    var request_calc = Tools.multiplyByFive(6);
    // And when it's done determining the value, let's add it to the scope.
    request_calc.then(function(result){
      $scope.result = result;
    });
    // Here we can see an example of how to access form information from the $scope via controller.
    $scope.validStatus = function(){
      alert($scope.demoForm.demoField.$valid);
    }
  });