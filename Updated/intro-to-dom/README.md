#Basic HTML Review
This repo is designed to give you some repetitive practice with some of the basic techniques for creating content for the web. __Because practice makes permanent! __ We'll start with some basic review of HTML code as used in static content generation, and later we'll move on to using JavaScript to generate more dynamic content.

### Intro to HTML

HTML, or "HyperText Markup Language" is the programming language used to create web pages. It is usually written in some sort of text editor. The resulting text and layout can be viewed with a web browser. The most popular browsers are: Chrome, Firefox, Safari, or Internet Explorer.

HTML consists of 'elements', such as 'tags'. The tags are written within ````<angle brackets>````.

Most commonly, the tags come in pairs. The opening tag will be written such as 

```` <h1> ````
which designates a Heading. The '1' means it is a heading of the 1st largest size.

The closing tag will be written with a slash inside the beginning, to represent the closing of that tag.

```` </h1> ````

This is what a heading tag looks like inside an HTML document:

````<h1>This is a Heading</h1>````

and when viewed in a web browser it looks like this:
##This is a Heading

Here is another example.
The ````<i>```` tag will produce italicized text.

````Italicize for <i>emphasis</i>````

shows up as:

Italicize for *emphasis*

There are several sample HTML documents for you to work with in this repo, called `index_barebones.html` and `index2.html`. These files are for you to use in the following exercises and you can modify them however you like.

###[HTML Reference on MDN](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference)

####HTML basics exercises

* Create a webpage that prints your name to the screen. 
* Create a webpage that prints the numbers 1 - 10 to the screen. 
* Create a webpage and set its title to "This is a webpage". 
* Create a webpage that prints the message "When was this webpage created? Check page's title for the answer." to the screen, and set the title of the page to the current date.
* Create a webpage that prints any text of your choosing to the screen, do not include a head section in the code. 
* Repeat exercise #5, but this time include a head section in the code. 
NOTE: Include comments in every HTML basics exercise.

####HTML text exercises

* Print your name in green. 
* Print the numbers 1 - 10, each number being a different color. 
* Prints your name in a Tahoma font. 
* Print a paragraph with 4 - 5 sentences. Each sentence should be a different font. 
* Print a paragraph that is a description of a book, include the title of the book as well as its author. Names and titles should be underlined, adjectives should be italicized and bolded.
* Print your name to the screen with every letter being a different heading size.


####HTML text formatting exercises

* Print the squares of the numbers 1 - 20. Each number should be on a separate line, next to it the number 2 superscripted, an equal sign and the result. (Example: 102 = 100) 
* Prints 10 names with a line break between each name. The list should be alphabetized, and to do this place a subscripted number next to each name based on where it will go in the alphabetized list. (Example: Alan1). Print first, the unalphabetized list with a subscript number next to each name, then the alphabetized list. Both lists should have an ``<h1>`` level heading.
* Print two paragraphs that are both indented using the ``&nbsp;`` command.
* Print two lists with any information you want. One list should be an ordered list, the other list should be an unordered list. 
* Prints an h1 level heading followed by a horizontal line whose width is 100%. Below the horizontal line print a paragraph relating to the text in the heading. 
* Print some preformatted text of your choosing. (hint: use the ``<pre>`` tag) 
* Print a long quote and a short quote. Cite the author of each quote. 
* Print some deleted and inserted text of your choosing. 
* Print a definition list with 5 items. 
* Print two addresses in the same format used on the front of envelopes (senders address in top left corner, receivers address in the center). 
* Print ten acronyms and abbreviations of your choosing, each separated by two lines. Specify the data that the abbreviations and acronyms represent. 


####HTML link exercises

* Create some links to various search engines (google, yahoo, altavista, lycos, etc). 
* Create links to five different pages on five different websites that should all open in a new window. 
* Create a page with a link at the top of it that when clicked will jump all the way to the bottom of the page. 
* Create a page with a link at the bottom of it that when clicked will jump all the way to the top of the page. 
* Create a page with a link at the top of it that when clicked will jump all the way to the bottom of the page. At the bottom of the page there should be a link to jump back to the top of the page. 


####HTML image exercises

* Display five different images. Skip two lines between each image. Each image should have a title. 
* Display an image that has a border of size 2, a width of 200, and a height of 200. 
* Display an image that when clicked will link to a search engine of your choice (should be opened in a new window). 
* Display an image that when clicked will link to itself and will display the image in the browser by itself. 
NOTE: Include the alt attribute in every <img> tag in the HTML image exercises.
