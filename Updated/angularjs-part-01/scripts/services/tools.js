'use strict';
// Firstly, we need to wire this controller into the myApp module
angular.module('myApp')
  // Here we see the name of the service defined.
  // Following the name, we see an anonymous function.
  // It's important to note that services behave a bit differently
  // from controllers.  Where controllers manipulate the scope
  // to interact with users, services return objects which other
  // pieces of code will use as APIs.
  .factory('Tools', function () {
    // Here, we are returning an object with a list and a method
    // that shows an alert with a specified name.  Any controller
    // can use this if the service is injected into the controller.
    return {
      "removeItem": function(list, index){
        list.splice(index, 1);
        return list;
      }
    };
  });