var Tree = function(value){
  var newTree = {};
  newTree.value = value;  //SOLUTION
  newTree.children = [];  //SOLUTION

  newTree.addChild = function(value){
  /* START SOLUTION */
    var child = Tree(value);
    this.children.push(child);
  /* END SOLUTION */
  };

  newTree.contains = function(target){
  /* START SOLUTION */
    var found = false;
    var subroutine = function(node){
      if ( node.value === target ){
        found = true;
        return;
      }
      for ( var i = 0; i < node.children.length; i++ ){
        var child = node.children[i];
        subroutine(child);
      }
    }
    subroutine(this);
    return found;
  /* END SOLUTION */
  };

  return newTree;
};
