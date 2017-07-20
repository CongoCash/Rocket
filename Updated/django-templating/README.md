Django Templating: Logic, Filters, and Tags
==========================

##What is Django?
The last few days, you have been using the Django ORM to build model relationships and better understand the connection between Python classes and database tables. The ORM is one of the most powerful features of Django, but it is only one piece.

Django is an open source web framework based on the MVC pattern and it includes a web server, a templating system, caching, form serialization and validation, the admin, user authentication, and built-in security features, among other features.

![djangopony]

###What's a Web Framework?
If you visit the Wikipedia pages for Django or Rails (or Laravel, Flask, Spring, or pretty much any other web framework), it will say somewhere in the first sentence that it is an "(open source) web application framework written in XYZ language"--but what exactly does that mean?

A web framework isn't its own programming language, it is a collection of features, libraries, or applications written in a programming language. E.g., Django is all written in Python. These libraries help speed up the process of web development.

So, a web framework consists of:

* Programming language
* Features, libraries, or applications
* Governing body (e.g., Django Software Foundation)
* Community, documentation, and support

###Why do we use web frameworks?
* <em>No need to reinvent the wheel</em>. It would be extremely tedious to recreate everything included in Django. Think of the loops, conditionals, and classes you've been writing in Python--would you know how to utilize that knowledge to create a web framework with database management, an HTTP server, url routing, templates, and all the other features of Django?
* <em>Open source</em>. If you made a web framework for yourself, you'd be the only one maintaining and testing it. Django is maintained by a team of core developers and contributed to by thousands more.
* <em>Development speed</em>. Django allows you to spin up rich web applications in a very short amount of time.
* <em>Guidelines and structure</em>. There are certain best practice web development standards, and using a web framework helps enforce them. Additionally, by having a predefined structure, it becomes much easier to read and reuse other people's code.

##Web Framework and Content Management System (CMS) Landscape
These are just a few of the web frameworks currently used

![framework landscape]

####The Have's
* Ruby
	* Rails
	* Sinatra
* JavaScript
	* Node.js / Express
* Python
	* Django!
	* Flask, Pyramid, Tornado

####The Have-not's
* ASP .NET
* PHP
    * CakePHP, Zend
    * CodeIgniter, Phalcon, Laravel
* Java
    * Grails, Struts, GWT, Spring

###Not all web frameworks are created equal
Different frameworks offer more or less features. Within the Python space:

![framework_spectrum]

You can read more about Python web applications and frameworks [here].

###Django comes batteries included
* There’s a lot of boilerplate in building a website.
* Frameworks targeted for specific areas aim to:
	* Reduce setup time.
	* Increase speed of development.
* What kinds of things are included?
	* WYSIWYG Text editors.
	* Scaffolding - database wrappers for quick content editing.
	* Entire Admin sites.
	* Templating
* Why not always use a “batteries included” framework?
	* The more that’s built in, that harder it can be to customize later.

###Who uses Django?

![django users]

Social
* Instagram
* Pinterest
* Eventbrite
* Disqus
* Rdio
* Reddit Gifts
* News
* The Washington Times
* The Onion
* PBS*
* NASA*

Other
* Mozilla
* Bitbucket
* National Geographic
* 23andMe
* Symantec
* Politifact

`*`: Not every website

##Django Follows the MVC Pattern (MTV)
MVC, or model-view-controller, is a common software architectural pattern for implementing user interfaces and is used all over the web by Django, Rails, and other frameworks.

The premise is to separate code into three logical, connected parts:

* Model. Your actual application data and basic rules around its behavior. These are your Django models and the methods you write for them.
* View. The output (usually visual) of your application, e.g., your HTML files.
* Controller. The connecting layer between your models and your views. Controllers specify what data a view will show, and how to handle user responses. For example, your Facebook newsfeed and your friends' timelines contain data from the same model (Post), but they are shown in two different views. The controllers contain logic to say "show interesting new Posts in my newsfeed", but "show Posts about a single user in that person's timeline"
Note that in Django these pieces aren't named model, view, and controller, but actually model, template, view. Don't worry about the naming conventions for now.

###Model view controller
Your models represent the actual data and how it behaves, your controllers specify how to interact with data in views, and your views actually display the data. Your models do not directly interact with your views.

![mvc diagram]

###Exploring Django Project Structure
Django projects can have a slightly flexible structure, but the default is what the <code>startproject</code> and <code>startapp</code> commands provide. Your Django project should look like the below:

````
/your_project
    /manage.py
    /your_app
        /__init__.py
        /admin.py
        /models.py
        /tests.py
        /views.py
    /your_project
        /__init__.py
        /settings.py
        /urls.py
        /wsgi.py
````

###Relating to MVC
Earlier we discussed the model-view-controller pattern. Let's look at how this applies to our actual Django project

Your models will be located in <code>your_app.models</code>

Your controllers are in <code>your_app.views</code>

In Django, TEMPLATES are the view files that visually present your data, and VIEWS are the connecting logic between your models and your templates.

We'll talk more about adding templates later.

##Basic URL Routing
There is one other major piece of this puzzle: URL routing. URL routing is the piece that processes what a user should see based on the URL they requested. For example, facebook.com will show you your newsfeed, but if you went to facebook.com/username, it would know to show you that user's timeline. If you tried to go to a url that Facebook doesn't recognize (e.g., facebook.com/BAD_URL), you will get a 404 page not found error. Similarly, you must specify in your Django app how to handle users requesting different urls.

Django is designed so that when you go to a URL, it routes you to the correct matching view. So, let's update our MVC diagram from earlier:

This:

![old mvc diagram]

Becomes this:

![new mvc diagram]

Django

* URLs (routing)
* Models (data)
* Views (logic)
* Templates (HTML / output)

###Adding Route Handling
Let's add a new route to our urls in the blog project we worked on last week.

When you look at your urls, you should see something like this

<strong>your_project/your_project/urls.py</strong>

````Python
urlpatterns = patterns('',
    #
    #
)
````

Django is already supplying you with <code>urlpatterns</code>, which it knows how to handle. All you have to do is fill in individual routes

The line url(r'^hello/', 'your_app.views.home'), represents a single route we are adding

<strong>your_project/your_project/urls.py</strong>

````Python
urlpatterns = patterns('',
    url(r'^hello/$', 'your_app.views.hello'),
)
````

The first part of this route is a Python regular expression. This will match the string "hello" or "hello/". So, this is a route for the url yourdomain.com/hello. In your development environment, this will look like 127.0.0.1:8000/hello.

The second part of this route specifies which view this route should point to.
<hr>
Now let's add the matching view

Each view you write is a function. It takes (at minimum) a <code>request</code> as a parameter. We are returning an HTTP response, which for now is just a string.

Navigate to 127.0.0.1:8000/hello in your browser and see the result!

<strong>your_project/your_app/views.py</strong>

````Python
from django.http import HttpResponse

def hello(request):
    return HttpResponse("This is my homepage")
````
##URL Routing
This is the overall flow of a Django app.

![app flow]

##Capturing variables in URL Routes
To make our application more dynamic, we can also capture variables in our URLs

<strong>urls.py</strong>

````Python
urlpatterns = patterns('',
    # Variables are captured in the part of the url in parentheses
    # The '?P<variable_name>' syntax lets you name the variable
    # The regex after the variable's name indicates what is allowed
    url(r'^hello/(?P<name>\w+)$', 'your_app.views.hello'),
)
````

Our view can then take this extra named variable parameter and use it in the view function.

<strong>views.py</strong>
````Python
def hello(request, name):
    return HttpResponse("Hello, {}".format(name))
````

##Adding Templates
Of course, most web sites have more than just simple strings as output. We can also return an HTML response.

Your browser knows how to format this string of HTML.

But you can imagine that this would very quickly become unwieldy if we tried to put a full page worth of HTML here. So, how do we separate this code and add more structure?

<strong>views.py</strong>

````Python
def hello(request, name):
    return HttpResponse("<h1>Hello!</h1>"
                        "<p>Your name is {}</p>".format(name))
````

We can use Django's templating system to render HTML when we hit certain views.

1. Add a new directory in your app called 'templates'
2. Add a new HTML file 'hello.html' inside this directory
If you are getting an error page that says "TemplateDoesNotExist", try adding the following to your settings: <code>TEMPLATE_DIRS = [os.path.join(BASE_DIR, 'your_app/templates')]</code>. Django will attempt to find your template files by default, but if it is having trouble you can explicitly specify their location with this setting.

<strong>views.py</strong>
````Python
from django.shortcuts import render_to_response

def hello(request, name):
    return render_to_response("hello.html")
````

<strong>your_app/templates/hello.html</strong>
````HTML
<!DOCTYPE html>
<html>
<head lang="en">
    <meta charset="UTF-8">
    <title></title>
</head>
<body style="background-color: blue;">
<h1>Howdy Djangonauts!</h1>
</body>
</html>
````

###Passing Variables to Templates
Django's views and templates can also be dynamic. To use the <code>name</code> variable we captured earlier, pass it in a dictionary in the view's response.

The key is name of the variable that will be used in the template. The value is the actual data you want to pass to the template.

Django templates will render variables with the <code>{{ variable_name }}</code> syntax

<strong>views.py</strong>
````Python
from django.shortcuts import render_to_response

def hello(request, name):
    return render_to_response(
        "hello.html",
        {'name': name}
    )
````

<strong>your_app/templates/hello.html</strong>
````HTML
<body style="background-color: blue;">
<h1>Howdy Djangonaut {{ name }}!</h1>
</body>
````
###Template Rendering
With template rendering, our app flow now looks like this:

![app flow with template rendering]

###Why templates?
Most web frameworks use a templating language. Just like programming languages, they all have different syntax, but are usually simpler. So why do we use them?

* They allow us to separate business logic from HTML.
* We can easily place data into our HTML.
* Can now reuse our HTML to keep our application DRY.
* Some common security issues are protected against.

###Templates Review
Here's our basic template. We have our HTML and we're including a variable in our template.

````Python
<html>
    <body>
        <div>{{ some_variable }}</div>
    </body>
</html>
````

##Playing Cards
Let's set up the example we'll be using for the rest of this repo.

First, create a new Django project with an application called "cards". See the [instructions for starting a project] if you forget.

Second, in our <code>models.py</code> let's add the following model, then run our migrations.

````Python
class Card(models.Model):
    SPADE = 0
    CLUB = 1
    DIAMOND = 2
    HEART = 3
    SUITS = (
        (SPADE, "spade"),
        (CLUB, "club"),
        (DIAMOND, "diamond"),
        (HEART, "heart")
    )
    suit = models.PositiveSmallIntegerField(choices=SUITS)
    rank = models.CharField(max_length=5)
````

The suit field is a good example of how in Django we represent a field that has a defined set of choices.

Next, let's create a file in our cards application called <code>utils.py</code>. More information can be found in the [Django util docs]. Essentially we will be creating a <code>@classmethod</code>.

Copy the following code into our file.
````Python
from cards.models import Card

def create_deck():
    """
    Create a list of playing cards in our database
    """
    suits = [0, 1, 2, 3]
    ranks = ['two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'jack', 'queen', 'king', 'ace']
    cards = [Card(suit=suit, rank=rank) for rank in ranks for suit in suits]
    Card.objects.bulk_create(cards)
````
Now let's run this function, which will create a list of cards in our database by running these commands.

````
>> python manage.py shell
>> from cards.utils import create_deck
>> create_deck()
````

Now, check your database and see that the cards have been created.

###Logic
Templates can have some basic logic statements like conditionals and for loops, which come in handy when presenting data in our HTML.

It's important to realize though, that our templates are not python. If you're trying to do something that you're finding complicated, that means you should probably be doing it in python.

Copy the code below for our first page. Also create a blank template, <code>cards.html</code>.

<strong>urls.py</strong>
````Python
urlpatterns = patterns('',
    url(r'^$', 'cards.views.home', name='home'),
)
````

<strong>views.py</strong>
````Python
def home(request):
    data = {
        'cards': Card.objects.all()
    }

    return render(request, 'cards.html', data)
````
See the red squiggly under 'Card'? Move your cursor over to the word and press alt + O to quickly import the package. Very handy trick in Pycharm.

###Conditionals
Django's templating language gives us some basic if / else type of statements.

````HTML
<div>
    {% if some_variable == 0 %}
        <span>Some text for 0</span>
    {% elif some_variable == 1 %}
        <span>Some text for 1!</span>
    {% else %}
        <span>Some text for everything else...</span>
    {% endif %}
</div>
````
Now depending on the value of our variables, whether they be strings, integers, booleans, etc we can have different HTML in our templates.

You can do other basic comparisons that you're used to normally doing: <code>!= > >= < <= not and or in</code>.

###Loops
Let's put the following code in our currently blank template, <code>cards.html</code>.

````HTML
<div>
    {% for card in cards %}
        <p>Suit: {{ card.suit }}, Rank: {{ card.rank }}</p>
    {% endfor %}
</div>
````
As we've seen before, we can loop over our list of cards and create HTML for each one. In the loop we'll have access to a <code>card</code> object, which we know has <code>suit</code> and <code>rank</code> fields.

We can use an easier to read version of suit by replacing <code>card.suit</code> with <code>card.get_suit_display</code>. Try this out in your template file.

###Filters
Django has built in filters that you can apply easily to variables in templates. Let's check out just a few.

Create a new page, which also passes our card data to a template called <code>card_filters.html</code>

````HTML
We have {{ cards | length }} cards!

{% for card in cards %}
    <div>
        <p>
            Capitalized Suit: {{ card.get_suit_display | capfirst }} <br>
            Uppercased Rank: {{ card.rank | upper }}
        </p>
    </div>
{% endfor %}
````

We can see above we used three different filters.
* length gives us the length of a list or string.
* capfirst capitalizes a string.
* upper will uppercase a whole string.

How will we be able to display this HTML?

###Template Tags
There are also template tags, like <code>url</code> which do slightly more complicated functions than filters.

Let's again, make a new page for this example.

````HTML
<style>
    .odd {
        color: blue;
    }
</style>

It's {% now "SHORT_DATETIME_FORMAT" %}!

{% for card in cards %}
    <p class="{% cycle 'even' 'odd' %}">
        Suit: {{ card.get_suit_display }}, Rank: {{ card.rank }}
    </p>
{% endfor %}
````
Above we're using 2 template tags.
* <code>now</code> gives us the current timestamp, which we can format however we'd like.
* <code>cycle</code> switches back and forth printing out each value for every pass through the for loop.

###Custom Filters and Tags
We're also able to create our own filters and tags to use within our own templates.

These filters and tags are just python functions taking in parameters from our template and outputting back html or values to be placed back in our pages.

First let's recreate a couple of built in filters to see how they work.

####Our First Filter
Let's see how the <code>first</code> filter actually works.

1. Create a <strong>python package</strong> called <code>templatetags</code> in your cards application.
2. Make sure you have an <code>__init__.py</code> file in your templatetags folder. This should be empty.
3. Create a file in <code>templatetags</code> called <code>list_filters.py</code>
4. Add the following code to the file:

````Python
from django import template

register = template.Library()

@register.filter
def first(list):
    if list is not None and len(list):
        return list[0]
````
* We can see that our filter is just a python function, which grabs the first item in a list.
* We use the <code>@register</code> decorator to tell Django to recognize this function as a filter.
<hr>
Now let's use the filter!

1. Set up a new page (url, view, and template).
2. Include the following in your template

````HTML
{% load list_filters %}

{{ cards|first }}

{% with cards|first as first_card %}
    <p>Suit: {{ first_card.get_suit_display }}, Rank: {{ first_card.rank }}</p>
{% endwith %}
````

* We need to load our custom filters by using the name of the python file, <code>list_filters</code>.
* We can now use it just like all of the built-in filters.
* Since this returns a whole new object, we can use the <code>with</code> template tag to store it as a new variable in order to access it's different properties.

####Custom Filters with Parameters
Let's see one more example, where we also pass a parameter to our custom filter.

1. Put this new filter in our <code>list_filters.py</code> file.

````Python
@register.filter
def suit(list, suit_type):
    return [item for item in list if item.get_suit_display() == suit_type]
````
* This filter will return only cards in the list with the given suit.

2. Create a new page and place this in your template.
````HTML
{% load list_filters %}

{% for card in cards|suit:"diamond"  %}
    <p>Suit: {{ card.get_suit_display }}, Rank: {{ card.rank }}</p>
{% endfor %}
````
* We can call our filter and now pass it the suit we'd like to filter the deck of cards by.
* In this example <code>suit_type</code> in our custom filter ends up being "diamond".

###DRY Templates
As we've heard many times, we want to keep our python code organized, clean, and DRY.

Our templates and HTML should be held up to the same standard.

Django's templating language gives us a few different mechanisms to implement this.

First let's take a look at our templates inheriting from another template.

###Inheritance
We've written python classes that inherit from others in order to reuse code.

Our templates can implement the same concept.

Let's create a new template called <code>base_template.html</code> with the following code:

````HTML
<!DOCTYPE html>
<html>
    <body>
        <h1>Welcome to our Card Game!</h1>
        {% block content %}{% endblock content %}
    </body>
</html>
````

* First, notice this base template includes the basics of our page, like the doctype and html tags.
* Next we see these new django template tags, block tags, we'll get back to this in a minute.
* Generally, most django applications will have a base template that has all of the common elements you would see on every page such as the header and footer.

Next let's set up a new page for our user's profile of this card game we've been working on.

In our new template let's insert the following code.

````HTML
{% extends 'base_template.html' %}

{% block content %}
    <p>Hi Player 1, you have 0 wins and 0 loses.</p>
{% endblock content %}
````
* First, we tell Django that this template wants to inherit from our base template by using the <code>extends</code> django template tag. This has to be the first line in our template.
* Secondly, we see <code>block</code> tags again. This is saying, take our base template and whenever we see a block, insert content found in the same named block from our sub templates.
* This means our text from our profile page, will be inserted into the <code>block</code> in our base template.

###Inheritance: Another example
Let's set up a new page for a FAQ about our web game.

In our new template let's insert the following code.

````HTML
{% extends 'base_template.html' %}

{% block content %}
    <p>Q: Can I win real money on this website?</p>
    <p>A: Nope, this is not real, sorry.</p>
{% endblock content %}
````

Again, we can see that it shares the same base template and code, with this content block overridden with our page specific html.
Let's also make this addition to the base template, which will take affect on our FAQ and Profile page.

````HTML
<!DOCTYPE html>
<html>
    <body>
        <div><a href="{% url 'profile' %}">Profile</a> |  <a href="{% url 'faq' %}">FAQ</a></div>
        <h1>Welcome to our Card Game!</h1>
        {% block content %}{% endblock content %}
    </body>
</html>
````

##Include
We've seen how to make our templates DRYer by having them extend our other templates. We can also reuse template snippets as well, instead of duplicating our HTML across pages.

So far we've used the same loop to print out our cards multiple time. Let's make it reusable.

1. Create a folder inside your <code>templates</code> folder called <code>includes</code>. Note, this is a Django common practice for organizing templates meant to be included, but not absolutely necessary.
2. Create a template file called <code>hand.html</code> with the following html, which we've used several times:

````HTML
{% for card in cards %}
    <p>Suit: {{ card.get_suit_display }}, Rank: {{ card.rank }}</p>
{% endfor %}
````

Now let's set up a new page that will deal a blackjack hand and use our new template.

Create a new url and a view with the following code, which will limit our deck to only 2 random cards. Ordering by <code>'?'</code> creates a random deck.

````Python
def blackjack(request):
    data = {
        'cards': Card.objects.order_by('?')[:2]
    }

    return render(request, 'blackjack.html', data)
````

Create a template, <code>blackjack.html</code> with the following code. The new <code>include</code> tag, is what we use to put our <code>hand.html</code> template html in this template.

````HTML
{% extends 'base_template.html' %}

{% block content %}
    <h2>Blackjack!</h2>
    <p>Here's your hand...</p>
    {% include 'includes/hand.html' %}
{% endblock content %}
````

###Poker Hand
Now let's say we want to create a page, which gives us a poker hand. We can now reuse our template snippet and not duplicate our code. This way if we want to change how the cards look in the future we only need to change one template instead of many. Let's create that poker hand page.

1. Create a new url and a view with the following code, which will limit our deck to 5 random cards.
````Python
def poker(request):
    data = {'cards': Card.objects.order_by('?')[:5]}

    return render(request, 'poker.html', data)
````
2.Create a template, <code>poker.html</code> with the following code. Again we use the <code>include</code> tag, to reuse our template snippet, which displays our cards.
````HTML
{% extends 'base_template.html' %}

{% block content %}
    <h2>Poker!</h2>
    <p>Here's your hand...</p>
    {% include 'includes/hand.html' %}
{% endblock content %}
````

##Django Debug Toolbar
Let's check out DjDT, a tool that every Django developer should be using. It is great for seeing which templates are being included and inherited from on a page as well as what variables they have available

It also has many other uses, the most popular being seeing the speed of your SQL queries. Let's set it up! First, make sure you're in a virtual environment!

1. <code>pip install django-debug-toolbar</code>
2. Put debug_toolbar in your INSTALLED_APPS.
3. Put INTERNAL_IPS = ("127.0.0.1", "10.0.2.2") in your local_settings.py

Now that we have DjDT set up, reload your poker hand page, there should be a tab on the right called DjDT. Click on it!

* First, let's quickly look at the SQL tab. We can see that it gives us information on all of the SQL queries this page ran. We can see how long it took for us to get 5 random cards from our database.
* Secondly, let's checkout the templates section. We can see 3 templates listed, <code>poker.html</code> which are view is pointed to, <code>base_template.html</code> which are template extends and <code>includes/hand.html</code> which is the template we included on our page.
* If you click "Toggle context" it will show you what variables each template has access to.
* If you click the template itself, it will show you the Django template markup.
This may not be obvious now, but it is extremely handy for debugging!

##Static Files
When building an application you often need to include external files, such as images, JavaScript and CSS. Django has some built-in functionality for templates to help make including this as easy as possible. Let's follow these steps to make sure we're ready to include static files:

* Create a folder in your cards application called <code>static</code>. Each of your django applications can have their own static folder with assets related to that application.
* Let's create 3 folders inside of our static folder, <code>img</code>, <code>js</code>, and <code>css</code>.
* <code>pip install pillow</code> <- this will let our python code work with images.
* In <code>urls.py</code> add the following at the bottom of the file:
````Python
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
````

The packages you want to import from are
* <code>django.conf</code>
* <code>django.conf.urls.static</code>

* In <code>settings.py</code> add the following before the line that imports your local_settings file:
````Python
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(PROJECT_ROOT, "static", *MEDIA_URL.strip("/").split("/"))
````

##Images
First, let's see how we would just add an image of a playing card into our application.

In our base template, let's do two things:

1. Add <code>{% load staticfiles %}</code> to the top of the template.
2. Put the following in our header div, before our Profile link:

````HTML
<img id="joker" width="40px" src="{% static "img/red_joker.jpg" %}">
````
Also, download the [red joker] image and place it in <code>static/img</code> folder that we just created.

If you reload any of your pages, we now have a playing card showing up in our header.

<code>static</code> is a template tag we can use to specify with a string what static file we'd like to use. To use it, we just load the <code>staticfiles</code> template tag library at the top of the file.

##JavaScript and CSS
The same static tag is how we also include javascript or css files into our application.

First, create <code>cards.js</code> and <code>cards.css</code> in their respective static folders and then copy/paste the code into them. Here is the [javascript] file. Here is the [css] file.

Next, include the following in the head section of your base template so that they're loaded on every single page.

````HTML
<head>
    <script src="//code.jquery.com/jquery-1.11.0.min.js"></script>
    <script src="{% static 'js/cards.js' %}"></script>
    <link rel="stylesheet" type="text/css" href="{% static 'css/cards.css' %}">
</head>
````
Reload your page, now that we've included some javascript and css, our playing card rotates every couple of seconds.

##Media
We've now seen how to include other files into our application, but what if we want to associate an image or file with one of our models?

Let's have our <code>Card</code> model actually save the image of the card it's associated with so we can use that to display it.

First, let's add the following image field to our model, create a migration, then migrate.

````Python
image = models.ImageField(upload_to='card_images', blank=True, null=True)
````

Our image field has an <code>upload_to attribute</code>, which defines what folder images for this field are saved to in our project.

<hr>

We don't want to upload every single card's image one by one, so let's use a modification of our function in <code>utils.py</code> to do it for us.

1. Create a new static folder in our root directory. The same directory that has all of our application folders and <code>manage.py</code> file.
2. Create a folder inside of the static folder called <code>media</code> and a folder inside of that named <code>card_images</code>.
3. Download images clicking on this [folder] and then clicking 'view the full file'. Put the playing card images inside of this new, <code>card_images</code> folder. Normally if we uploaded images, Django would do this for us. Your folder structure should be static/media/card_images/jpegs of card images.
4. Overwrite your current <code>utils.py</code> with the code found in this [utils.py file], which adds our images in appropriately for each card.

Then, open up the django shell by running <code>python manage.py shell</code> and run the follow commands:

````
>>> from cards.models import Card
>>> Card.objects.all().delete()
>>> from cards.utils import create_deck
>>> create_deck()
````

##Media - All Together Now
Now all of our playing cards in our database should have an image tied to them appropriately.

Let's edit our <code>hand.html</code> snippet and make sure of the new images:
````HTML
{% for card in cards %}
    <img width="100px" src="{{ card.image.url }}">
{% endfor %}
````
If we go to our blackjack and poker pages, we now have actual playing card images!

In a template, to get the full url to media that we have uploaded, you use the url property of that field.


##Missions

###URL Exercises
Create a route that takes a variable and print out that variable in the response.

Create a route that takes two variables. Print 'fizz' if the first is a multiple of 3, and print 'buzz' if the second is a multiple of 5.

Learn more about Django routing in the Django [url docs]

###Template Rendering Exercises
Make a page that takes two url parameters: name and color. Welcome the user by name and make the page background the specified color.

###Template Logic Exercises
* Create a page that only displays cards that are clubs.
* Create a page that only displays cards that are diamonds or hearts.
* Create a page that displays the message "This is just a spade" if the card is a spade or displays the usual suit and rank.
* Create a page that displays only face cards. Only use 1 if statement.

###Template Tags Exercises
* Using a filter, truncate the suit so that only the first letter is shown.
* Change the now template tag, to display the full month and date only.
* Using a template tag, put a link on our filter page that links to our tag page and vice versa
* Using a filter, get a random card to display from the list.
* Using a filter, display only the last card from the list.
* Use the regroup template tag to display the cards by their Suit.

###Custom Filter Exercises
* Write a filter, which filters the list to only show "Aces".
* Write a filter, which takes a parameter called rank, and filters the list of cards for only that rank.

###Inheritance Exercises
* Create a new page that deals 5 cards. Have this page inherit from our base template.
* Add a footer below the block content, which says "copyright [your name] 2014"
* Create a `<head>` section in your base template, which has a `<title>` tag to display the title of the page.
* Have the contents of your title be a new block, which each page can overwrite to put a proper title. For example, your web browser's tab on the profile page should say "Profile".

###Include Exercises
* In our base template, let's put links to our poker and blackjack pages.
* Create 2 new pages, one that shows all Hearts and one that shows all cards that are not face cards. Reuse our template via include.
* For our blackjack page, let's also show the dealer's hand. We'll need our view to give 2 more random cards for the dealer and use our hand.html snippet. Hint, check the Django documentation on how you can specificy variables with the include tag.
* Show what the current score is for the player and dealer.
* Show a message if the dealer or player has a "blackjack" (Cards add up to 21).

###Static Files and Media Exercises
* There should be a black joker card in the library of playing card images. Add that to your project's image static folder and put that on the other side of your header.
* Register our <code>Card</code> model with the admin, then go upload new photos for the playing cards, to see how they're changed. Specifically the library of playing card images should have alternate ones for face cards you can use.
* Create a second image field on our Card model for alternate images of cards. After running your migrations, add some alternate photos for your cards.
* In your template, if the card has an alternate photo, show that one, else show the original photo.

###Overall Mission Project
Let's turn our portfolio sites into Django-powered sites! Here are some exercises to get you started. Be creative!

* Create a base template, which contains your header, top navigation bar with links, and footer.
* Create 2 pages, a home page and about me, which extend the base template and display relevant content about yourself.
* Use a picture of yourself and your CSS using Django's static files.
* Create a new 'projects' page and a project model in your database. Have this show a full list of projects.
* Have your home page show one random project. Use Django filters and template tags to get the random project. Use the <code>include</code> template tag to reuse display a project between your home page and project list page.



[djangopony]: img/djangopony.png
[framework landscape]: img/framework_landscape.png
[framework_spectrum]: img/framework_spectrum.png
[here]: http://docs.python-guide.org/en/latest/scenarios/web/
[django users]: img/djangoco.jpg
[mvc diagram]: img/mvc_diagram.png
[old mvc diagram]: img/old_mvc_diagram.png
[new mvc diagram]: img/new_mvc_diagram.png
[app flow]: img/app_flow.png
[url docs]: https://docs.djangoproject.com/en/dev/topics/http/urls/
[app flow with template rendering]: img/app_flow_with_template_rendering.png
[instructions for starting a project]: https://github.com/rocketu/django-orm/blob/master/README.md
[Django util docs]: https://docs.djangoproject.com/en/1.7/ref/utils/
[red joker]: img/red_joker.jpg
[javascript]: assets/cards.js
[css]: assets/cards.css
[folder]: assets/playing_cards.zip
[utils.py file]: assets/utils.py