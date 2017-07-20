// Add your code to the function stubs below to implement a stack

var Stack = function(){
  var stack = {};

  // Use an object with numeric keys to store values
  var stackItem = {};
  /* START SOLUTION */
  var size = 0;
  /* END SOLUTION */

  // Implement the methods below
  stack.push = function(item){
    /* START SOLUTION */
    stackItem[size] = item;
    size++;
    /* END SOLUTION */
  };

  stack.pop = function(){
    /* START SOLUTION */
    size && size--;
    var result = stackItem[size];

    delete stackItem[size];

    return result;
    /* END SOLUTION */
  };

  stack.size = function(){
    /* START SOLUTION */
    return size;
    /* END SOLUTION */
  };

  return stack;
};
