'use strict';
// Firstly, we need to wire this controller into the myApp module
angular.module('myApp')
  // Here we see the name of the service defined.
  // Following the name, we see an anonymous function.
  // It's important to note that services behave a bit differently
  // from controllers.  Where controllers manipulate the scope
  // to interact with users, services return objects which other
  // pieces of code will use as APIs.
  .factory('Tools', function ($timeout, $q, $http) {
    // Here, we are returning an object with a list and a method
    // that shows an alert with a specified name.  Any controller
    // can use this if the service is injected into the controller.
    return {
      "removeItem": function(list, index){
        list.splice(index, 1);
        return list;
      },
      "fakeTask": function(){
        var deferred = $q.defer();
        $timeout(function(){
          alert("fakeTask is now complete!");
          deferred.resolve(['Creepers', 'Skeletons', 'Zombies']);
        },2000);
        // Return the promise to allow other code to act
        // on the result.
        return deferred.promise;
      },
      "randomResult": function(){
        var deferred = $q.defer();
        $timeout(function(){
          if(Math.random() > 0.5){
            deferred.resolve("Successfully completed task!");
          }else{
            deferred.reject("The task failed!");
          }
        },100);
        // Return the promise to allow other code to act
        // on the result.
        return deferred.promise;
      },
      "randomInterval": function(){
        var deferred = $q.defer();
        var interval = Math.random() * 3000;
        $timeout(function(){
          deferred.resolve("Task took " + (interval/1000).toFixed(3) + " seconds to complete.");
        },interval);
        // Return the promise to allow other code to act
        // on the result.
        return deferred.promise;
      },
      // This function will return the argument multiplied
      // by 100 after waiting for two seconds.  This is to
      // demonstrate an asychronous activity.
      "multiplyByFive": function(num){
          var deferred = $q.defer();
          $timeout(function(){
              deferred.resolve(num * 5);
          },2000);
          // Return the promise to allow other code to act
          // on the result.
          return deferred.promise;
      },
      "authGithub": function(){
        var static_token;
        static_token = "3a8cc33336f9c939e4809af3b1906e5fce4e3d63";
        if(!static_token){
          var token = sessionStorage["token"];
          if(!token){
            token = prompt("Token");
            sessionStorage["token"] = token;
          }
        }else{
          var token = static_token;
        }
        // remove token
        // delete localStorage.token
        $http.defaults.headers.common['Authorization'] = "token " + token;

      }
    };
  });