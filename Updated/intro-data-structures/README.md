Introduction to Data Structures
=====================

Programming languages like __Python__ and __JavaScript__ offer native support for a variety of data types that have rich feature sets right out of the box. It's possible to learn the basics of code without understanding how these underlying data structures work, but in order to become a really solid engineer you will need a little better grasp of what's going on. 

This sprint will give you the opportunity to build several basic data structures from the ground up, and in the process gain a better understanding of what's happening behind the scenes. 

### 1. [Stack]
A stack is one of the most basic data structures in all of computer science. It has the following characteristics:

  * Linear structure
  * Insertion and removal of items occurs at one end of the stack, often referred to as the 'top of the stack'.

![stack img]

You can think of a stack as a physical stack, for example a stack of paper in a printer. To add paper you put the new sheets on the top of the stack. When the printer prints, it takes one sheet at a time from the top of the stack. This is referred to as 'last in - first out' (LIFO).

### 2. [Queue]
A queue is very similar to a stack. The difference is in the way that items are added and removed. A queue has the following characteristics:

  * Linear structure
  * Insertion of items occurs at one end of the queue, and removal at the other. You may sometimes see these actions referred to as 'enqueue' and 'dequeue'.

![queue img]

A good example of a queue is a line at a coffee shop. When a customer arrives at the store, they enter the 'queue' at the end of the line. Customers are served one-at-a-time from the front of the line. This is referred to as 'first in - first out' (FIFO).

##Your First Mission 

In this assignment, you will be working with a partner to implement the following data structures. Follow the directions carefully. You will be working in both Python and JavaScript.

* Python
  * Use the following files for your code:
    * `py/queue.py`
    * `py/stack.py`
* JavaScript
  * Use the following files for your code:
    * `js/queue.js`
    * `js/stack.js`

##Constraints

1. You CANNOT use a `list` (Python) or `array` (JavaScript) data type.
2. You CAN use a `dictionary` (Python) or `object` (JavaScript) with numeric keys.

##Specifications

1. For the queues, write code to implement the following:
  * `enqueue(item)` - adds an item to the end of the queue
  * `dequeue()` - removes an item from the front of the queue
  * `size()` - returns the number of items in the queue

2. For the stacks, write code to implement the following:
  * `push(item)` - adds an item to the top of the stack
  * `pop()` - removes an item from the top of the stack
  * `size()` -  returns the number of items in the stack
<br>

<hr>

##More Data Structures!

The `stack` and the `queue` are two of the most basic data structures. There are lots more! Here are a few examples of data structures that are a little bit more involved. 

As you're working on these, remember that they are all simply different ways to organize data. When developing software, the important thing is to use the data structure best suited to the needs of the project. Think about why you might select one of these structures over another. 

###Follow the instructions below and implement the required methods in both __Python__ and __JavaScript__.

### 1. [Set]

A `set` is a very straightforward data type that corresponds for the most part to the mathematical concept of a *finite set*. In __Python__, a set is represented by the `tuple` data type. There is no direct corollary in __JavaScript's__ native data types.

![set img]

##Mission

Using the `js/set.js` and `py/set.py` files, implement a set with the following:
  * `add(item) - adds the item to the set 
  * `remove(item)` - if the item is contained in the set, removes the item from the set 
  * `contains(item)` - returns a boolean value indicating if the item is included in the set
  * for this exercise, your methods only need to work with strings.
  * remember that sets are unordered and do not contain duplicates
  * For __Python__, do not use the `tuple` data type

<hr>

### 2. [Linked List]

![linkedlist img]

##Mission

Using the `js/linkedlist.js` and `py/linkedlist.py` files, implement a linked list with the following:
  * `.addToTail(item)` - adds an item to the end of the list
  * `.removeHead()` - removes and returns the item at the head of the list
  * `.contains(item)` - returns a boolean value indicating if the item is included in the list
  * for this exercise, your methods only need to work with strings.
  * For __Python__, do not use the `list` data type
  * For JavaScript, do not use the `array` data type

<hr>

### 3. [Tree]

![tree img]

##Mission

Using the `js/tree.js` and `py/tree.py` files, implement a tree with the following:
  * complete the `.children` and `.value` property declarations as necessary.
  * `addChild(item)` - creates a tree node with the passed-in value, and adds that node to the list of children for the parent tree
  * `contains(item)` - returns a boolean indicating if the item exists in the root node or any descendant node

<hr>

##Extra-Credit

As you might have guessed, this has just been the tip of the iceberg for data structures used in software engineering. It's a fascinating subject, and if you're interested in some additional independent study, here are some resources:

[Doubly-Linked-Lists]

[Graphs]

[Bloom Filters]

[Bloom Filter tutorial]

[Binary Search Trees]

[B-trees]

[Red-Black Tree]

[Hash Tables]

[Data Structure Interview Questions]

[Top 10 Algorithms for Interviews]



[Stack]: http://en.wikipedia.org/wiki/Stack_(abstract_data_type)
[Queue]: http://en.wikipedia.org/wiki/Queue_(abstract_data_type)
[stack img]: http://upload.wikimedia.org/wikipedia/commons/thumb/2/29/Data_stack.svg/200px-Data_stack.svg.png
[queue img]: http://upload.wikimedia.org/wikipedia/commons/thumb/5/52/Data_Queue.svg/200px-Data_Queue.svg.png
[Linked List]: https://en.wikipedia.org/wiki/Linked_list
[Tree]: https://en.wikipedia.org/wiki/Tree_(data_structure)
[Set]: https://en.wikipedia.org/wiki/Set_(abstract_data_type)
[linkedlist img]: img/linkedlist.png
[set img]: img/set.png
[tree img]: img/tree.png
[Doubly-Linked-Lists]: http://en.wikipedia.org/wiki/Doubly_linked_list
[Graphs]: http://en.wikipedia.org/wiki/Graph_(mathematics)
[Bloom Filters]: http://en.wikipedia.org/wiki/Bloom_filter
[Bloom Filter tutorial]: http://billmill.org/bloomfilter-tutorial/
[Binary Search Trees]: http://en.wikipedia.org/wiki/Binary_search_tree
[B-trees]: http://en.wikipedia.org/wiki/B-tree
[Red-Black Tree]: http://en.wikipedia.org/wiki/Red%E2%80%93black_tree
[Hash Tables]: https://en.wikipedia.org/wiki/Hash_tables
[Data Structure Interview Questions]: https://www.udemy.com/blog/data-structures-interview-questions/
[Top 10 Algorithms for Interviews]: http://www.programcreek.com/2012/11/top-10-algorithms-for-coding-interview/