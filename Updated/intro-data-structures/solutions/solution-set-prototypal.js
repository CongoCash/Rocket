var Set = function(){
  var set = {};

  set._members = undefined;
  /* START SOLUTION */
  set._members = {};
  /* END SOLUTION */

  set.add = function(item){
    /* START SOLUTION */
    this._members[item] = true;
    /* END SOLUTION */
  };

  set.contains = function(item){
    /* START SOLUTION */
    return !!this._members[item];
    /* END SOLUTION */
  };

  set.remove = function(item){
    /* START SOLUTION */
    delete this._members[item];
    /* END SOLUTION */
  };

  return set;
};



