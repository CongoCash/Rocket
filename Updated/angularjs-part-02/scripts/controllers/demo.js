'use strict';
// Firstly, we need to wire this controller into the myApp module
angular.module('myApp')
  // Here we see the name of the controller defined.
  // Following the name, we see an anonymous function with two arguments.
  // These arguments are functionality being injected into the controller.
  // Think of this as being like including scripts in HTML. 
  // Unless they are referenced here, you cannot utilize them.
  .controller('DemoController', function ($scope, $http, DemoService, Tools) {
    // The rest of the function defines the behavior & data that the controller will manage.
    // Let's look up Github repositories that belong to Tivix
    var repos_request = $http.get("https://api.github.com/users/tivix/repos");
    // If we successfully retrieve them, then let's add them to the scope.
    repos_request.success(function(data){
      $scope.items = data;
    });
    // If there's an error though, then let's tell the user
    repos_request.error(function(data){
      $scope.error = ["There was a problem retrieving the data."];
    });
  });