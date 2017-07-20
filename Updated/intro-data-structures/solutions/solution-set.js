var Set = function(){
  var set = Object.create(setProps);
  set._members = undefined;
  /* START SOLUTION */
  set._members = {};
  /* END SOLUTION */
  return set;
};

var setProps = {};

setProps.add = function(item){
  /* START SOLUTION */
  this._members[item] = true;
  /* END SOLUTION */
};

setProps.contains = function(item){
  /* START SOLUTION */
  return !!this._members[item];
  /* END SOLUTION */
};

setProps.remove = function(item){
  /* START SOLUTION */
  delete this._members[item];
  /* END SOLUTION */
};
