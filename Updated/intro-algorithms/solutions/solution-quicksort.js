var quickSort = function(array) {
  /* START SOLUTION */
  if (array.length <= 1) { return array; }

  var pivot = array[0];

  var left = array.slice(1).filter(function (x) {
    return x < pivot;
  });

  var right = array.slice(1).filter(function (x) {
    return x >= pivot;
  });

  return concat(quickSort(left), [pivot], quickSort(right));
  /* END SOLUTION */
};

/* START SOLUTION */
var concat = function () {
  return [].concat.apply([], arguments);
};
/* END SOLUTION */

var list = [3,89,14,1,6,334,9,0,44,101];

console.log('Before: ', list);
console.log('After: ',quickSort(list));