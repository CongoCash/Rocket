#Introduction to jQuery
You've worked a little bit with the native DOM API by now, and have seen how it's possible to access elements programatically using JavaScript. It works great, and with modern browsers the DOM API is actually well implemented and reasonably consistent. But it was not always so.

Up until quite recently, major web browsers like Chrome, Firefox and most notably Internet Explorer varied widely in their support of the native DOM API. Actually, until the HTML5 specification began gaining traction, many of the current methods did not even exist in *any* of the browsers. This created problems for software engineers who wanted to push the boundaries of what was currently possible and create more robust, interactive web applications. In order to insure that their code would run on many diferent browser types, huge amounts of additional code had to be written, tested and maintained to implement the various browser possibilities. This was a huge problem.

Open source JavaScript libraries were the answer. By leveraging JavaScript as a functional programming language, engineers were able to write __libraries__ of code that extended and normalized the functionality of web browsers. These libraries could be easily written in JavaScript and included in an HTML page simply by adding a `<script>` tag.

jQuery was, and continues to be one of the most effective and widely used JavaScript libraries in the world. It's primary benefit is to __normalize__ the DOM methods so that the same script will run equally well on any supported browser. The code is also reasonably intuitive, so anyone familiar with JavaScript and CSS can easily pick it up.

Why is CSS important to jQuery? The selector methodology used for CSS was designed specifically to target DOM elements for styling, and it has a robust selection set that allows the developer to make complex selections easily. This is exactly what is needed by JavaScript to interact with the DOM. By using the existing CSS 'hooks' the designers of jQuery gave developers the access they needed without reinventing the wheel. Pretty clever.

Under the hood, jQuery is doing some pretty complex work. Anyone looking for a better understanding can easily read through the code. It's available for download in both verbose/commented and minified/production formats.

###Modifying the DOM with jQuery
There is no need to reinvent the wheel, as the native jQuery documentation is very good, and easy to understand. The jQuery Learning site is [here](http://learn.jquery.com/).

If you can't stand it and want to start coding, at least read through these sections:

* [$(document).ready](http://learn.jquery.com/using-jquery-core/document-ready/)
* [Selecting Elements](http://learn.jquery.com/using-jquery-core/selecting-elements/)
* [Event Basics](http://learn.jquery.com/events/event-basics/)


##Your Mission

Refactor your Tic-Tac-Toe game from the last sprint into jQuery code. Try to refactor your logic to improve the code based on what you learned from the class presentations.
<hr>

##[What is AJAX?](http://en.wikipedia.org/wiki/Ajax_%28programming%29)

One of jQuery’s great features is it’s abstraction of AJAX, an acronym for Asynchronous JavaScript. AJAX is a term that describes loading data dynamically without loading a new page. The browser sends a request in the background and, upon success or error, a callback is triggered and then the data can be displayed or used. While AJAX stands for Asynchronous Javascript And XML, the term AJAX now tends to cover all dynamically loaded content, whether it’s XML, HTML, JSON or even JavaScript. Requests are made using the [XMLHttpRequest API](http://en.wikipedia.org/wiki/XMLHttpRequest)

The key to AJAX’s concept is “asynchronous”. This means something happens to the page after it’s loaded. Traditionally, when a page is loaded, the content remains the same until the user leaves the page. With AJAX, JavaScript grabs new content from the server and makes changes to the current page. This all happens within the lifetime of the page, no refresh or redirection is needed.

###How AJAX works
Take a look at this file:

[Shopping Cart Sample](shopping_cart/index.html)

As you can see, clicking on the item adds it to the cart without refreshing the page.

####Different ways to make JQuery AJAX calls
###[$.click()](http://api.jquery.com/click/)
Before we go over the different ways to make an AJAX call, let’s see how `$.click();` works.

Place the code below in click.html to see how it works.

```
$("#click_test").click(function(){});
```

Currently the function is empty. Even though the __Click test__ button is clickable, nothing will happen if you click.

Now let's fill out our function. Place the code below in `click.html` and see what’s happening!

```
$("#click_test").click(function(){
    alert("Your $.click triggered an alert event!");
})
```
When the __Click test__ button is clicked you will see an alerted message.

####TODO : Add the click functionality as indicated in the `click.html` file.
___Reference this page -___ `exercises/click_exercise/click.html`

<hr>

###1. [$.load()](http://api.jquery.com/load/) : Load HTML From a Remote URL and Inject it into the DOM

```
var loadUrl = "TestPage.html";

$(document).ready(function () {
    $("#load_basic").click(function () {
        $("#result").html(ajax_load).load(loadUrl);
    }
}
```
As you can see in the above code, you can easily make a call to any page by passing it a Url. One of the important things about the load method is that it allows you to load part of the page rather than the whole page. So, the invocation of the AJAX function remains the same, with the exception of the URL, which can be modified by assigning a new variable or even by using string concatenation to build up a url from, for example, data from the event object and a file extension.:

```
$("#load_basic").click(function (evt) {
    $("#result").html(ajax_load).load(evt. *SOMETHING ELSE GOES HERE* + '.txt');
}
```

Be aware that the argument to the `.html()` function needs to correspond to the target in the HTML. 

Tip: The callback function provides more control and allows handling of errors by making use of the Status value.

```
var loadUrl = "TestPage.html";
$(document).ready(function () {
    $("#load_basic").click(function () {
        $("#result").html(ajax_load).load(loadUrl, function (response, status, xhr) {
            if (status == "error") {
                var msg = "Sorry but there was an error: ";
                $("#dvError").html(msg + xhr.status + " " + xhr.statusText);
            }
        });
    });
}
```

####TODO : Complete the load_exercise

___Reference this page -___ `exercises/load_exercise/index.html`

####Pro Tip:
Getting 'Cross-Origin' errors? This protocol is built into your prowser to prevent nasty cross-site scripting attacks. Check out this excellent blog post on [CORS](http://www.html5rocks.com/en/tutorials/cors/).

When using AJAX to get files from your local machine you will need to run a server. The simplest way to go is the the [Python SimpleHTTPServer](http://www.pythonforbeginners.com/modules-in-python/how-to-use-simplehttpserver/). 
  * From the command line, navigate into the directory containing your `index.html` file.
  * Enter this line: `python -m SimpleHTTPServer`
  * Open your web browser and navigate to 127.0.0.1:8000.
  * You are now viewing the file delivered through the Python server. If you take a look at the terminal, you will see a log of all server traffic. Pretty cool!
  * To stop the server, enter Ctrl-C at the command line.
    * If you get an error when restarting the server, you probably still have an instance running. You can either open a new terminal (a pain) or use the strategy outlines in this [StackOverflow](http://stackoverflow.com/questions/19071512/socket-error-errno-48-address-already-in-use) post to identify and kill the process.

<hr>
###2. [$.getJson()](http://api.jquery.com/jQuery.getJSON/) : Retrieve JSON from a Remote Location

___Reference this page -___ `exercises/getJson_exercise/getJson.html`

This getJson method allows you to get JSON data by making an AJAX call to the server. The getJson method only allows you to pass parameters using the GET method. Using the POST method with a parameter is not allowed. One more thing - this method treats the response as JSON.

```
var jsonUrl = "Json.html";

$("#btnJson").click(function () {
    $("#dvJson").html(ajax_load);
    $.getJSON(jsonUrl, function (json) {
        var result = json.name;
        $("#dvJson").html(result);
    });
});
```

The above code makes use of the getJSON method and displays the JSON data fetched from the server on the page. The following is some JSON data returned by the Json.html file:


```
{
    "name": "Hemang Vyas",
    "age" : "32",
    "sex": "Male"
}
```

####TODO : Complete the getJson_exercise outlined in the `getJson.html` file.
<hr>
###3. [$.get();](http://api.jquery.com/get/)

___Reference this page -___ `exercises/post_get/post_get.html`

This method allows you to make AJAX requests with the GET method. It handles the responses in many formats including xml, html, text, script, json, and jonsp.

```
var getUrl = "GETAndPostRequest.aspx";

$("#btnGet").click(function () {
    $("#dvGet").html(ajax_load);

    $.get(getUrl, { Name: "Pranay" }, function (result) {
        $("#dvGet").html(result);
    });
});
```

<hr>
###4. [$.post();](http://api.jquery.com/jQuery.post/)

___Reference this page -___ `exercises/post_get/post_get.html`

This method allows you to make AJAX requests with the POST method. It handles the responses in many formats including xml, html, text, script, json, and jonsp. $.post does the same as $.get but just sends data using a POST method.
###What's the difference between [GET and POST?](http://java67.blogspot.com/2014/08/difference-between-post-and-get-request.html)

```
var postUrl = "GETAndPostRequest.aspx";

$("#btnPost").click(function () {
    $("#dvPost").html(ajax_load);

    $.post(postUrl, { Name: "Hanika" }, function (result) {
        $("#dvPost").html(result);
    });
});
```

####TODO : Complete the post_get_exercises
<hr>
###5. [$.ajax();](http://api.jquery.com/jQuery.ajax/)

___Reference this page -___ `jQuery_ajax.html`

This method allows you to make an AJAX call. This method provides more control than all other methods we have seen. You can figure out the difference by checking the list of parameters.

```
var ajaxUrl = "Json.html";

$("#btnAjax").click(function () {
    $("#dvAjax").html(ajax_load);
    $.ajax({
        type: "GET",
        url: ajaxUrl,                 // Location of the service
        data: "",                     //Data sent to server
        contentType: "",              // Content type sent to server
        dataType: "json",             //Expected data format from server
        processdata: true,            //True or False
        success: function (json) {    //On Successful service call
            var result = json.name;
            $("#dvAjax").html(result);
        },
        error: ServiceFailed          // When Service call fails
    });
});
```

In the above code, you can see all the parameters and comments related to each parameter and a description of the purpose of each one.

####TODO : Complete the ajax_exercise
<hr>
###Extra credit
Under exercises, there is a folder called gallery. The gallery folder contains two different directories. One called `withAjax` and the other called `withoutAjax`.

The `withoutAjax` folder examplifies the code that you have to write in order to duplicate the functionality in the `withAjax` folder. Modify the `withAjax` folder to make the execution of the file present a new picture when you click the link without refreshing the entire page.


##Double Kick-Butt Extra Credit

###Option 1 - Code Refactor
Open the `shopping_cart` directory and navigate to the `cart.js` file. There are a couple of functions that call a `livequery` method. This actually requires the addition of another external script, which you will see linked at the top of the HTML page. 

While functional, this represents an example of legacy code that is no longer needed for modern browsers. Additionally, if you analyze the code you will see that there are a lot of repeated calls to the DOM for information that would be better stored in a data model (of your design) in the JavaScript.

Refactor this code to remove this tight-coupling, and move as much of the data out of the DOM and into the code as you can. 

###Option 2 - Tic-Tac-Toe Effects
Add some [jQuery Animation and Effects](http://api.jquery.com/category/effects/) to your game
In addition to great selectors and AJAX, jQuery offers some great convenience methods to help you add cool effects with ease. Check out this page and play with some options. See what you can create to make your UI more engaging. For even more involved effects, take a look at [jQuery UI](http://jqueryui.com/). This is an additional library, so you will need to download the file and link to the local copy, or link to the [CDN](http://en.wikipedia.org/wiki/Content_delivery_network). 

###D3

jQuery isn't the only open-source JavaScript library available to you. There are many others that add incredible functionality just by adding a `script` tag. D3 is a graphics library that allows developers to create complex visualizations of large data sets. The growth of 'big data' is one of the leading industry trends, and the ability to create understandable visual representations of large data sets is key.

The D3 has a unique approach of taking data and combining it with the DOM to create a group of 'data-DOM' pairs. This allows the dataset to dynamically drive quantity, scaling and a host of functions that combine to create some fantastic looking charts. D3's website is here:

##Maximum Awesome Extra Credit

####[D3](http://d3js.org/)

Download the library, or add the CDN link to yout HTML file and get started. There are some fantastic tutorials to get you started [here](https://github.com/mbostock/d3/wiki/Tutorials).

Need some data? Check out [Kaggle](http://www.kaggle.com/competitions). Click on an interesting topic, and then click 'get the data'. Make something awesome!