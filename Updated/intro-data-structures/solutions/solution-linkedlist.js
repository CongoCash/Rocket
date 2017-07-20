var LinkedList = function(){
  var list = {};
  list.head = null;
  list.tail = null;

  list.addToTail = function(value){
  /* START SOLUTION */
    var newTail = Node(value);

    if (!list.head) {
      list.head = newTail;
    }

    if (list.tail) {
      list.tail.next = newTail;
    }

    list.tail = newTail;
  /* END SOLUTION */
  };

  list.removeHead = function(){
    /* START SOLUTION */
    if (list.head === null){
      return null;
    }

    var currentHead = list.head;
    list.head = list.head.next;

    return currentHead.value;
    /* END SOLUTION */
  };

  list.contains = function(target){
    /* START SOLUTION */
    var node = list.head;

    while (node) {
      if (node.value === target) {
        return true;
      }

      node = node.next;
    }

    return false;
    /* END SOLUTION */
  };

  return list;
};

var Node = function(value){
  var node = {};

  node.value = value;
  node.next = null;

  return node;
};

