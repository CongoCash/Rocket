Django: Users and AJAX
======================

##The User Model
Django comes with a built in application called <code>auth</code> that you can use right out of the box. It has all of the basic functionality of signing up, logging in, and logging out.

It looks something like you see below:
````Python
class User(models.Model):
    username = models.CharField(_('username'), max_length=30, unique=True,
        help_text=_('Required. 30 characters or fewer. Letters, numbers and '
                    '@/./+/-/_ characters'),
        validators=[
            validators.RegexValidator(re.compile('^[\w.@+-]+$'), _('Enter a valid username.'), 'invalid')
        ])
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=30, blank=True)
    email = models.EmailField(_('email address'), blank=True)
    is_staff = models.BooleanField(_('staff status'), default=False,
        help_text=_('Designates whether the user can log into this admin '
                    'site.'))
    is_active = models.BooleanField(_('active'), default=True,
        help_text=_('Designates whether this user should be treated as '
                    'active. Unselect this instead of deleting accounts.'))
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)
````

###Why the user model is special
Having users is great. It's probably the most common feature across web applications.

But, the Django user model is important for more than just that convenience. Django provides a number of additional features that depend on the user model. These features include groups, permissioning, signing into the admin, and more.

Because of this, and the uniqueness of users, it's important to remember that you can only have one user model per project.

###History of the user model
The user model had remained mostly static up until recently where a refactor was done to make the User model extensible.

Previously if you wanted to add custom fields to this user model you'd have to make your own <code>UserProfile</code> model that related to this one.

What that means is that you had two separate tables in your database, one for the Django Auth User model and one for your own, which would store a few fields like phone number.

This user model is also heavily bent towards English names. Having a first and last name field is not friendly to a large part of the world's population whose names don't abide by this format.

###What's next?
Now that migrations are part of the core Django library, the core developers are actually starting to make small changes to the User model that they haven't been able to for a long time.

Some specific changes include increasing the max length of the email field, which was one of the most common issues with the built-in User model people had.

Be on the lookout for a few more changes in the next release of Django, which will help fix some of the legacy issues with the User model.

###User admin
Out of the box, the Django Admin has the User model registered. The actual User Admin is a bit customized and is set up so that when you add a new user, at first you only enter their username and password first. Afterwards, you get access to edit the rest of the fields.

The admin is great for first creating users to test with as well as staff users, who should have access to use the admin. This is what the <code>is_staff</code> flag is used for.

You can also see when people joined by default and change their password if need be.

Also note the "History" button, which shows you the Django Admin Log for the particular model you're looking at. It's a great way to keep track of whose doing what in the Admin if you have multiple staff users.

###Permission & Groups
Staff users can be assigned permissions, so that they only have access to create, edit, or delete different models. When a staff user is logged in, they will only see links to the Admin sections that they've been given permissions for.

For small sites this permissioning system works great, but sometimes at scale it can fall apart because not all permissions are just based on models.

Groups are just predefined sets of permissions. For example you may have a group called "Blog Authors", where all users who belong to that group are allowed to manage the Blog section of the website.

###Auth forms
Django has several built in forms in it's auth application that we can use to get user functionality up and running quickly.

Feel free to take a look at <code>django.contrib.auth.forms</code> for the entire list or Django's documentation.

For practice today, let's continue with our playing card project.

###Sign up
First, let's set up the sign up form so people can sign up for our site.

<strong>urls.py</strong>
````Python
url(r'^register/$', 'cards.views.register', name='register')
````

<strong>views.py</strong>
````Python
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("profile")
    else:
        form = UserCreationForm()

    return render(request, "registration/register.html", {
        'form': form,
    })
````
Our register view uses Django auth's built in <code>UserCreationForm</code>. This is a custom model form that has a couple additions:

* Checks the confirm password matches the first password.
* Checks that this username isn't already being used by someone.

Now let's create our template. Note, it's common django practice to pull all auth related templates in a folder called <code>registration</code>.

This is a very straightforward template including a form as we've seen before.

<strong>registration/register.html</strong>
````HTML
{% extends "base_template.html" %}

{% block content %}
    <form method="post" action=".">
        {% csrf_token %}
        {{ form.as_p }}

        <input type="submit" value="Submit">
    </form>
{% endblock %}
````
Now let's try it out and sign up with a user. We can check in our admin that a new user was created.

###Login form
How about if we've already created a user and we just want to log back in? There's a built-in form for that too. There's actually already a view defined for us, we just need to hook up the url and a template.

<strong>urls.py</strong>
````Python
url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
````

<strong>registration/login.html</strong>
````HTML
{% extends "base_template.html" %}

{% block content %}
    <form method="post" action=".">
        {% csrf_token %}
        {{ form.as_p }}

        <input type="submit" value="Log in">
    </form>

    <p>Not member? <a href="{% url 'register' %}">Register!</a></p>
{% endblock %}
````

This again, is a pretty straightforward template for a form. We've added a link to the sign up page in case our user hasn't registered yet.

Now if we try to login, we get a 404 error because we're sent to <code>/accounts/profile</code>. This is the default login redirect URL.

We want the login page to go to our profile page, which just lives at <code>/profile</code>.

To change this let's set <code>LOGIN_REDIRECT_URL = 'profile'</code> in our settings.py

Now if we login we're redirected to the proper page.

###request.user
We've now got the ability for users to sign up and login to our website.

In all of our views we have access to the request object, which always has a user property whether a user is signed in or not.

With <code>request.user</code> we're able to do a bunch of things, including checking if the user is currently logged in, if they're an active user, and access any properties about the user.

###Auth in template
One of the most common use cases for using the user instance in the template is printing out a greeting.

* In our profile.html, let's change "Player 1" to <code>user.username</code>.
* Note that in your template, you don't have to do <code>request.user</code>. The template just understands the variable <code>user</code>. In your views you will use <code>request.user</code>.
* Username is just a field on the user model, we can access it like we would any other variable in our template.

###Logout
We've got Sign up + Login, logically the next feature we're missing is Logout.

Like login, this view comes standard with Django and we just need to hook up the pieces.

<strong>urls.py</strong>
````Python
url(r'^logout/$', 'django.contrib.auth.views.logout', name='logout'),
````

<strong>registration/logged_out.html</strong>
````HTML
{% extends "base_template.html" %}

{% block content %}
    <p>Come back soon!</p>
{% endblock %}
````
Navigate to the logout page in your browser. Check that if you go back to the profile page, your username no longer appears.

###Auth in template part 2
So now we have pages to register, login, and logout. If a user is currently authenticated, we only want to show them the logout link in the nav and if they're not currently authenticated then we want to show them the login and register links.

We can easily pull this off in the template with an if statement.

Put the follow code inside of <code>base_template.html</code> at the end of the navigation div.

````HTML
<span style="float:right;">
    {% if user.is_authenticated %}
        <a href="{% url 'logout' %}">Logout</a>
    {% else %}
        <a href="{% url 'login' %}">Login</a> | <a href="{% url 'register' %}">Register</a>
    {% endif %}
</span>
````
If the user is authenticated, then we just display the Logout link, else we display both the login and register links.

###Auth in view
We also have access to the user object in the view. Let's say we actually don't want to show the profile page at all if a user is not logged in.

We have write the following code in the view, which will redirect users not logged in to the login page.
````Python
def profile(request):
    if not request.user.is_authenticated():
        return redirect("login")

    return render(request, 'profile.html', {})
````

Test it out. Make sure you've logged out first then try to go the profile page. <code>request.user.is_authenticated()</code> returns False and you're redirected to the login page.

###Auth as decorator
As mentioned previously, this kind of code we just saw checking for a logged in user in a view is something we'd probably want to reuse.

Django's auth library has prepackaged a decorator called <code>login_required</code>, which does just that.

First we need to put this in our <code>settings.py</code> to configure where our login url is located: <code>LOGIN_URL = 'login'</code>

Remove the code we just wrote from our view and instead use the decorator as seen below. Note, you will need to import the decorator.

````Python
@login_required
def profile(request):
    return render(request, 'profile.html', {})
````

###Customizing user form
The built-in Django <code>UserCreationForm</code> is missing one of the most important fields when a user is first signing up: email.

Let's build upon this form to add email as a field user's need to first fill out when they sign up.

First we need to create our own form, which will inherit from Django auth's.

1. Create a <code>forms.py</code> in our cards application.
2. Put the following code in <code>forms.py</code> to create our own form which inherits from Django's but includes an email field:

````Python
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class EmailUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")
````

Now, in our <code>register</code> view, we need to use this new form instead of Django's built in one.

After you change <code>UserCreationForm</code> to <code>EmailUserCreationForm</code> try signing up. We should now see an email field.

To test that we are saving the email correctly, let's print the email out in <code>profile.html</code> as well.

````HTML
<p>Your email address is {{ user.email }}</p>
````

##Mission Part I
* Only show the "Profile" page link if the user is currently authenticated. [Essential]
* On the profile page, also display the user's <code>last_login</code> datetime. [Essential]
* Display the user's username, if logged in, up in the right hand nav. Set this to be the new link to the profile page. [Essential]
* If the user is logged in and a staff user, put a link in the top right hand nav to the Django admin. [Extra]
* On the profile page, also display how long ago the user registered via <code>date_joined</code>. Hint: template filter. [Extra]
* Let's extend our user form to also let the user enter their First and Last names when registering. These are fields already on the User model called <code>first_name</code> and <code>last_name</code>. [Extra]


###Users: Customizing Relationships
Often, user's forget their password and need to retrieve it from your site. Now that we're saving emails for our users. Let's see how we can hook up this functionality.

Per the running theme, Django also provides this out of the box for us. The forgot your password workflow is a bit more involved, so let's go through it piece by piece.

First, let's set up the following urls:

````Python
url(r'^password_reset/$', 'django.contrib.auth.views.password_reset', name='password_reset'),
url(r'^password_reset/done/$', 'django.contrib.auth.views.password_reset_done', name='password_reset_done'),
url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
    'django.contrib.auth.views.password_reset_confirm',
    name='password_reset_confirm'),
url(r'^reset/done/$', 'django.contrib.auth.views.password_reset_complete', name='password_reset_complete'),
````
Resetting your password has 4 main steps (represented by each of the views).

1. A user enters their email address for the account they want to be reset. This view then sends them an email.
2. The user is redirected to an "email sent" page.
3. From the email, the user gets a unique link to click, which brings them to a "Set Your New Password" page on the website. This let's them change the password for their account.
4. The user is redirect to a "your password has successfully been changed" page afterwards.

All we need to do is set up the appropriate templates, Django has us covered with its views that we already added.
<strong>registration/password_reset_form.html</strong>
````HTML
{% extends "base_template.html" %}

{% block content %}
    <form method="post" action=".">
        {% csrf_token %}
        {{ form.as_p }}

        <input type="submit" value="Submit">
    </form>
{% endblock %}
````

<strong>registration/password_reset_done.html</strong>
````HTML
{% extends "base_template.html" %}

{% block content %}
    <p>Email with password reset instructions has been sent."</p>
{% endblock %}
````

<strong>registration/password_reset_confirm.html</strong>
````HTML
{% extends "base_template.html" %}

{% block content %}
    {% if validlink %}
        <form method="post" action=".">
            {% csrf_token %}
            {{ form.as_p }}

            <input type="submit" value="Submit">
        </form>
    {% else %}
        <p>Password reset failed</p>
    {% endif %}
{% endblock %}
````
<strong>registration/password_reset_complete.html</strong>
````HTML
{% extends "base_template.html" %}

{% block content %}
    <p>Password reset successfully</p>
    <p><a href="{% url 'login' %}">Log in</a></p>
{% endblock %}
````

###Setting up Email
We're almost ready to try out our reset password workflow. The last bit is actually setting up our Django app to send emails.

For the point of development and sometimes even small applications you can just use a gmail email address for sending out emails.

At scale, you'd want to use a service, such as Mailgun or Mandrill.

Put the follow settings in your <code>settings.py</code> replacing the appropriate information with your gmail account.

<strong>CAUTION: Never push sensitive information to your github</strong>
````Python
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'your_email@gmail.com'
EMAIL_HOST_PASSWORD = 'your_password'
EMAIL_PORT = 587
DEFAULT_FROM_EMAIL = 'your_email@gmail.com'
````

###Emailing users
Sending out emails to users once you have emails working is trivial. There's a few different ways to send emails but let's take a quick look at how to send an email to the logged in user.

Let's say after a user first registers, we want to send them a welcome email. We could do the following:

````Python
user = form.save()
user.email_user("Welcome!", "Thank you for signing up for our website.")
````
Try registering with an email address you own and see the email you get.

What if we want to actually send a much more detailed email that has some HTML styling?

We can actually use HTML and input variables into our message!

````Python
text_content = 'Thank you for signing up for our website, {}'.format(user.username)
html_content = '<h2>Thanks {} for signing up!</h2> <div>I hope you enjoy using our site</div>'.format(user.username)
msg = EmailMultiAlternatives("Welcome!", text_content, settings.DEFAULT_FROM_EMAIL, [user.email])
msg.attach_alternative(html_content, "text/html")
msg.send()
````
Note above that we give it a text and a html version.

Try registering again with an email address you own and see the new and improved email you get.

If you've run out of email addresses, there's a trick you can use. Sign up with your_email+1@gmail.com. Gmail will know to forward the email to your regular address. Continue to keep increase the number as you need to for testing.

###Custom users
What happens if we want to add a field to the user model? We can create our own User model, which inherits from Django's.

Let's say we want to store our user's phone number. In our cards application, let's put in the following model:
````Python
class Player(AbstractUser):
    phone = models.CharField(max_length=12, help_text="Format should be: 650-111-2222")
````
Then in our <code>settings.py</code> we need to put the following: <code>AUTH_USER_MODEL = 'cards.Player'</code>. This setting must be specified. As we discussed earlier, there can only be one User model and Django must know what that model is for password reset, admin, etc. to function correctly.

We now can create a <code>makemigrations</code> and run it to create our new user model. It will have all of the fields it did before, plus a phone field.

We've told Django that Player is our user model, so <code>request.user</code> will now refer to an instance of a Player.

Now, we just tell our <code>EmailUserCreationForm</code> it should be using our new Player class.

You'll notice we had to override the <code>clean_username</code> method. This is because Django's built-in form makes the assumption that you're using it's built-in model.

````Python
class EmailUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = Player
        fields = ("username", "email", "password1", "password2")

    def clean_username(self):
        # Since User.username is unique, this check is redundant,
        # but it sets a nicer error message than the ORM. See #13147.
        username = self.cleaned_data["username"]
        try:
            Player.objects.get(username=username)
        except Player.DoesNotExist:
            return username
        raise forms.ValidationError(
            self.error_messages['duplicate_username'],
            code='duplicate_username',
        )
````
###FYI - Django Registration
For the sake of not reinventing the wheel, some of what we've seen today is common user functionality that many Django developers have implemented over and over again.

There is a Django library, called django registration, which has code and functionality for some of what we've done today as well as several other common tasks around user authentication. It's fairly popular in the Django community, but not required.

Here's the [documentation]

###Relating a user
We have Players! Now we can actually tie data in our database to our Player model.

Our Player model, is just like any other Django model meaning we can relate another model to it using a ForeignKey or ManytoMany.

Let's make a really simple modified version of the card game war, to see how we can keep track of wins, loses, and ties.

###WarGame Model
First we'll need to create our model that's going to keep track of the matches. It will need to be related to our user model as well as have a field for the outcome of the match.

Let's add the following model to our <code>models.py</code> and migrate our database.
````Python
class WarGame(models.Model):
    LOSS = -1
    TIE = 0
    WIN = 1
    RESULTS = (
        (LOSS, "loss"),
        (TIE, "tie"),
        (WIN, "win")
    )

    result = models.IntegerField(choices=RESULTS)
    player = models.ForeignKey(Player)
````
Notice we're using a choice field for the result and have a ForeignKey to our Player model.

###WAR!
The rules for our game of war are going to be very, very simple.

* Every round of WAR, we're going to pick one random card for the computer and one random card for the player.
* If the player's card is a higher rank than the computer's, they win. If it's the same, they tie. If it's lower the player loses.
* Aces are considered the highest in our game.

Let's see how we'd set up this page in our game.
1. Set up our url
````Python
url(r'^war/$', 'cards.views.war', name='war'),
````
2. Set up our view
Set up our view. We get 2 random cards and compare the cards to get the result. With the result we create a new WarGame record for the user currently logged in.
````Python
@login_required()
def war(request):
    random_cards = Card.objects.order_by('?')
    user_card = random_cards[0]
    dealer_card = random_cards[1]

    result = user_card.get_war_result(dealer_card)
    WarGame.objects.create(result=result, player=request.user)

    return render(request, 'war.html', {
        'user_cards': [user_card],
        'dealer_cards': [dealer_card],
        'result': result
    })
````

We now need to create the method on our Card model, which compares itself with another card.

````Python
def get_ranking(self):
    rankings = {
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9,
        'ten': 10,
        'jack': 11,
        'queen': 12,
        'king': 13,
        'ace': 14
    }
    return rankings[self.rank]

def get_war_result(self, card_to_check):
    my_ranking = self.get_ranking()
    card_to_check_ranking = card_to_check.get_ranking()
````

We've created one function, which converts each of our cards into an integer for quick comparison.

And we've created another function which compares those integers and returns us -1, 0, or 1 to represent our result.

Try it out in your Django shell!


##Mission Part II
* Edit our register welcome email to actually use their first and last name instead of username. [Essential]
* Have the register welcome email have the datetime of when they exactly joined. [Essential]
* On our blackjack page, send the user an email every time they're dealt an Ace. It should use their username or name in the email and say they got an Ace and also what the suit of that Ace was. [Essential]
* Have our EmailUserCreationForm allow the user to save a phone number. [Essential]
* Show that phone number on their profile page. [Essential]
* Add a <code>war.html</code> template. Use our <code>includes/hand.html</code> snippet to display the user card and the dealer card. Check the Django docs for how to pass variables to the <code>include</code> tag. [Essential]
* In the template, let the user know if they've won, lost, or tied. [Essential]
* Have your profile view pass in the list of WarGame records for the current user: <code>WarGame.objects.filter(player=request.user)</code> [Essential]
* Loop over that list of game records in <code>profile.html</code> and show the <code>game.get_result_display</code> of each. You should see a list of "tie", "loss", "win" down your profile page. [Essential]
* After a user has played 10 games, send them an email saying thanks for playing! [Extra]
* On the user's profile page, show their current win-loss-tie record and how many times they've played. [Essential]
* Create a leaderboard that shows the top 5 players with the highest win/loss record. You'll need to create a few more players and play a few games to test this out. [Extra]
* Show their "score" by adding up their wins, losses and ties. If a user has 5 wins, 3 losses, and 2 ties their score will be 2. Hint: Use django's Count method in your Queryset. [Essential]
* Have the user model save a "balance". When a user plays WAR they bet a certain amount of money and either win or lose that amount. They get a default balance when they first sign up. [Extra]
* Create a form that allows people to add money to their balance. This can just let someone arbitrarily pick what they want to add to their balance. [Extra]
* Look at the documentation for django-registration and set up the two-factor email verification for a user on your website. [Extra]
* Read the docs and integrate Django's permissioning. Up to you how. Some ideas: maybe everyone can play War, but only some users can play other games. [Extra]
[documentation]: http://django-registration.readthedocs.org/en/latest/

##AJAX and Django

###Integrating AJAX with Django
Week 2 we learned AJAX, and how to use it to talk to third party APIs. Today we're going to learn how to do the same with our Django applications. In fact, our Django applications will serve as APIs.

How? Let's think about...

<strong>... what is an API?</strong>

Wikipedia tells me an API is an Application Programming Interface. That's sort of nebulous. The APIs you have heard of so far are for big web services, like Google, Facebook, etc. But people also talk about writing APIs in Django and Rails, about Java APIs, about APIs for everything, really.

###APIs: the simple explanation
An API is just a way to interact with an application. The same as how your keyboard and mouse are ways that you interact with your computer: you click and tap and your computer takes some actions. You do certain things with an API, and it'll do things in the application, e.g., make some data, send you some data, whatever the creators decide you are allowed to do.

For most of the APIs we talk about, the "action" that we take is going to a URL. So, we go to one URL and we get a bunch of data, we go to another URL and it makes some data for us, we go to a different URL and it deletes some data for us.

For example, a (simplified, made-up) API call we would make to Rotten Tomatoes might look like: http://api.rottentomatoes.com/search=Batman and then, boom, the API sends us a list of movies about Batman.

###Writing APIs with Django
APIs aren't just some complicated thing big companies make--we can make them ourselves with Django. It works exactly the same way, but we get to control what URL we are going to and what those URLs do. So, we could make an API at http://bayleeiscool.com that understands the command "random_baylee_fact". Then if you were to go to http://bayleeiscool.com/random_baylee_fact the API would send you back a random fact about Baylee.

In a way, every website you go to is using an API. When you go to a URL in your browser, like google.com, you're taking an action (going to the URL), that sends a command, that loads the the Google search page.

The same thing happens with your Django applications: you go to a certain URL, and the Django application gives you back some pretty HTML and CSS. Now, instead of just sending full HTML templates and CSS, we are going to learn to return JSON and HTML snippets. The premise is the same: go to URL, Django does stuff, Django sends you back some stuff.
APIs are pretty ubiquitous, which can make it difficult to figure out what exactly they are.

###APIs: Some definitions
First, we are only really talking about web APIs here: APIs that you work with through URLs.

Here are some terms we will use to talk about web APIs:

* Endpoint: an API endpoint is just a specific URL and HTTP method that controls an API. It is one of the URL "actions" that we talked about earlier
* Client: something that uses an API. When you go to Google Maps on your computer, your browser is a client of the Maps API. When you use the Google Maps app on your phone, that app is a client. When you use some other service on the internet that uses Google Maps, that service is a client.

###Some simple examples
Before we dive into our main example for the day, let's think of some cases where AJAX could be useful.

<strong>Todo List</strong>

Imagine you have a todo list application. You have a Todo model, and it saves all a user's todos. For a user to look at their todos, we could structure this like the basic Django apps we first learned: a list view with all the todos, links to detail pages, and links from there to edit or delete.

But all that is overkill for a simple todo list.

It would be far more usable if there was just a single input field under all our existing todos, where we could input new todos. They should immediately get added to our todo list, instead of us refreshing the entire page. We should be able to remove todos by just clicking an 'x' icon next to them. They should get immediately removed without waiting for us to refresh the entire page.

<strong>Writing comments</strong>

Similarly, imagine we want to leave a comment on an article we just read. We should just be able to write the comment and hit submit. If the page doesn't refresh, users are left wondering if their comment saved. If the page does refresh, that's way too much waiting time for a simple comment add. Instead, we can update the page immediately with JavaScript, and then use AJAX to run to Django and save the comment.

<strong>Long-running tasks</strong>

Imagine that when users sign up for your site, you have an 'Invite your friends' section. Users put in 15 friends' email addresses and then hit 'Invite'. If they had to wait for all 15 emails to send, they might be waiting for awhile. But you want them to move on quickly and start playing with your app, not waiting. So you pop up a message in a little green box telling them 'Success! Emails sent!', send an AJAX request to Django to send the emails, and let the user continue on their way.

###Pokemon App!
We're going to be using the [Pokemon API] to use JSON to create models and save them in our database to retrieve later. Let's start off with our models.

````Python
class Team(models.Model):
    name = models.CharField(max_length=30)


class Pokemon(models.Model):
    name = models.CharField(max_length=30)
    image = models.URLField()
    pokedex_id = models.PositiveIntegerField()  # this is the ID from the pokeapi
    team = models.ForeignKey(Team)
````

If you're not sure what Pokemon to create, create a Bulbasaur!
````Python
Pokemon.objects.create(name='bulbasaur',
                       pokedex_id=1,
                       image='http://pokeapi.co/media/img/1383571573.78.png',
                       team=SOME_TEAM
                       )
````

###Write your views
Let's add a view that will return all our Pokemon. When we hit this view with AJAX, it'll give us a JSON object that contains all our Pokemon.

<strong>views.py</strong>
````Python
def all_pokemon(request):
    pokemon = Pokemon.objects.all()
    data = serializers.serialize('json', pokemon)
    return HttpResponse(data, content_type='application/json')
````
<code>serializers.serialize</code>: Django [provides] a framework that "translates" Django models into other formats. Simply pass in the desired format for your first parameter, and the data to be serialized as the second.

<code>return HttpResponse()</code>: This is the data we'll receive back from our Ajax request. The first parameter is our newly serialized object, and the second specifies that it is JSON.

###Create a URL and make a GET Request
Write URL for your new view.

````Python
url(r'^all_pokemon/$', 'pokemon.views.all_pokemon', name='all_pokemon'),
````
If you navigate to <code>0.0.0.0:8000/all_pokemon</code>, you should see a JSON response that includes all your Pokemon. Now, instead of navigating there with our browser, we can...

<strong>...make an AJAX request to the url we just created:</strong>

* Create a new HTML template and JS file. Load jQuery and use Django's <code>{% static %}</code> to load your JS file.
* Create a new home / index url and view to point at this template.

<strong>index.js</strong>
````Javascript
$.ajax({
    url: '/all_pokemon',
    type: "GET",
    success: function(data) {
        console.log(data);
    }
})
````

###That's it!
Now when you go to your home URL, you should be making an AJAX call that gets all your pokemon. Just like that, we are using Django to respond to AJAX requests. You constructed a URL and view (all_pokemon) the same as always. Your view returned some information, as it normally does, but instead of rendering HTML, you just returned some JSON.

You just wrote a simple Django API of your own.

This example is trivial because we could just pass our pokemon data in the home view itself, but the point is to show that you can make AJAX calls to your Django API, from within your Django project.

###Formatting Our Data
<code>json.dumps()</code> is another way to serialize an object into a JSON string, but gives us more control over formatting, which lets us make our JSON more readable.

Currently, our object looks like this:

````Javascript
{
    pk: 1,
    model: "pokemon.pokemon",
    fields: {
        pokedex_id: 25,
        image: "/media/img/25.png",
        name: "Pikachu",
        team: 1
    }
}
````

Right now all of our important information is inside of the "fields" object, which maps to our Pokemon model's fields.

If we wanted this Pokemon's name, we'd have to write something like <code>data[1].fields.name</code>. We also have a "model" key, which we don't really need either.

Rather than using serializers.serialize to magically construct our JSON, we can actually loop over all of our Pokemon objects, put the relevant information into new objects, and use json.dumps() to make a new JSON string with our freshly-made cleaned-up information.

###json.dumps()
Create a new url that points to this view.

````Python
def pokemon_data_dump(request):
    pokemon_objects = Pokemon.objects.all()
    collection = []
    for pokemon in pokemon_objects:
        collection.append({
            'name': pokemon.name,
            'image': pokemon.image,
            'pokedex_id': pokemon.pokedex_id,
            'team': {
                'id': pokemon.team.id,
                'name': pokemon.team.name
            }
        })
    return HttpResponse(
                json.dumps(collection),
                content_type='application/json'
           )
````

Step by step walkthrough:

* Get all of our Pokemon objects and set them to pokemon_objects.
* Create a collections array.
* Loop over pokemon_objects and create a new object for each Pokemon, and then append the new object to collection.
* Pass collection as a parameter to json.dumps().

##Mission Part III
* Create a new URL and view - "pokemon_simple_data". Use <code>json.dumps()</code> rather than <code>serializers.serialize()</code>.
* For team information, instead of passing a nested team object, just return the team name.
* Add an 'id' property that is set to a Pokemon's 'pk' so that we can easily access specific Pokemon objects.
* On your home page, add ajax calls to pokemon_data_dump and pokemon_simple_data. You should be able to see the different types of data they return.
* Read more about <code>json.dumps()</code> in the [json dumps documentation] and learn how to further format your JSON.
Going forward, you can use whichever method you prefer.

###Making a POST Request
If you want to create or edit models, you'll need to send information to your server with a POST request.

````Javascript
var pokemonData = {
    pokedex_id: 25,
    image: "/media/img/25.png",
    name: "Pikachu",
    team: {
        name: "Random Team",
        id: 1
    }
};

pokemonData = JSON.stringify(pokemonData);

$.ajax({
    url: '/new_pokemon/',
    type: 'POST',
    dataType: 'json',
    data: pokemonData,
    success: function(response) {
    },
    error: function(response) {
    }
});
````

* <code>pokemonData</code>: This is the information we'll be POSTing to the server.
* <code>JSON.stringify()</code>: Converts pokemonData to JSON.
* Inside our AJAX call, we have a <code>data</code> option, which we set to pokemonData. We could also just put the data object here, instead of setting it to a variable first, but that is a bit harder to read.
* <code>error</code>: Both GET and POST requests have error functions. If your request fails, the code here will execute. <code>response</code> is an error message object.

###Handling our POST Request
Using <code>json.dumps()</code> the view would look like

````Python
@csrf_exempt
def new_pokemon(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        pokemon = Pokemon.objects.create(
            name=data['name'],
            image=data['image'],
            pokedex_id=data['pokedex_id'],
            team=Team.objects.get(id=data['team']['id'])
        )
        pokemon_info = {
            'name': pokemon.name,
            'image': pokemon.image,
            'pokedex_id': pokemon.pokedex_id,
            'team': {
                'id': pokemon.team.id,
                'name': pokemon.team.name
            }
        }
        return HttpResponse(json.dumps(pokemon_info),
                   content_type='application/json')
````

Using <code>serializers.serialize()</code>...
````Python
@csrf_exempt
def new_pokemon(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        pokemon = Pokemon.objects.create(
            name=data['name'],
            image=data['image'],
            pokedex_id=data['pokedex_id'],
            team=Team.objects.get(id=data['team'])
        )
    response = serializers.serialize('json', [pokemon])
    return HttpResponse(response,
                        content_type='application/json')
````
Breakdown:

<strong>json.dumps()</strong>
* Check if this is a POST request.
* json.loads() deserializes the data sent in the POST. Basically the opposite of json.dumps().
* Create a new Pokemon object with values from data.

<strong>serializers.serialize()</strong>
* Finally, we serialize our pokemon object.
* serialize() expects an array, so we put pokemon inside of one.

###Cross-site request forgery
Remember how we added <code>{% csrf_token %}</code> to all our Django forms? Now we want to post data without worrying about that.

<code>@csrf_exempt</code>: We aren't saving any particularly important information in this application, so we can add this decorator. If you're deathly afraid of someone ruining all of your Pokemon teams, feel free to add <code>{% csrf_token %}</code> to your HTML. You can read more about CSRF tokens, and using them with AJAX, in the [csrf Django docs].


##Mission Part IV:
* Create the functionality to save you pokemon from an AJAX request inside your new Pokemon app. [Essential]
* Although a "real" Pokemon team can only have six members at a time, for now, let's just add them all to the same team, so you can go ahead and hardcode those values for now. [Essential]
* Once you've done that, create a "new_team" URL and view. [Essential]
* Add a "Get Random Team" button that makes a GET request to pokeapi for six random Pokemon. [Essential]
* Once the user's team has been loaded, add a "Save Team" button. This will create a new team, as well as the Pokemon associated with it. [Essential]
* Depending on how you have set up your relationships (or if you want to go back and change them), you might have one Pokemon belong to one team, belong to many teams, or even just save a "Team" as an array of Pokemon objects that are *not* their own models (i.e. you only have a Team model, and no Pokemon model). [Extra]
* Add delete functionality with ajax to delete teams or Pokemon. [Essential]
* Add a new view that returns pokemon filtered by type [Essential]

##Weekend Mission
Choose from one of the following assignments to work on. Regardless of which assignment you choose, you should have the following features:

* Users should be able to login, reset their passwords, and edit their profiles
* It shouldn't look hideous (e.g., no plain HTML pages)
These projects all make use of 3rd party plugins. You can <code>pip install</code> packages available on [PyPI], and you can get reviews of Django packages on [Django Packages].

####Choice #1: Wanderful
Create a Django app that allows users to store locations they want to travel to. Users should be able to input locations and have them stored in a list. Bonus functionality: allow users to have multiple lists of locations. Use a Django mapping 3rd party app to plot the locations on a map (don't use a JS library). Use HTML5 geolocation to get the user's current location and output how far each stored location is from the present position. It would be great if users could upload photos of each location.

####Choice #2: It's in a Book
Create a Django app that allows users to learn words by reading them in context. Allow users to store words that they want to learn. Use Beautiful Soup to get a bunch of text from articles or books online. When a user clicks on a word in their word list, they should then see the text of an article / book where the word is used. Users should be able to delete words, and move them to a 'learned' list once they've learned a word.

####Choice #2: Movie Mapper
Allow users to store favorite movies and favorite locations. Use one of the IMDB packages available on PyPI to get locations for movies. Users should be able to see a map of their locations, showing movies shot there, and similarly, see a movie and the locations it was shot.

FYI
* Mapping is a common feature on the web. Both Google Maps and its top competitor with developers, Leaflet, have Django plugins you can use without any JavaScript. Think maps are boring or easy? You clearly haven't read [this excellent post].
* Along with maps, you should be aware of HTML5 (and other forms of) geolocation. You don't have to be able to write native mobile apps to take advantage of user location. [This post] explains the options well.
* Web scraping can be a really useful tool. Imagine there is this great site that has information you want to (legally) use, but they don't have an API. For example, a recipe site. The home page always lists the top 10 recipes in the same format, and each recipe page has the same structure (`<h2>` title, `<ul> `for ingredients, `<ol>` for instructions, etc.). How can you get all that data without manually looking at the recipes? Web scraping! Learn about using [Python's xml and requests libraries], which are important libraries you should know about, then maybe learn a simpler way of doing the same with [Beautiful Soup].

[pokemon API]: http://pokeapi.co/
[provides]: https://docs.djangoproject.com/en/dev/topics/serialization/
[json dumps documentation]: http://pymotw.com/2/json/#human-consumable-vs-compact-output
[csrf Django docs]: https://docs.djangoproject.com/en/1.7/ref/contrib/csrf/
[PyPI]: https://pypi.python.org/pypi
[Django Packages]: https://www.djangopackages.com/
[this excellent post]: http://alistapart.com/article/hack-your-maps
[This post]: http://diveintohtml5.info/geolocation.html
[Python's xml and request libraries]: http://docs.python-guide.org/en/latest/scenarios/scrape/
[Beautiful Soup]: http://www.crummy.com/software/BeautifulSoup/