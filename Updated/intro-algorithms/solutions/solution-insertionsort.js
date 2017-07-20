var insertionSort = function(array) {
  /* START SOLUTION */

  for(var i = 1; i < array.length; i++) {
    var val = array[i];
    var hole = i;

    while(hole > 0  &&  val < array[hole - 1]) {
      array[hole] = array[hole - 1];
      hole -= 1;
    }

    array[hole] = val;
  }

  return array;
  
  /*END SOLUTION*/
};

var list = [3,89,14,1,6,334,9,0,44,101];

console.log('Before: ', list);
console.log('After: ',insertionSort(list));
