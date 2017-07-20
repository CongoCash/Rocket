// Feel free to add helper functions if needed.
/* START SOLUTION */
var swap = function(index1, index2, array) {
  var temp = array[index1];
  array[index1] = array[index2];
  array[index2] = temp;
  return array;
};
/* END SOLUTION */

var bubbleSort = function(array) {
  // Your code here.
  /* START SOLUTION */
  var len = array.length;

  for (var i = 0; i < len; i++) {
    var swaps = 0;
    // Do j < len - 1 - i iterations so we don't consider the final (sorted)
    // element in the array in future iterations
    for (var j = 0; j < len - 1 - i; j++) {
      if (array[j] > array[j + 1]) {
        swaps++;
        swap(j, j + 1, array);
      }
    }

    // If no swaps were done during this iteration, then the array is sorted
    // and we can bail out
    if (!swaps) { break; }
  }

  return array;
  /* END SOLUTION */
};

var list = [3,89,14,1,6,334,9,0,44,101];

console.log('Before: ', list);
console.log('After: ',bubbleSort(list));
