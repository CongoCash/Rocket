/* START SOLUTION */
// Merge two sorted arrays in sorted order
var merge = function (left, right) {
  var merged = [];
  var iL = 0, iR = 0;
  while (merged.length < left.length + right.length) {
    // Default to the left element for stability
    if (iR >= right.length || left[iL] <= right[iR])  {
      merged.push(left[iL]);
      iL += 1;
    } else {
      merged.push(right[iR]);
      iR += 1;
    }
  }
  return merged;
}
/* END SOLUTION */

var mergeSort = function(array) {
  // Your code here.
  /* START SOLUTION */
  var lists = [];
  // Split array into sublists
  // Natural variant: split array into pre-sorted sublists
  var currentList = [];
  lists = []
  for (var i = 0; i < array.length; i++) {
    if (currentList.length && array[i] < currentList[currentList.length-1]) {
      lists.push(currentList);
      currentList = [];
    }
    currentList.push(array[i]);
  }
  lists.push(currentList);
  // Until the entire array is sorted
  while (lists.length > 1) {
    var newLists = [];
    // Merge all adjacent lists
    for (var i = 0; i < Math.floor(lists.length/2); i++) {
      newLists.push(merge(lists[i*2], lists[i*2+1]))
    }
    // Include the leftover list if the number is odd
    if (lists.length % 2) {
      newLists.push(lists[lists.length-1]);
    }
    lists = newLists;
  }
  // we have a single, fully sorted list
  return lists[0];
  /* END SOLUTION */
};

var list = [3,89,14,1,6,334,9,0,44,101];

console.log('Before: ', list);
console.log('After: ',mergeSort(list));
