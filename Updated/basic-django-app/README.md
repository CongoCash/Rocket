Basic Django App
====================

##Recap
So far, this is the flow of our application with URL's, views and templates.

![app flow]

##Adding Models
Let's fill in the rest of this diagram: adding models, and allowing users to interact with our application instead of just serving static pages.

![app flow with models]

##Let's Make a New Django Project!
* Create a new Django project named <em>Favorites</em>
* Add an app called <code>hollywood</code>
* Add the following models and migrate
* Feel free to use the [project cheat sheet] if you need to!

````Python
class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name


class Movie(models.Model):
    name = models.CharField(max_length=100)
    release_year = models.PositiveSmallIntegerField()
    genre = models.ForeignKey(Genre)

    def __unicode__(self):
        return self.name


class Actor(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveSmallIntegerField()
    movies = models.ManyToManyField(Movie)
````
##Laying out our application
Our Django app will have this site map. This basic layout can be found in many applications.

![hollywood site map]

##First, let's create a site landing page
Add the following code to the given locations.

<strong>urls.py</strong>
````Python
from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'hollywood.views.home', name='home'),
)
````

<strong>templates/home.html</strong>
````HTML
<h1>Welcome to Hollywood!</h1>
````

<strong>views.py</strong>
````Python
from django.shortcuts import render

def home(request):
    return render(request, "home.html")
`````

There are many ways to return an HTML response. Here is an alternate method

<strong>views.py (alternate)</strong>
````Python
from django.shortcuts import render_to_response

def home(request):
    return render_to_response("home.html")
````

##Then we add a Genre landing page
<strong>urls.py</strong>
````Python
urlpatterns = patterns('',
    ##
    url(r'^genres/$', 'hollywood.views.genres', name='genres'),
)
````

<strong>views.py</strong>
````Python
def genres(request):
    return render_to_response("genres.html")
````

<strong>genres.html</strong>
````HTML
<h1>Genres live here</h1>
````
We can now update our home page to include a link to the genres page

<strong>home.html</strong>
````HTML
<h1>Welcome to Hollywood!</h1>
<a href="{% url "genres" %}">Genres</a>
````

##Creating an index page
Of course, we don't just want a static genre page. It would make sense to turn this into an index page (a page that lists all our genres), so users can see them all. This is where we can add in our models.

We use Django template tags to write a for loop with <code>{% for %}</code> and <code>{% endfor %}</code> just like we saw Monday.

<strong>views.py</strong>
````Python

def genres(request):
    genres = Genre.objects.all()
    return render_to_response("genres.html", {'genres': genres})
````

<strong>genres.html</strong>
````HTML
<h1>Genres live here</h1>
<ul>
    {% for genre in genres %}
        <li>{{ genre.name }}</li>
    {% endfor %}
</ul>
<a href="{% url "home" %}">Back to Hollywood</a>
````

##Flow through the app

![app flow 3]

##Create new entries
Users can't just log into the admin to make changes. We need to create a page where they can do that.

This page will include a form where users can input the information necessary to create a new genre. Where before we wrote programs that used Python's <code>raw_input</code>, now users will be able to input information in a web form.

##Model Forms
Django makes this easy for us by automatically creating forms for models.

All we need is to declare this ModelForm subclass and specify the model we are interested in. Then Django will introspect the model and create an appropriate form.

<strong>hollywood/forms.py</strong>
````Python
from django.forms import ModelForm
from hollywood.models import Genre


class GenreForm(ModelForm):
    class Meta:
        model = Genre
````

##Display our model form
<strong>urls.py</strong>
````Python
urlpatterns = patterns('',
    ##
    url(r'^genres/new/$', 'hollywood.views.new_genre', name='new_genre'),
)

````

<strong>views.py</strong>
````Python
def new_genre(request):
    form = GenreForm()
    data = {'form': form}
    return render(request, "new_genre.html", data)
````

<strong>genres.html</strong>
````HTML
<a href="{% url 'new_genre' %}">Add new genre</a>
````

<strong>new_genre.html</strong>
````HTML
<h1>Add new genre</h1>
<form method="post">
    {% csrf_token %}
    {{ form }}
    <input type="submit" value="Add new genre">
</form>
````
##Proccess our form
When you visit an HTML page, you are sending a GET request. When you are creating a new object, you are sending a POST request. Django lets you examine these requests and determine which is which. So, when you first go to the form page, you are sending a GET request and will hit the <code>else</code> condition, and when you submit the form you will hit the <code>if</code> condition.

<strong>views.py</strong>
````Python
def new_genre(request):
    # If the user is submitting the form
    if request.method == "POST":

        # Get the instance of the form filled with the submitted data
        form = GenreForm(request.POST)

        # Django will check the form's validity for you
        if form.is_valid():

            # Saving the form will create a new Genre object
            if form.save():

                # After saving, redirect the user back to the index page
                return redirect("/genres")

    # Else if the user is looking at the form page
    else:
        form = GenreForm()
    data = {'form': form}
    return render(request, "new_genre.html", data)
````

##App flow through object creation

![app flow 4]

##Viewing your data
Once you've created these new entries, people are going to want a way to look at the data. You can add more data to the index page, but as you can imagine this would get messy with complex models. Instead, it is common practice to have a detailed view page.

<strong>urls.py</strong>
````Python
urlpatterns = patterns('',
    ##
    url(r'^genres/(?P<genre_id>\w+)/$', 'hollywood.views.view_genre', name='view_genre'),
)
````

<strong>views.py</strong>
````Python
def view_genre(request, genre_id):
    genre = Genre.objects.get(id=genre_id)
    data = {"genre": genre}
    return render(request, "view_genre.html", data)
````

Add a template...

<strong>view_genre.html</strong>
````HTML
<h1>{{ genre.name }}</h1>
<a href="{% url "home" %}">Back to Hollywood</a>
<a href="{% url "genres" %}">Back to Genres</a>
````

And then update your genre index page

<strong>genres.html</strong>
````HTML
<h1>Genres live here</h1>
<ul>
    {% for genre in genres %}
        <li><a href="{% url "view_genre" genre.id %}">{{ genre.name }}</li>
    {% endfor %}
</ul>
<a href="{% url "home" %}">Back to Hollywood</a>
````
For urls that take arguments, you can pass the arguments within the <code>{% url %}</code> tag after the url name.


##Mission Part I [Essential]
* Add a movie index page that lists out all your movies. Add some movies in your Django shell so that you can see them.
* Add a page to create new movies, with the necessary routing, form handling, links and redirects.
* Make view pages for your movies. These will be more interesting because they have more data.

<strong>Finish Hollywood [Essential]</strong>

Add the index, create, and detail pages for Actors as we did for movies and genres. Go ahead and add some of your favorite movies, actors, and genres.

<strong>Reorganize templates [Extra]</strong>

You should have a lot of template files now. It's kind of messy. Move your model-specific templates into model-specific folders within your templates folder (e.g., all your movie templates go in templates/movies). Make sure you update your views so they now point to the right place.

<strong>New favorites [Extra]</strong>

Make a new app within your favorites project. It will be another logical grouping of favorite things. E.g., it could be nascar and your models could be Car, Team, Driver, or something else of your choosing!

##Laying out our application
Once again, let's look at the overall layout of our application

![hollywood site map]

##Editing existing records
Editing an existing object is a bit of a combination of the create view and the detail view -- you need a form to edit and process, but you are also finding an existing record.

Let's start by adding our route.

<strong>urls.py</strong>
````Python
urlpatterns = patterns('',
    ##
    url(r'^genres/(?P<genre_id>\w+)/edit/$', 'hollywood.views.edit_genre', name='edit_genre'),
)
````

<strong>views.py</strong>
````Python
def edit_genre(request, genre_id):
    # Similar to the the detail view, we have to find the existing genre we are editing
    genre = Genre.objects.get(id=genre_id)

    # We still check to see if we are submitting the form
    if request.method == "POST":
        # We prefill the form by passing 'instance', which is the specific
        # object we are editing
        form = GenreForm(request.POST, instance=genre)
        if form.is_valid():
            if form.save():
                return redirect("/genres/{}".format(genre_id))

    # Or just viewing the form
    else:
        # We prefill the form by passing 'instance', which is the specific
        # object we are editing
        form = GenreForm(instance=genre)
    data = {"genre": genre, "form": form}
    return render(request, "genres/edit_genre.html", data)
````
Our edit template looks almost identical to our create template because it has the form, but when you actually load the page, the form will be prefilled.

<strong>edit_genre.html</strong>
````HTML
<h1>Edit genre {{ genre.name }}</h1>
<form method="post">
    {% csrf_token %}
    {{ form }}
    <input type="submit" value="Update genre">
</form>
````

Let's also update our detail view so that it's easy to edit a record we are looking at.

<strong>view_genre.html</strong>
````HTML
<h1>{{ genre.name }}</h1>
<a href="{% url "edit_genre" genre.id %}">Edit genre</a>
<br>
<a href="{% url "home" %}">Back to Hollywood</a>
<a href="{% url "genres" %}">Back to Genres</a>
````

##Deleting records
Last but not least, we want to be able to delete records as well.

<strong>urls.py</strong>
```Python
urlpatterns = patterns('',
    ##
    url(r'^genres/(?P<genre_id>\w+)/delete/$', 'hollywood.views.delete_genre', name='delete_genre'),
)
````

This should be starting to look quite repetitive -- that's a good thing.

Deleting works a little differently. We don't actually need to go to a page to delete an object, we can simply delete the object in the view, and then redirect the user to the index page.

<strong>views.py</strong>
````Python
def delete_genre(request, genre_id):
    genre = Genre.objects.get(id=genre_id)
    genre.delete()
    return redirect("/genres")
````

As we did with edit, let's update the detail template so we can easily access the delete action.

<strong>view_genres.html</strong>
````HTML
<h1>{{ genre.name }}</h1>
<a href="{% url "edit_genre" genre.id %}">Edit genre</a>
<a href="{% url "delete_genre" genre.id %}">Delete genre</a>
<br>
<a href="{% url "home" %}">Back to Hollywood</a>
<a href="{% url "genres" %}">Back to Genres</a>
````

##Recap: Basic Django App
Congratulations! You made a Django project. It's simple, but captures the functionality that powers most applications you use on the web and in mobile apps.

You'll start to notice routes just like the ones you created all over the web.

<strong>urls.py</strong>
````Python
urlpatterns = patterns('',
    url(r'^genres/$', 'hollywood.views.genres', name='genres'),
    url(r'^genres/new/$', 'hollywood.views.new_genre', name='new_genre'),
    url(r'^genres/(?P<genre_id>\w+)/$', 'hollywood.views.view_genre', name='view_genre'),
    url(r'^genres/(?P<genre_id>\w+)/edit/$', 'hollywood.views.edit_genre', name='edit_genre'),
    url(r'^genres/(?P<genre_id>\w+)/delete/$', 'hollywood.views.delete_genre', name='delete_genre'),
)
````
##Mission Part II
* Add edit functionality for movies and actors. [Essential]
* Guess what? Add delete functionality for actors and movies! [Essential]

##Digging into Forms
From this point, we'll be looking at the blog project we made earlier. You should have models BlogPost, Author, Comment, and Tag.

##Django Forms API
Django forms can be thought of in different sections:

* <em>Widgets</em>: A class responsible for what HTML is actually outputting to the page.
* <em>Fields</em>: A class responsible for rendering and validating an input.
* <em>Forms</em>: A collection of Fields
* <em>Form assets</em>: The CSS and JS required to correctly render the form

##Form objects
So far, we have only looked at ModelForm objects. But Django allows you to create non-model forms as well using the base Form class.

Django form definitions look a lot like our model definitions, but instead of adding model fields, we are adding form fields.

<strong>forms.py</strong>
````Python
from django import forms
from blog.models import Author

class CommentForm(forms.Form):
    author = forms.ModelChoiceField(queryset=Author.objects.all())
    comment_body = forms.CharField()
````

##Displaying our forms
<strong>urls.py</strong>
````Python
url(r'form/$', 'writers.views.my_form_view', name='form_view'),
````


<strong>views.py</strong>
````Python
from blog.forms import CommentForm

def my_form_view(request):
    data = { "comment_form": CommentForm() }
    return render(request, "my_form.html", data)
````

<strong>my_form.html</strong>
````HTML
<form method="POST">
    {% csrf_token %}
    {{ comment_form }}
    <input type="submit" value="Submit comment" />
</form>
````

##Customizing form layout
Forms have no special layout by default (have a look at the html on your page). Instead you can use some helper functions to format your forms. Try each of the following on your comment form.

* <code>{{ my_form.as_p }}</code>
* <code>{{ my_form.as_ul }}</code>
* <code>{{ my_form.as_table }}</code>

You can also loop over a form's fields individually to print them out.

````HTML
<ol>
    {% for field in form %}
        <li>
            {{ field.label_tag }}
            {{ field }}
        <li>
    {% endfor %}
</ol>
````

##Saving non-model forms
When we were working with model forms, all we had to do to create or update an object was call <code>form.save()</code>. But what about with non-model forms?

Custom forms aren't related to a model, so they have no concept of saving a model object.

But, we still have access to the form (with the form data)

And we still know how to create Comment objects

<code>Comment.objects.create(body="SOME TEXT", author=SOME_AUTHOR)</code>

So let's just fill in our <code>create</code> call with data from the form.

##Extracting form data
If you inspect your form variable, you will see that once forms are validated, they have access to an attribute <code>cleaned_data</code>

<code>form.cleaned_data</code> is just a dictionary. The keys are the field names you defined in your form class. The values are the data being submitted.

So instead of calling <code>form.save()</code> we can extract each of the form fields and use them as we wish. In this case, to create a comment.

````Python
def my_form_view(request):
    data = { "comment_form": CommentForm() }
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            author = form.cleaned_data['author']
            body = form.cleaned_data['comment_body']
            Comment.objects.create(author=author, body=body)
    else:
        return render(request, "my_form.html", data)
````

##Validating input
Depending on the exact Field object chosen some validation is automatic. For example, <code>EmailField</code> and <code>URLField</code> will ensure the input matches the required format for those types of data.

More common validation is provided through arguments to the Field constructor.

* All fields take a <code>required</code> argument (e.g., <code>forms.CharField(required=False)</code>). Fields are required by default!
* CharFields take <code>max_length</code> and <code>min_length</code> arguments

Check the documentation when using a field to see if it provides validation functions for your specific needs.

##Displaying errors
By default, Django outputs the errors for each Field between the label and input of the Field. The errors are in an unordered list with a class of <code>errorlist</code>.

To change the error layout we need to do a custom form layout.
````HTML
<form method="POST">
    {% csrf_token %}
    <ul>
        {% for field in form %}
            <li>
                {{ field.errors }}
                {{ field.label_tag}} {{ field }}
            </li>
        {% endfor %}
    </ul>
</form>
````

##Custom validators
Sometimes, the provided validation functions aren’t enough.

Every Field accepts a validators argument. It’s a list of functions to call with the provided input.

Custom validators take a single argument, the user’s input.

They should either run silently, with no <code>return</code> statement, or raise a <code>ValidationError</code> if input is bad

<strong>forms.py</strong>
````Python
def no_politics_validator(value):
    if re.match("democrat|republican|obama|congress", value) is not None:
        raise ValidationError("You can’t talk about politics on this blog")

class CommentForm(forms.Form):
    author = forms.ModelChoiceField(Author)
    comment_body = forms.CharField(validators=[no_politics_validator])
````

##Subclassing forms
````Python
class MyBaseForm(forms.Form):
    field1 = forms.ModelChoiceField(YourModel)
    field2 = forms.CharField()

class MyOtherForm(MyBaseForm)
    # gets field1 and field2 from MyBaseForm
    # can have additional fields of its own
    another_field = forms.BooleanField()
````


##Mission Part III
* Read about the [built-in form fields] that Django makes available, then make forms with the appropriate form fields for each model in your blog app. [Essential]
* Build out the create action for each of your models (route, view, template). Instead of using a ModelForm, create your own. [Essential]
* [Read more] about the arguments you can pass to your form fields. Based on your model's defined fields, add some of these field arguments as appropriate. E.g., if a field on your model is not required, or has a min or max length, your form fields should specify this. [Essential]
* Write a custom validator for your blog. Add error display to your forms. Make some errors and see what happens.
* Read more about [custom validators]. [Extra]

* Do the [Django Tutorial], parts 1-4 if you have not yet. It is similar to what we've done in class, but goes into more detail on some subjects than we have and explains things slightly differently. [Essential]

* Learn more about [Django models]. There are more options that we haven't covered, and a lot more detail on what's possible. [Essential]

* Become a query expert: [Extra]

	* [Querying basics]: mostly a review of what we've covered in class
	*See the full [QuerySet API reference]. This covers more than what we've done in class, but will give you more powerful ways to query your models.

* Read about (and apply) formsets and form widgets. Also try loading multiple forms on the same page and submitting them. [Extra]

If you are still wrapping your head around what we've talked about so far with basic Django apps, take our blog from today and flesh it out with the full index, create, detail, edit, and delete functionality for each model. [Extra]

Still want more practice? Make an online bookselling application called Zambezi. As a book retailer, you will need to keep track of your books and key information about them. Your models should include (but are not limited to): Book, Genre, Author. You will also have a Customer model. As the application manager, you should be able to add books to a customer's recommended book list. You will be using both many to many and many to one relationships. [Extra]


If you don't think you need to practice that anymore, try making a non-CRUD / resourceful app (e.g., one that doesn't just use index, create, detail, edit, and delete views). Try turning a game of your choosing into a Django app. Think about how users will make decisions in your game--will they be presented with different links for different options? will you use non-model forms for user input? How will you abstract your functionality to make your views and templates flexible and reusable? [Extra]

Create a contact form that includes a field for users to input their email addresses. When users submit the form, they should get an email confirmation.

Sending mail from Django is straightforward using the built-in <code>send_mail</code> function: [Extra]

````Python
from django.core.mail import send_mail

    send_mail("Subject",
            "Message",
            "from@example.com",
            ["to@example.com"]
    )
````
It's up to you to figure out where / how to use this function (there is more than one answer).

[app flow]: img/app_flow.png
[app flow with models]: img/app_flow_all.png
[project cheat sheet]: https://github.com/rocketu/django-orm
[hollywood site map]: img/hollywood_site_map.png
[app flow 3]: img/app_flow3.png
[app flow 4]: img/app_flow4.png
[built-in form fields]: https://docs.djangoproject.com/en/dev/ref/forms/fields/#built-in-field-classes
[Read more]: https://docs.djangoproject.com/en/dev/ref/forms/fields/#core-field-arguments
[custom validators]: https://docs.djangoproject.com/en/dev/ref/validators/
[Django tutorial]: https://docs.djangoproject.com/en/1.6/intro/tutorial01/
[Django models]: https://docs.djangoproject.com/en/dev/topics/db/models/
[Querying basics]: https://docs.djangoproject.com/en/dev/topics/db/queries/
[QuerySet API reference]: https://docs.djangoproject.com/en/dev/ref/models/querysets/