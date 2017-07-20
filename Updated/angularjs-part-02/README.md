# AngularJS Part 2

Welcome to AngularJS Part 2.  During this sprint, you will be learning how to build apps that interact with RESTful services.

### Getting Started

Fork/Pull code

Open console, navigate to repo

run `python -m SimpleHTTPServer 9000`

Open your browser to http://localhost:9000

Start editing files!

***

## Lecture

**We’ve seen what AngularJS can do, now let’s take it to the next level.**
* What we are ultimately trying to do is create a web frontend that can "talk" with a web backend.  What does that mean?
* So we want to be using a combination of HTTP methods and data to express interaction between the frontend and the backend.
* HTTP methods are high level verbs.
    * We can GET data from a server.
    * We can POST new records to it.
    * We can PUT a new record in a specified location on the server. (Replaces existing record. Describes an entire record.)
    * We can PATCH an existing record with only the changes we want to make.
    * Or we can DELETE a record from the server.
* The location we reference is an API endpoint.  It can target specific objects (nouns) in the system in order to act on them
* So, combining an HTTP verb with a noun specified by an API endpoint (and any relevant data) results in interaction between the frontend and the backend.
* We’re going to explore some more advanced AngularJS modules and concept that are built to support this type of interaction.

**Checkpoint** - Discussion.
* How would I retrieve a list of todo items?
* How would I change the title of one todo item?
* What are two different ways we can add items to the todo list?
* Any further questions?

**Checkpoint** - Interacting with servers.
* Let’s talk about a topic in preparation for interacting with servers.
* Can anyone tell me how you might handle an AJAX requests?
* How do we handle asynchronous tasks like what we need to do when the server responds? Callbacks.
* What’s the problem with callbacks?  Callback hell.
* What’s the alternative?  Promises.
* On its face, promises look awfully similar to callbacks, but they are specified through APIs.
* This is important, because most of the AngularJS APIs rely on promises to deliver results for asynchronous tasks.  This is delivered through the $q service, which is in turn based on [Kris Kowal’s q library](https://github.com/kriskowal/q).
* Promises are different from callbacks because they don’t rely on on the code that performs the task to follow up afterwards and finish what we started.  When the task is done, anything else that needs to happen must be done by the code executing the async task.  The task itself and the follow-up are "tightly" coupled.
* This is bad because we essentially "deliver a note" and hope that the other party follows the instructions on the note correctly.  With promises, we essentially give the other party our phone number to txt us at and tell us they are done.  This makes promises “loosely” coupled with the asynchronous task being performed.
* Here’s the great thing about promises.  Let’s pretend you can give other people that phone number, and they can see texts to the number as well.  Now, if someone else is interested in knowing when the async task is done, I can say it’s in the works now, but use this phone number to get notice when it’s done.  Then they wait to do their thing.
* If we simply pass a note, nothing can change, and no other parties can be added.
* This is a more advanced concept.  Don’t worry about understanding it in its entirety, but know that they are different from callback functions you might be familiar with.

**Checkpoint** - Promises in AngularJS.
* Many times, the promises as passed back by default from other services.
* Promise APIs have one hard requirement.  They must be "thenable."
* Let’s pretend we have a promise variable.  The to respond to its result, we must do the following.
    * promise.then(function(animal){ alert(animal); })
    * The first argument of the then method on the promise API specifies the success handler.  It assumes that the code performing the task will return data as an argument, which we have named animal.
    * To add an error handler, add a second anonymous function using the catch API method.
    * promise.catch(function(){ alert("We have a problem!") });
* We can create our own promises using the $q service.  We won’t dive into that right now though.
* Protip: Anonymous functions are easy to use as arguments for a function, but can be tricky to debug.  Consider passing named function references instead of anonymous functions.
* Protip: Promises offer a lot more functionality and allow you to handle asynchronous tasks in a myriad of ways depending on your project’s requirements.  When you have many success handlers chained together, the first one could return a value, which will be passed on to other success handlers.  Or it could return a new promise, which must be first resolved before proceeding to the next success handler.

**Exercise Set A - Promises**

1. **(Essential)** Use the fakeTask function in the Tools service to create a promise.  An alert window will appear when the task is complete.  You can use [the following blog post](http://www.tivix.com/blog/keeping-promises-with-angularjs/) as a reference for how the promise API works, and how they can handle asynchronous tasks.
2. **(Essential)** Using the previous promise, add an argument to the anonymous function that handles the success case.  Display the data on the page.
3. Use the randomResult function in the Tools service to create a promise.  Create both success and error cases for this promise.  The result will randomly be successful or fail.
4. Bonus: Create three promises with fakeTask, in succession of one another.  When one completes successfully, create the next one.
5. Bonus: What happens when you add new handlers to a promise that’s already been completed?
6. Bonus: Create three promises at the same time using the randomInterval function in the Tools service.  These promises will be completed at a random point in time.  Inject the $q service into your controller, and utilize $q.all to create a new promise that finishes when all three of the earlier promises are completed.

**Checkpoint** - The $HTTP service.
* Next, let’s talk about the $HTTP service.
* This is an example of a service that you’ll need to inject into your controllers or other services.
* To make a GET request to a server for a resource, it’s no more complicated than this.
    * $http.get("path/to/API")
    * What’s the problem with this approach? Nothing happens with the request.
    * It still makes the request, but AngularJS doesn’t have an action to perform afterwards.  Let’s iterate.
* Let’s react to the request.
    * $http.get("path/to/API").success(function(data){ console.log(data); })
    * Now we can access the result.  The get function returns a promise that we can act on by calling the success API and providing an anonymous function to execute when the task finishes.
    * NOTE: Does everyone understand what an anonymous function is?
    * Note here, there we could chain multiple success handlers to the promise without initiated a new request.  We could also store the promise in another variable.
    * But what’s the problem now?  We are only accounting for a successful result.  What about error cases?
* Let’s handle both cases.
    * var request = $http.get("path/to/API");
    * request.success(function(data){ console.log("We did it!", data); });
    * request.error(function(data){ console.log("Looks like we have a problem.", data); })
* A quick note: You’ll see that the anonymous function accepts one argument when it’s called.  This is used by AngularJS to deliver the content as a JS object.
* These anonymous functions can also accept arguments for status, headers, and config.  You don’t need to worry about them just yet, but feel free to take a peek if you’re curious.
* Congratulations, you’ve performed your first GET request to the server!

**Checkpoint** - $HTTP Continued.
* Now, let’s look at how we can post data to the server.
* At the most basic level, we can do this:
    * $http.post("path/to/API")
    * But we know we aren’t responding to the result.
    * We also have another problem.  What is it? We’re not actually posting anything.
* Let’s try again.
    * $http.post("path/to/API", {‘animal’: ‘dog})
    * Even if we aren’t responding to the result of this POST, we are still POSTing a new record to the server. Which, if everything goes well, will be recorded.
    * We just need to pass a JS object with key-value pairs. Then AngularJS will translate this into the correct HTTP request format for delivery.
* I’ll let you try adding success and error cases to the result of the promise.

**Exercise Set B - $HTTP**

1. **(Essential)** Load the file JSON/animals.json using the [$HTTP service](https://code.angularjs.org/1.3.11/docs/api/ng/service/$http).  Dump the data to your console.
2. **(Essential)** List all of the animals on the page.
3. Use a service to store the results from the request.
4. Use this service to make the $HTTP request, or return the stored results.
5. Change the request URL to an invalid address.  Add an error handler to your code.
6. Bonus: Add a loading indicator to the page.  Use Tools.randomInterval to simulate a long running request for a server resource and display the loading indicator after the you first call the function, and remove the indicator once the promise has been completed.
7. Bonus: What happens if two controllers on the same page need to access the same data over HTTP?  While we can cache data in a service for use in later requests, how can we eliminate duplicate requests for controllers that are loaded simultaneously.  Remember! Promises can be passed around in code so that multiple parties can handle the results of one task.  How could you share a promise between two controllers?  Would services be useful in accomplishing this?

**Checkpoint** - Preparing data by using forms.
* HTML forms are the most common route to providing interactions between the frontend and backend.
* Forms are explicit and easy to understand.  Other behaviors will be tied to more implicit behaviors - say, clicking a button.  These will also trigger interactions with the backend, but let’s stick with forms for the time being.
* Something special happens when you use a form in an AngularJS view.  Once it is named, Angular adds a special object to the scope that handles that form.
* ```<form name="myForm”>``` results in a new piece of scope data for the controller.  It can be referenced from $scope.myForm now.
* There are many pieces of information we can use here, but let’s focus on two of them.
    * $valid, $invalid are provided to give you insight into whether the form is valid and ready to be submitted.  TheseInfo are read only properties that can only be changed by AngularJS.  They will simply be true or false.
    * Information about form fields are also accessible through this object.  Simply refer to them as $scope.myForm.myField.  These fields also have $valid, $invalid flags, as well as an errors API, which we will cover shortly.

**Exercise Set C - Form Validation**

1. **(Essential)** Create a [form](https://code.angularjs.org/1.3.11/docs/api/ng/directive/form) with a [text field](https://code.angularjs.org/1.3.11/docs/api/ng/directive/input), a [select field](https://code.angularjs.org/1.3.11/docs/api/ng/directive/select), and a [checkbox field](https://code.angularjs.org/1.3.11/docs/api/ng/input/input%5Bcheckbox%5D).  Name the form myForm.
2. **(Essential)** AngularJS also provides support for HTML5 field type validation.  Try setting up an [email](https://code.angularjs.org/1.3.11/docs/api/ng/input/input%5Bemail%5D) field, URL field, or [number field](https://code.angularjs.org/1.3.11/docs/api/ng/input/input%5Bnumber%5D).
3. **(Essential)** Add the validation status of the form to the page.
4. **(Essential)** Set the text, select, and checkbox fields to be required and add test values to see when the validation status changes.
5. **(Essential)** Add the validation status of each field next to each field.
6. Add a ng-minlength field requirement to the text field.  Set it to 5.  Only values with five or more characters will be considered valid.
7. Display a list of $error flags that have been set to true for each field.  Display it following the field.
8. Try entering a non-valid values to the email, URL, or number field you created.  What type of validation error message appears?
9. **(Essential)** Add a submit button which is disabled if the form is not valid.
10. **(Essential)** Include an [ng-submit event](https://code.angularjs.org/1.3.11/docs/api/ng/directive/ngSubmit) in the form tag.  Print the value of the fields to the console.
11. Bonus: Store all field values as part of one object using dot notation.

**Checkpoint** - AngularJS forms API continued.
* Even if you’re not using these APIs right away, it is important to be familiar with these APIs so that you do not try to reinvent the wheel.
* AngularJS is valuable in how many APIs and tools it provides.  This can be overwhelming, but just understand that these are tools you can use as you need them.
* Getting back to the forms API...
* Each field has a list of errors, named $error.  This list is an assort of key-value pairs.
* The key represents the name of a potential error. For instance, required.
* The value represents whether or not that error is present in the field.  So if a field that’s required, and it has no value, then the "required" key will return false for $scope.myForm.myField.required.
* How do we determine which fields are required though?
* Recall directives.  Who can tell me what a directive is?
* So AngularJS will look for the require attribute in a form field to understand when it must have a value.
    * ```<input type="text” name=”myField” required>```
* Other examples of validation directives include minlength, maxlength, and pattern.
* AngularJS also provides support for validating HTML5 fields, by default.  For instance, you can specify the input type to be "email" and AngularJS will only consider the field valid if the value matches an email address pattern.  No further directives are required.
* These will not prevent you from submitting a form by default.  Try using $invalid with the disabled directive on a form button.

**Review Demo Content in Repo**
* You’ll find that the new repository is very similar to the one from the previous sprint.
* However, the tools service has been fleshed out with additional functionality you’ll need for the assignments.
* Let’s quickly look at the new index.html
* Here, you’ll find two controllers operating on the page.
* The first will be responsible for retrieving a list of 10 Tivix repositories on Github.  With this controller, you’ll find an example of how to perform a GET request, limit the results, and use details from a richer set of results, rather than just a list.
* The second controller demonstrates some simple promise and forms techniques.
* The first portion will query the Tools service for the value of 6 times 5.  We know we can solve this with javascript, but here we want to simulate an asynchronous task occurring.
* The second portion demonstrates how to make a radio button field required, and report on it’s validation status.

**Checkpoint** - Wrapping up.
* Final Questions?
* The lecture notes will be available for your reference while working on exercises.  A separate document outlining your exercises and lab for the spring have also been posted.
* Please make use of the links to AngularJS documentation.  I’ve given you a high level overview of what AngularJS has to offer, but you’ll only benefit from digging into the docs and unlocking more of it’s functionality yourself.
* Best of luck!

***

# Labs (Please select one, the other will be bonus points)

## Part 2 Lab A - Live Todo List

Your assignment is to extend your single page app for Todo lists to interface with your Django Rest Framework project.  [Please follow these instructions](https://github.com/rocketu/django-rest-framework/blob/ba45db70e5fdad96e92644a3e7585b7764397f8b/README.md#django-cors-headers-package-setup) from the Django Rest Framework Repo to setup CORs.

1. **(Essential)** Load todo items from the server.
2. **(Essential)** Save todo items to the server.
3. Delete todo items from lists.

## Part 2 Lab B - [Github API](https://developer.github.com/v3/)

Authenticating to Github: When you are ready to start making calls to the Github API, use the Tools.authGithub function to authenticate you with the API.  This will pre-authenticate you with a dummy account for this sprint.

1. **(Essential)** Retrieve a list of Twitter Bootstrap Repositories.
    1. Use the following API URL: [https://api.github.com/orgs/twbs/repos](https://api.github.com/orgs/twbs/repos)
2. **(Essential)** List these repositories by name.
3. Sort the repositories by name.
4. **(Essential)** List repositories and the number of stars each one has.
5. Sort the list of repositories by number of stars.
6. **(Essential)** Create a route that displays the details of a repo.  The route should accept a parameter called name.  Use name to retrieve the individual repo record from github.
    2. Use the following API URL: [https://api.github.com/repos/twbs/](https://api.github.com/repos/twbs/gruntworker)[name]
7. Only load the list of Bootstrap repos if they have not been already.  Store the data in a service.

**For additional references**, check out the following sites:
* https://code.angularjs.org/1.3.11/docs/guide
* https://code.angularjs.org/1.3.11/docs/api
* https://egghead.io/technologies/angularjs?order=ASC
