Introduction to Algorithms
================

An [algorithm] is nothing more than a clear, step-by-step procedure for solving a problem. As a software engineer you will spend a great deal of your time analyzing problems and creating solutions. You can expect these problems to come with different constraints and criteria, and these will likely inform your decision to use one approach over another for a given task.

Over time you will begin to see that, like recipes, problems and algorithms fall into different categories. Your ability to analyze problems based on your past experience will go a long way toward helping you make an educated guess about a likely solution. This type of reasoning is more formally known as 'developing a [heuristic]', and is a valuable step in the process of selecting a suitable algorithmic solution.

Here is a short list of some common algoritm types. This is nowhere near complete, and an exhaustive study would take a lifetime. At this stage of your software training, the important thing is to have a basic understanding of concepts, and some limited exposure to these topics. 

###Algorithm Types

* [Brute-force]
* [Divide and Conquer]
  * Merge and Quick Sorts
* Search and Enumeration
  * [Tree Traversal]
* [Randomized Algorithms]
  * [Monte Carlo Algorithms]
  * [Las Vegas Algorithms]
* [Reduction of Complexity]
  * [Selection Algorithm]

####You are not expected to read all of the above material in detail for this class. It is a reference for your study, and hopefully will spark an interest in this fascinating subject. For even more interesting reading material and visualizations, check out the additional resource links at the end of this repo.

<hr>

One of the most basic categories of algorithms in software engineering is the [Sorting Algorithm]. It's a good place to start because it's an easy concept to understand. You have a list of things, and you rearrange them in order. And before you say it, yes it could be __ascending__ or __descending__ order, but for the purposes of this repo we will only be concerning ourselves with sorting __integers__ in __ascending__ order.

In this assignment you'll be writing code in __Python__ and __JavaScript__ to implement several types of sorting algorithms. They are:

  * Bubble Sort
  * Insertion Sort
  * Merge Sort
  * Quick Sort

Why are there so many different types of sorting algorithms when they all do the same thing? It turns out that they are not all the same, and this list is just the tip of the iceberg. 

Sorting algorithms vary in efficiency that can be measured in a variety of ways including [time complexity], [space complexity], and difficulty of implementation. Here is an excellent introduction to sorting algorithms (programmer complexity!) 

###Read this introduction before proceeding to the coding exercises below:

###[Intro to Sorting Algorithms]

<hr>

##Your Mission
Using the starter files in the `js/` and `py/` folders, you will implement the four sort algorithms listed below in __Python__ and __JavaScript__. You can use any resources, but start with the links on this page. They should be more than enough.

Make sure that you
  * DO make a fork of the main repo before beginning your work.
  * DO NOT copy and paste any code. 
  * DO test your code.
  * DO write your code with clean formatting.

###Sorting Algorithms


#### [Bubble Sort]

![bubblesort img]

####Pseudocode

* Compare pairs of adjacent elements of the sequence.
  * If the they are in the wrong order, swap them. 
* If not at the end of the sequence, move to the next pair and repeat.

<hr>

####[Insertion Sort]

![insertionsort img]

####Pseudocode

* Iterate through the array, starting from the second element:
  * Note the element at this index.
* Walk back through the previous elements until you find a smaller element (or the beginning of the array), moving each element up by one.
* Insert the noted element at this point.

<hr>

####[Merge Sort]
The merge sort algorithm uses the 'divide and conquer' strategy. It starts with the list of *length-n* and divides into a series of *n* sublists of length 1. Logically, any list with one item can be considered to be sorted, right?

Next, the adjacent *length-1* lists are merged into sorted sublists of *length-2*. Then those are merged into lists of *length-4*, and so on until the entire list is assembled in sorted order.

![mergesort img]

There are two approaches to implementing a merge sort. They are referred to as "top-down" (using recursion) and "bottom-up" (using iteration). Both arrive at the same result, and it's useful to have an understanding of both approaches.

####Pseudocode - Bottom Up

* Split the input into "sorted" sublists
[4,7,4,3,9,1,2] -> [[4],[7],[4],[3],[9],[1],[2]]

* Merge the adjacent 1-item lists into sorted 2-item lists 
[[4],[7],[4],[3],[9],[1],[2]] -> [[4,7],[3,4],[1,9],[2]]

* Repeat merge step
[[4,7],[3,4],[1,9],[2]] -> [[3,4,4,7], [1,2,9]]

* Repeat merge step
[[3,4,4,7], [1,2,9]] -> [[1,2,3,4,4,7,9]]

* The completed sort
[1,2,3,4,4,7,9]


####Pseudocode - Top Down

* Split the input array in half
[4, 7, 4, 3, 9, 1, 2] -> [4, 7, 4], [3, 9, 1, 2]

* Both sides are sorted recursively:
[4, 7, 4] -> [4, 4, 7]
[3, 9, 1, 2] -> [1, 2, 3, 9]

* Both halves are merged:
[4, 7, 4], [3, 9, 1, 2] -> [1, 2, 3, 4, 4, 7, 9]

Step 2 may cause some confusion, but it's straightforward when you think about what's actually happening. When we say 'both sides are sorted recursively', what we actually mean is that each list is passed as an argumant into another recursive call to `mergesort`. And what happens as a result? Eventually the list is 'sorted' into a series of 1-item lists. From that point, the halves are successively merged just as in the 'bottom-up' version.

<hr>

####[Quick Sort]
The quick sort algorithm uses the 'divide and conquer' strategy.

![quicksort img]

####Pseudocode

* Pick a 'pivot point'. Picking a good pivot point can greatly affect the running time.
* Break the list into two lists: 
  * One with elements less than the pivot element, 
  * One with elements greater than the pivot element.
* Recursively sort each of the smaller lists.
* Make one big list: the 'smallers' list, the pivot points, and the 'biggers' list.

<hr>

##Additional Resources
Just can't get enough of algorithms? Check out the following list!

[The Runestone] - a fantastic resource on Python algorithms and data structures!

[Sorting Algorithm Animations] - super cool visualizations of how algorithms work.

[Python and Algorithms] - fascinating and easy to read with lots of code samples.

[Big-O Cheatsheet] - excellent reference to algorithmic time complexity.

[Algorithmic Patterns]

[Dictionary of Algorithms and Data Structures]

[Recursion]

[Permutation]

[Software Design Patterns]

[The Algorithmist]






[Algorithm]: http://en.wikipedia.org/wiki/Algorithm

[Heuristic]: http://en.wikipedia.org/wiki/Heuristic

[Brute-force]: http://en.wikipedia.org/wiki/Brute-force_search

[Tree Traversal]: http://en.wikipedia.org/wiki/Tree_traversal

[Divide and Conquer]: http://en.wikipedia.org/wiki/Divide_and_conquer_algorithms

[Randomized Algorithms]: http://en.wikipedia.org/wiki/Randomized_algorithm

[Monte Carlo Algorithms]: http://en.wikipedia.org/wiki/Monte_Carlo_algorithm

[Las Vegas Algorithms]: http://en.wikipedia.org/wiki/Las_Vegas_algorithm

[Reduction of Complexity]: http://en.wikipedia.org/wiki/Reduction_(complexity)

[Selection Algorithm]: http://en.wikipedia.org/wiki/Selection_algorithm

[Sorting Algorithm]: http://en.wikipedia.org/wiki/Sorting_algorithm

[Bubble Sort]: http://en.wikipedia.org/wiki/Bubble_sort

[Insertion Sort]: http://en.wikipedia.org/wiki/Insertion_sort

[Merge Sort]: http://en.wikipedia.org/wiki/Merge_sort

[Quick Sort]: http://en.wikipedia.org/wiki/Quicksort





[The Runestone]: http://interactivepython.org/runestone/static/pythonds/index.html

[The Algorithmist - Sorting]: http://www.algorithmist.com/index.php/Sorting

[The Algorithmist]: http://www.algorithmist.com/index.php/Main_Page

[Permutation]: http://en.wikipedia.org/wiki/Permutation

[Software Design Patterns]: http://en.wikipedia.org/wiki/Software_design_pattern

[Algorithmic Patterns]: http://cs.lmu.edu/~ray/notes/algpatterns/

[Dictionary of Algorithms and Data Structures]: http://xlinux.nist.gov/dads//

[Sorting Algorithm Animations]: http://www.sorting-algorithms.com/

[Recursion]: http://en.wikipedia.org/wiki/Recursion

[Python and Algorithms]: http://www.astro.sunysb.edu/steinkirch/reviews/algorithms_in_python.pdf

[Big-O Cheatsheet]: http://bigocheatsheet.com/

[time complexity]: http://bigocheatsheet.com/

[space complexity]: http://www.leda-tutorial.org/en/official/ch02s02s03.html

[Intro to Sorting Algorithms]: http://community.topcoder.com/tc?module=Static&d1=tutorials&d2=sorting


[bubblesort img]: img/Bubble-sort-example-300px.gif

[insertionsort img]: img/Insertion-sort-example-300px.gif

[mergesort img]: img/Merge-sort-example-300px.gif

[quicksort img]: img/Quicksort-example.gif
