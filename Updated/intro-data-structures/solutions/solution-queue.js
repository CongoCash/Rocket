// Add your code to the function stubs below to implement a queue

var Queue = function(){
  var queue = {};

  // Remember, a queue has numeric indexes. You can use an object to store values and give them numeric keys.
  var queueItem = {};
  /* START SOLUTION */
  var start = -1;
  var end = -1;
  /* END SOLUTION */

  // Implement the methods below

  queue.enqueue = function(item){
    /* START SOLUTION */
    end++;
    queueItem[end] = item;
    /* END SOLUTION */
  };

  queue.dequeue = function(){
    /* START SOLUTION */
    queue.size() && start++;
    var result = queueItem[start];

    delete queueItem[start];

    return result;
    /* END SOLUTION */
  };

  queue.size = function(){
    /* START SOLUTION */
    return end - start;
    /* END SOLUTION */
  };

  return queue;
};
