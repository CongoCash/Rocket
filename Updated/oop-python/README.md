Object Oriented (OO) Python Fundamentals, Inheritance & Methods
================

###Functional Programming Vs. Object Oriented Programming
So far, all the programming you have done is functional. You've been writing functions to solve very specific problems. In functional programming, your code is organized around actions and the logic to handle them. In OO programming, you organize your code around types of objects, including their state and available behavior.

Python is an object-oriented language. Other examples of OO programming languages include: Java, Perl, Ruby, PHP, Objective-C, etc. The differences between OO and functional programming probably won't be immediately obvious to you, but will start to make sense after you have been programming for awhile.

<hr>

###What Are Objects?
To discuss OO programming, we should explain some of the key terminology.

Objects are representations of ‘things’.

A [class] is a blueprint or prototype from which objects are created

In the real world, you'll often find many individual objects all of the same kind. For example, there may be thousands of bicycles in existence, all of the same make and model. Each bicycle was built from the same set of blueprints and therefore contains the same components. In object-oriented terms, we say that your bicycle is an instance of the class of objects known as bicycles. A class is the blueprint from which individual objects are created.


##Your Mission Part I
Read the comments found in py/car.py line by line. Instantiate each class and access each attribute of the class. Once that has been completed write your own class in py/bicycle.py using an <code>`__init__()`</code> method. Give your bicycle some accessories! What data structure(s) will allow you to include some accessories with your bicycles? You should be able to add and remove bicycle accessories. Then, go on a bike ride! Already done? Want to dig a little deeper?
* Check out CodeCademy's Intro to Classes: [class basics] & [member variables and functions]
* Take a look at [Python the Hard Way], exercises 40-42
* Read the official documentation on [python classes]
* Python in one page: [Learnxinyminutes: Python]

Once you are done with this exercise, move onto the blog directory. Once again, run through the code line by line and understand what is happening within the code. The code is broken up into 3 main files - main.py, blog_post.py, and author.py. Run the code in your terminal with well placed print statements.

After you are done with this, create a command line tool for a building manager. The building manager needs to be able to add new buildings, apartment units, and renters. All apartment units must be in an associated building. Buildings should have some basic information associated, like their address, if they have a doorman, the number of floors, etc. Apartments should have a unit number, rent, square footage, number of bedrooms, etc. You should also have basic information about your renters.

You should also have a way of identifying if the apartment is occupied. If it is, you shouldn't be able to add a new renter to the unit.

Work in the <code>building-manager/</code> directory.

Bonus: When talking about apartments in a building, you should be able to refer to them and get their attributes using the specific apartment name. <strong>Hint</strong>: what data structure will allow this?

<hr>

#Inheritance

Previously we used an example of a Car class. But what about other types of vehicles?

* Stick shifts are still cars, but there are a few differences. Acceleration is limited by your current gear. Braking might stall the car.
* Boats are vehicles, they can accelerate, but not brake.
* Tanks can accelerate, brake, turn left and right, have a color. But they can also blow stuff up!

Clearly there are a lot of similarities between different vehicle types, but also a number of variances in terms of properties and functionality. Object oriented Python uses inheritance as a way to de-duplicate this common functionality.

* Common features are abstracted into base classes (also known as super classes)
* Derived classes (sub classes) inherit features from one or more base classes
* Additional features can then be added, or existing ones changed in the derived class
* Objects can be instantiated on a base class or a derived class
* Inheritance chains can be any length in Python

#### Inheritance: Base classes and Subclasses

![inheritance visual]

##### Simple Inheritance Example
Let's revisit our car example and think of it as a Vehicle instead. To make a class that is a subclass of another, use the <code>class Subclass(ParentClass)</code> notation to reference the parent class in the definition.

A subclass has all of the same methods and attributes as its parent classes unless you specify otherwise. For our ManualTrans objects, we are adding the <code>clutch_in</code> as an attribute and <code>engage_clutch()</code> and <code>disengage_clutch()</code> as methods. We'll overwrite <code>`__init__`()</code> to set the attr and <code>brake()</code> to call our methods.

In Python, <code>super()</code> is a method that says 'do everything in the parent class version of this method'. Essentially when you're overwriting a method, it allows you to preserve all of the existing functionality, and add more on top.

#### Multiple Inheritance and Mixins
What happens if some of our Vehicles share the same functionality, but some don't? For example, what if we wanted to add windshield wipers to some of our vehicles? Python allows for objects to inherit from multiple classes. This is often called a Mixin, which allows us to share functionality between two classes

This also allows us to write DRY (Don't Repeat Yourself) code and not duplicate our wiper code in two places.

#### Mixin Visual
![mixin visual]

#### Creating a Mixin
You'll find that a mixin is created for you in py/car.py called <code>CarMixin</code>. This is a new object which contains the common wiper code. Another class, called <code>ManualCar</code> has also been created which will inheret from our <code>ManualTrans</code> class. The class <code>RaceCar</code> will inheret from the <code>ManualCar</code> and <code>CarMixin</code>. What this means is that when we create a new instance of <code>RaceCar</code>, we can now call <code>CarMixin</code>'s methods as well as <code>ManualTrans</code>'s.


##Your Mission Part II
Add ManualCar and Motorbike classes that subclass ManualTrans.
* Overwrite some methods without using <code>super</code> and see what happens.
* Overwrite <code>`__init__`()</code> or <code>brake()</code> using <code>super()</code>. Does this reference to ManualTrans or Vehicle?
* Add some differentiating functionality between ManualCar and Motorbike. Take them for a ride!
* Create classes for the rest of the objects in the <em>Mixin Visual</em>. Pay attention to which classes they inheret from.
* Add print statements to the various methods so our output can inform us that the car is breaking or the boat has accelerated.
* Have your program create 1 instance of each of the following: RaceCar, StreetCar, Motorbike, AutoCar, Boat.
* Have your program drive and control each of the classes by calling the various methods. When you run it, there should be output describing what is happening.

Bonus: Add a <code>RadioMixin</code> to some of your classes, which can turn the radio on and off as well as change the station.

Need more?
* Work through CodeCademy's Introduction to Classes: [inheritance]
* Take a look at [Python the Hard Way], exercises 43-44

<hr>

#Methods

### Review Time: What is <code>self</code>?
What is self? Let's look at our Vehicle class again.

* Notice that every method's first argument is <code>self</code>.

* Also notice that when calling these methods, you never have to pass in anything for <code>self</code>. Self always refers to the
instance of the object you're running the function on. This is why they're called instance methods.

All of the Vehicle functions deal with modifying the instance of the object in some way.

### Static Methods
What if we want to write a function that doesn't necessarily need the instance of the object, but is related to that object? The answer
is to write a static method. Notice the <code>@staticmethod</code> in <code>vehicle_static_method.py</code> on the <code>random_car_color()</code> method. This staticmethod gives us a random color for a car but does not need an actual car instance to do this. This function logically belongs with the <code>Vehicle</code> class, so this allows us to keep our code organized. To use it, we just need to specify the class <code>Vehicle</code> instead of a <code>Vehicle()</code> instance.


### Class Methods
What if we want to write a function that doesn't necessarily need the instance of the object but is related to the specific class? To write a class method, we use the decorator over the method. This is implemented in <code>vehicle_class_method.py</code>. Our example classmethod <code>get_speed_max</code> gives us the max speed of the specific class, but does not need an actual car instance to do this.Notice, that this <code>max_speed</code> is different on our boat class than it is on our <code>Vehicle</code> class. To use it we just need to specify which class we'd like to find the max speed of, and <code>cls</code> in the method will refer appropriately to <code>Vehicle</code> or to <code>Boat</code>.


## Your Mission Part III
Let's continue using our vehicle application and add to it.

* Add a static method on <code>Vehicle</code> which randomly chooses a direction (-180 to 180).
* Add a class method, which returns a new instance of that class, with a random color.
* Add a class method, which takes in another vehicle as an argument, and creates a new instance of the current class, with the passed in vehicle's speed, color, and direction. For example, if I called this method on a RaceCar, and passed it a Boat, it would create a new RaceCar with the Boat's speed, color, and direction
* Have your application now use these new methods to create and "drive" your different types of vehicles.

After you are done with this, create <strong>Blackjack</strong>! You should apply what has previously been mentioned about classes, inheritance and different kinds of methods.

* Create objects to represent the deck, the hand, the game, and the player (along with whatever else you deem appropriate).

#####Some nice to have's:
* Every turn should show all players current hands.
* The player has the ability to enter their name and have it be displayed
* There should be more than one person that can play.
* Players should have the option to 'double down' and play multiple hands for each person if the situation arises

#####Bonus!
* Every player starts out with a given amount of coins to play with and can only play if their coin count is above zero.

###Debugging Cheatsheet
You've already used a couple different debugging techniques. First and foremost, the best way to help yourself debug is to not 'cowboy code'--you should be trying out your code at regular intervals, rather than writing 100 lines and not being sure where your code is broken.

* print statements: very quick and easy, but can be messy
* PyCharm debugging. Other IDEs will also let you set breakpoints, and there are Python modules that will help you do the same. To set breakpoints in PyCharm, you must run your code through PyCharm and not in your normal terminal window.
	* Go to Run / Debug and Edit Configuration
	* Click on the + sign in the upper-left corner to add a new script you want to run
	* Fill in the name, select the source file, and hit OK
	* Click on the left of your code in PyCharm to set breakpoints
	* Run your code in debug mode to step through breakpoints
* Python also has logging built in, which allows you to catch errors, but also warnings and other more granular information


Extra Resources:
* Read through [Classmethods and Staticmethods for Beginners]
* Take a look at [Python Guide to Static, Class, and Abstract Methods]
* More about classes via [Dive Into Python]


[class]: http://docs.oracle.com/javase/tutorial/java/concepts/index.html
[class basics]: http://www.codecademy.com/courses/python-intermediate-en-WL8e4/0/1
[member variables and functions]: http://www.codecademy.com/courses/python-intermediate-en-WL8e4/1/1
[Python the Hard Way]: http://learnpythonthehardway.org/book/
[python classes]: https://docs.python.org/2/tutorial/classes.html
[Learnxinyminutes: Python]: http://learnxinyminutes.com/docs/python/


[inheritance visual]: img/car_inheritance.png
[inheritance]: http://www.codecademy.com/courses/python-intermediate-en-WL8e4/2/1
[Python the Hard Way]: http://learnpythonthehardway.org/
[mixin visual]: img/car_mixin.png

[Classmethods and Staticmethods for Beginners]: http://stackoverflow.com/questions/12179271/python-classmethod-and-staticmethod-for-beginner
[Python Guide to Static, Class, and Abstract Methods]: https://julien.danjou.info/blog/2013/guide-python-static-class-abstract-methods
[Dive Into Python]: http://www.diveintopython.net/object_oriented_framework/index.html



