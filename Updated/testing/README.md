Testing
=======================

## What is testing?
We write some simple, straightforward code which tests that our features and functionality behave as we expect.

Simply, you write a test case for each scenario that you want to test and assert that the desired behavior has happened.

This helps make sure that our application is functioning as intended.

Once upon a time, developers wrote untested code, which was shipped off to a QA team, which then created the tests for them. This no longer happens. Developers are expected to write tests for their code.

## Why test?
Testing is perceived by people who don't test as a scary, large time sink, which won't provide as much benefit as the time it will take to implement.

But they're wrong! Testing may take a little bit of an investment up front if you're not familiar with it, but it will produce dividends later on in a project.

So what makes testing great?

* As more code is written for a project and developers come and ago, people will write code, which breaks existing functionality.
* Relying on purely manual testing from developers, product managers, and QA is not good enough.
* Writing tests causes developers to write code that is easily testable, which also means it is easily maintainable.
* If all tests are passing it will give the team more confidence in making changes and releasing those changes to production.
* If the team is more confident, that means they are likely to produce more code and more features instead of being concerned about breaking existing functionality.
* Writing tests often causes you to think about extra use cases, you didn't originally plan for.


## Test Suite Coverage
The "Test Suite" is the collection of all of the tests for the application.

Ideally this is worked on from the start of a project, but late in the project is better than never.

A test suite, ideally, covers 80% or more of the application's code.

Coverage is the idea that the tests cause x percentage of the code to actually be executed when the tests are ran.

We'll see tools in a bit that let us actually figure out what percentage of our code base is covered and how we can improve it.


## Setup Project
Set up the 'cards' project given in the repo.

## Unit Test
A unit test is the smallest case, we'll test for. The name comes from testing a "unit" of code, which is usually a specific function.

Imagine we had the following function, which returns to us the max between number_one and number_two.

````Python
def max(number_one, number_two):
    if number_one >= number_two:
        return number_one
    else:
        return number_two
````

We would want to test this function for 3 different scenarios to check the expected behavior.

* number_one is larger than number_two should return number_one
* number_two is larger than number_one should return number_two
* number_one is the same as number_two should return number_one or number_two (same value)

#### Basic Unit Test
Let's set up our first unit test. Let's create a <code>tests.py</code> file in our cards application where we will put all of our tests.

Put the following code in our new file

````Python
from django.test import TestCase
class BasicMathTestCase(TestCase):
    def test_math(self):
        a = 1
        b = 1
        self.assertEqual(a+b, 2)

    def test_failing_case(self):
        a = 1
        b = 1
        self.assertEqual(a+b, 1)
````

Now run python <code>manage.py test</code> to run your tests!

#### Running the Tests
As you can tell, Django's test command was able to automagically find our test file. It has some logic to look through all of our applications for files or folders prepended with the word <code>test</code>.

Notice also that both of our tests' function names are also prepended with the word <code>test</code>. This is important! This is how Django's test runner discovers our tests.

We noticed from our test suite output that one of the tests failed. Let's remove that test and run the test suite again.

Everything passed! Now let's make some real tests.

````Python
class UtilTestCase(TestCase):
    def test_create_deck_count(self):
        """Test that we created 52 cards"""
        create_deck()
        self.assertEqual(Card.objects.count(), 52)
````

Put this test in and run your tests again to check that it passes.

Notice here that we created a new <code>TestCase</code>. Different <code>TestCase</code>'s can have multiple tests and are a good way to organize and separate tests.

Large codebases can end up with a gigantic test file that is hard to maintain if not properly segmented.

#### Another Unit Test
This time, let's unit test our model's <code>get_ranking</code> function.

We want to create a test, which creates a card and checks that get_ranking returns the expected rank for that card.

````Python
class ModelTestCase(TestCase):
    def test_get_ranking(self):
        """Test that we get the proper ranking for a card"""
        card = Card.objects.create(suit=Card.CLUB, rank="jack")
        self.assertEqual(card.get_ranking(), 11)
````
Notice that this time we made a <code>ModelTestCase</code> to house our new test. Organized!

## Mission: Part I
Your turn to write a few unit tests. Let's test our <code>get_war_result</code> function. There are 3 different outcomes we need to check for! Write a unit test checking each case.

Think about if these tests logically belong under a <code>TestCase</code> we already created or should be part of a new one.

####Reusable Test Code
You may have noticed, we had to create <code>Card</code> objects for each of our tests in <code>ModelTestCase</code>.

Tests have a function you can define, called <code>setUp</code>, which each test will call before it runs. This is where you can put scaffolding code that each test needs to use.

This leads to DRY testing!

````Python
class ModelTestCase(TestCase):
    def setUp(self):
        self.card = Card.objects.create(suit=Card.CLUB, rank="jack")

    def test_get_ranking(self):
        """Test that we get the proper ranking for a card"""
        self.assertEqual(self.card.get_ranking(), 11)
````

Our <code>setUp</code> function is now creating a card, which can be accessed in any test using <code>self.card</code>.

#### Form Tests
Let's say we want to test our form. On our <code>EmailUserCreationForm</code> we've created a <code>clean_username</code> function, which checks to see if a username is already taken. We can write a test that checks to see if the <code>ValidationError</code> is properly raised.

````Python
class FormTestCase(TestCase):
    def test_clean_username_exception(self):
        # Create a player so that this username we're testing is already taken
        Player.objects.create_user(username='test-user')

        # set up the form for testing
        form = EmailUserCreationForm()
        form.cleaned_data = {'username': 'test-user'}

        # use a context manager to watch for the validation error being raised
        with self.assertRaises(ValidationError):
            form.clean_username()
````

1. Create a user, which will have a username that we're trying to register with.
2. Setup the form with the initial <code>cleaned_data</code> dictionary set up. Note, since this is a Unit Test, this is a better way then just actually going through the whole form submittal process.
3. Call the function and use <code>assertRaises</code> to check and capture the <code>ValidationError</code>.

## Mission: Part II
Write the inverse of this form unit test, where we check to see if the <code>clean_username</code> function passes.

Pay attention to what the output is of the function you need to check for if the username is not taken. That's what you'll need to <code>assert</code> in your test.

## Improving Unit Tests

#### Coverage
While we're writing tests, it would be great to have some kind of statistics around how much of our codebase are we actually test.

Luckily someone created a great tool for python to just that. It's aptly named: <code>coverage</code>.

* Install coverage: <code>pip install coverage</code>
* Run our test suite using it: <code>coverage run --source=. manage.py test</code>
* Generate the report on the command line: <code>coverage report -m</code>
* Generate a pretty html report: <code>coverage html</code> then open <code>htmlcov/index.html</code>

And now we can see how much coverage we have of our python code! This tool should not be used as a judgement of exactly how well tested your application is, but is a metric that can be used to track some sort of progress implementing tests.

#### Linting: PEP8 & Pyflakes
To really beef up our test suite, let's also have it check our code for any kind of errors that we can autodetect.

This process is called linting, where you use a "linter" to run through all of your code and detect a variety of issues without needing to actually run it.

Python has 2 different linters, which check for different issues:

* PEP8 - Checks to see if you're breaking any of python's PEP8 conventions: <code>pip install pep8</code>
* Pyflakes - Checks for unused imports and variables: <code>pip install pyflakes</code>

Add 'pep8' and 'pyflakes' as dependencies in our <code>settings.py</code> then add the following <code>TestCase</code> to your <code>tests.py</code>. Now run your test suite again!

````Python
class SyntaxTest(TestCase):
    def test_syntax(self):
        """
        Run pyflakes/pep8 across the code base to check for potential errors.
        """
        packages = ['cards']
        warnings = []
        # Eventually should use flake8 instead so we can ignore specific lines via a comment
        for package in packages:
            warnings.extend(run_pyflakes_for_package(package, extra_ignore=("_settings",)))
            warnings.extend(run_pep8_for_package(package, extra_ignore=("_settings",)))
        if warnings:
            self.fail("{0} Syntax warnings!\n\n{1}".format(len(warnings), "\n".join(warnings)))
````

Your test suite should now fail with a bunch of lint errors. Aren't computers great?

## Mission: Part III
Clean up all of your lint errors and make your test suite pass!

## Refactoring

#### Refactoring Testable Code
Writing tests for your code often makes you write cleaner code. Since you want to be able to write a test for units of logic, often times the code is written in smaller pieces. These smaller pieces are usually in separate functions, which then become more reusable.

When implementing tests for existing code it usually involves some refactoring to make the code more easily testable. This can be a scary endeavor, however, since we don't want to break the code that's already there. There are no tests in place to let us know if our refactoring breaks anything!

#### Let's Refactor and Test!
Let's say we want to make a change to how the email works when a new user registers. As of right now, this code exists inside a view function and is not tested. In order to write a test to make sure an email gets sent properly, we'd have to test the view.

So let's refactor this emailing logic, so that it happens when the form is saved, on our custom form <code>EmailUserCreationForm</code>.

First, we'll move this code out of our view and into a <code>save</code> method on our form.

````Python
class EmailUserCreationForm(UserCreationForm):
    ...

    def save(self, commit=True):
        user = super(EmailUserCreationForm, self).save(commit=commit)
        text_content = 'Thank you for signing up for our website, {}'.format(user.username)
        html_content = '<h2>Thanks {} for signing up!</h2> <div>I hope you enjoy using our site</div>'.format(user.username)
        msg = EmailMultiAlternatives("Welcome!", text_content, settings.DEFAULT_FROM_EMAIL, [user.email])
        msg.attach_alternative(html_content, "text/html")
        msg.send()
        return user
````

Now we can write a test just for our form's save function instead of the whole Django view.

Let's write a test that checks we sent out an email and that the subject is what we expected.

Django gives you access to an <code>outbox</code>, which lets you test sending email easily.

````Python
def test_register_sends_email(self):
    form = EmailUserCreationForm()
    form.cleaned_data = {
        'username': 'test',
        'email': 'test@test.com',
        'password1': 'test-pw',
        'password2': 'test-pw',
    }
    form.save()
    # Check there is an email to send
    self.assertEqual(len(mail.outbox), 1)
    # Check the subject is what we expect
    self.assertEqual(mail.outbox[0].subject, 'Welcome!')
````

#### Testing a New Feature
When starting off with a new feature, it's the best time to write tests. Thinking about how you're going to test the code you're writing will influence the way you write it (in a good way!).

Some developers strictly write all of their tests before writing any of their feature's code. This is referred to as Test Driven Development. We'll learn more about this later, but for now we will mix writing tests and feature code. This is fine, as long as testing is not an afterthought.

#### User Record
Let's implement showing our user's win/loss record on their profile page. This means our view will need to be responsible for passing along this information to our template.

At first glance, we may be tempted to write some code in our profile view that would do some queries to figure out the number of wins and losses for the logged in user and pass that to the template. This, however, would not be easily reusable or testable!

Let's instead put that business logic into methods on our models. If we have a user, it may make sense to be able to call a method such as <code>user.get_wins()</code> or <code>user.get_losses()</code>.

These methods would then also be easily reusable from anywhere in our application if we have a user object. We can also write tests, just for these methods and not worry about the view.

#### Methods
First, let's create the appropriate methods on our user model. These could be abstracted even more, but good enough for now.

````Python
class Player(AbstractUser):
    ...

    def get_wins(self):
        return WarGame.objects.filter(player=self, result=WarGame.WIN).count()

    def get_losses(self):
        return WarGame.objects.filter(player=self, result=WarGame.LOSS).count()
````

#### Tests
Second, we'll write tests for each of these methods. We'll need to create WarGame's so let's use a helper method to set up dummy data.

````Python
def create_war_game(self, user, result=WarGame.LOSS):
    WarGame.objects.create(result=result, player=user)

def test_get_wins(self):
    user = Player.objects.create_user(username='test-user', email='test@test.com', password='password')
    self.create_war_game(user, WarGame.WIN)
    self.create_war_game(user, WarGame.WIN)
    self.assertEqual(user.get_wins(), 2)

def test_get_losses(self):
    user = Player.objects.create_user(username='test-user', email='test@test.com', password='password')
    self.create_war_game(user, WarGame.LOSS)
    self.create_war_game(user, WarGame.LOSS)
    self.create_war_game(user, WarGame.LOSS)
    self.assertEqual(user.get_losses(), 3)
````

#### Implement
Third, let's pass this information from the view to our template and display it.

**views.py**
````Python
@login_required
def profile(request):
    return render(request, 'profile.html', {
        'games': WarGame.objects.filter(player=request.user),
        'wins': request.user.get_wins(),
        'losses': request.user.get_losses()
    })
````

**profile.html**
````HTML
<p>Hi {{ user.username }}, you have {{ wins }} wins and {{ losses }} loses.</p>
````

## Mission: Part IV

Let's add a new feature to our application. We want our user to get badges for getting a certain number of wins.

* We want their profile to show badges when they get 5, 15, and 30 wins.
* We want to send them an email notification that they earned each badge.
* Write your new feature in an easily reusable and testable way.
* Create tests for all of your new code.
* Your code coverage should not fall below what it was before implementing your new feature.

## Mission: Part V
Find a previous project that has interested you and write tests for it!

You know how to use coverage and can start monitoring how much of your application you are slowly covering with tests as you go.

Parts of your application may have large code blocks that are hard to test. You should refactor that into smaller, testable units.

If you've covered a large portion of your project with tests and have fixed all linting errors try implementing a new, tested, feature for your application.

## Integration Testing
The other type of testing strategy, integration testing, is when you test that some process or larger feature works end to end.

Well tested code bases have a mixture of unit and integration tests.

For our application, let's say we want to test a page in our application. We can write a test that calls a specific URL and then check the HTML coming back as well as some data in the database being affect.

This would incorporate testing how multiple parts of our Django application integrate with each other: url routing, views, model logic, template rendering, etc.

#### Django Integration Test
Let's keep it simple at first. We'll test that our home page and make sure it's rendering the expected HTML as well as receiving the appropriate card data.

````Python
class ViewTestCase(TestCase):
    def setUp(self):
        create_deck()

    def test_home_page(self):
        response = self.client.get(reverse('home'))
        self.assertIn('<p>Suit: spade, Rank: two</p>', response.content)
        self.assertEqual(response.context['cards'].count(), 52)
````
**add <code>from django.core.urlresolvers import reverse</code> to the top of tests.py to import the reverse method**

<code>self.client</code> is built into Django's <code>TestCase</code> class, which is a helper for calling your urls. We use it to make a GET request to the home page.

We then check <code>response.content</code>, which represents the HTML or potentially JSON that was outputted by the view, then <code>response.context</code>, which is the dictionary of data passed to a template.

## Mission: Part VI
Let's create tests for a few of the other simple pages.

* Write a test for the FAQ page.
* Write a test for the filters page.

#### POST Integration Test
Next, let's write a test for registering for our site. We'll need to make a POST request to our register URL, with the appropriate user information. We'll then want to check that we've redirected appropriately and that the user was created in the database.

````Python
class ViewTestCase(TestCase):
    ...

    def test_register_page(self):
        username = 'new-user'
        data = {
            'username': username,
            'email': 'test@test.com',
            'password1': 'test',
            'password2': 'test'
        }
        response = self.client.post(reverse('register'), data)

        # Check this user was created in the database
        self.assertTrue(Player.objects.filter(username=username).exists())

        # Check it's a redirect to the profile page
        self.assertIsInstance(response, HttpResponseRedirect)
        self.assertTrue(response.get('location').endswith(reverse('profile')))
````

## Mission: Part VII
Now let's create a test for the login page of our application.

#### User Integration Test
Let's say you want to test the profile page, but this requires having a user that is already logged in. Django's <code>client</code> testing helper, let's us login a user then perform whatever necessary Django functions we need to do.

````Python
class ViewTestCase(TestCase):
    def create_war_game(self, user, result=WarGame.LOSS):
        WarGame.objects.create(result=result, player=user)

    ...

    def test_profile_page(self):
        # Create user and log them in
        password = 'passsword'
        user = Player.objects.create_user(username='test-user', email='test@test.com', password=password)
        self.client.login(username=user.username, password=password)

        # Set up some war game entries
        self.create_war_game(user)
        self.create_war_game(user, WarGame.WIN)

        # Make the url call and check the html and games queryset length
        response = self.client.get(reverse('profile'))
        self.assertInHTML('<p>Your email address is {}</p>'.format(user.email), response.content)
        self.assertEqual(len(response.context['games']), 2)
````

## Mission: Part VIII
Let's write a test for the WAR page, which should be a little bit more of a challenge.


#### Mocking
Warning! Mocking is an advanced testing topic and can take awhile to understand what's happening.

When you're writing tests and your code has a dependency on another set of functions or general 3rd party service, say Twitter's API, you don't want to test necessarily if Twitter's API is working every time you run your test suite.

Mocking let's you fake what the call to Twitter's API would return, so that you can focus on the test at hand for your code, without your test failing if Twitter's API goes down.

The concept is that you "Patch" what the bits of code are and just tell your program what those bits of code should return when called, without actually calling them.

#### XKCD
Our home page now looks pretty plain and is not inside of our base template. Let's change that! We're going to put some inspiration on the home page by using XKCD's API: [XKCD API docs].

The game plan is to put a random comic on our homepage, every time the user goes to the page. We'll first get the latest comic from XKCD, to see how many comics there are total, then pick a random comic from 1 to that number.

First, let's create a function in <code>utils.py</code>, which will get a random comic from XKCD. We're going to use a new library, which helps us make requests easier: <code>pip install requests</code>

````Python
def get_random_comic():
    # Get the "num" of the latest one to get the total amount of xkcd comics created
    latest_comic = requests.get("http://xkcd.com/info.0.json").json()

    # Get a random comic from all time
    random_num = random.randint(1, latest_comic['num'])
    random_comic = requests.get("http://xkcd.com/{}/info.0.json".format(random_num)).json()
    return random_comic
````

Now let's set up our home page's view and template to use our new random comic.
** views.py
````Python
def home(request):
    return render(request, 'home.html', {
        'comic': get_random_comic()
    })
````

<strong>home.html</strong>
````HTML
{% extends 'base_template.html' %}

{% block content %}
    <h2>Some Random Inspiration</h2>
    <div>
        <h3>{{ comic.safe_title }} - {{ comic.year }}</h3>
        <img alt="{{ comic.alt }}" src="{{ comic.img }}">
        <p>{{ comic.transcript }}</p>
    </div>
{% endblock content %}
````

#### Mocking XKCD
Now how do we go about writing a test to prove a comic loaded on our home page? We don't want our test to rely on the XKCD API. We just want to test that we pass a dictionary of comic information to our template and render it appropriately.

Let's mock it! First we'll need to install mock: <code>pip install mock</code>.

Now let's start changing our home page test. Mock let's us patch the result of a specific function on a python module. In this case we want to patch what requests.get returns to us.

Let's break it down into pieces. First, we can use a decorator from the mock module to specific the function we're going to patch.

````Python
@patch('cards.utils.requests')
def test_home_page(self, mock_requests):
````

Here, we're saying we want to patch the requests library in our <code>utils.py</code> file. This gives us access to a new variable, which we've named <code>mock_requests</code> in our test where we'll see next that we can start patching values.

Now that we have the requests library properly patched with mock, we can specify what we want the module to return.

````Python
 mock_comic = {
        'num': 1433,
        'year': "2014",
        'safe_title': "Lightsaber",
        'alt': "A long time in the future, in a galaxy far, far, away.",
        'transcript': "An unusual gamma-ray burst originating from somewhere across the universe.",
        'img': "http://imgs.xkcd.com/comics/lightsaber.png",
        'title': "Lightsaber",
    }
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = mock_comic
    mock_requests.get.return_value = mock_response
````
We've come up with our own fake comic, which we're going to set as the return value of <code>json()</code> as well as a <code>status_code</code> of 200. We've also set this as the return value of the <code>get()</code> call.

````Python
response = self.client.get(reverse('home'))
    self.assertIn('<h3>{} - {}</h3>'.format(mock_comic['safe_title'], mock_comic['year']),
                  response.content)
    self.assertIn('<img alt="{}" src="{}">'.format(mock_comic['alt'], mock_comic['img']),
                  response.content)
    self.assertIn('<p>{}</p>'.format(mock_comic['transcript']), response.content)
````

We're just checking that the appropriate comic data was passed from our view and formatted in our template appropriately.

This is a more simple use case we've seen, but can be very powerful for testing complicated applications.

Now the requests library will not make an API call, but instead return the fake comic we've created. Next all we need to
do is test our page's content as we normally would.

## Mission: Part IX
Let's try out more mocking. Gravatar is an open service for having an avatar and information for your email address across all websites.

1. When a user first signs up, pull in their Gravatar information and save it in your Player model: [Gravatar docs]
2. This may require making some migrations to save some of the data.
3. Show some of this information, for example their photo, on the profile page.
4. Write a test that mocks pulling in and saving the Gravatar information when a user first registers.


## Selenium Testing
Selenium is a tool that let's us test our application in a real, live web browser. It's a type of integration test that let's us really prove that our application is functioning properly for a user.

Out of the box, selenium let's us load up a page and then start interacting with the DOM. We can check if elements exist, we can fill out form fields, and we can interact with elements such as clicking a button.

Selenium tests can be slow, and a bit painful to write so they should not be written for every feature of your application. You should think carefully and pick mission critical parts of your application to test.

Selenium has drivers for all of the various browsers, but Firefox seems to be the most used.

#### Our First Selenium Test
Let's test that we can login to the admin portal on our website! We will actually get to see Firefox in a brief moment open up and login to our app's admin.

Django has a built in test case we can use to run selenium tests called <code>LiveServerTestCase</code>. This will handle spinning up a server that's running our application for selenium to use.

First, a few things we need to set up to get selenium working:

* Install it! <code>pip install selenium</code>
* We need to run <code>python manage.py collectstatic</code> so our static assets are available to the live test server.
* We need to set our static root appropriately: <code>STATIC_ROOT = os.path.join(BASE_DIR, 'static')</code>
* A weird bug in Django with selenium tests requires us to move <code>django.contrib.contenttypes</code> to the top of our <code>INSTALLED_APPS</code> list.

#### Setup and Tearddown
Let's set up the first <code>TestCase</code> for our selenium tests:

````Python
class SeleniumTests(LiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        cls.selenium = WebDriver()
        super(SeleniumTests, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super(SeleniumTests, cls).tearDownClass()
````

Note that we're using class methods for setting up and tearing down. These only get run once, before all of the tests run and after all of the tests run whereas the regular methods get run before and after each test.

We're doing this so that our tests run quicker. <code>cls.selenium = WebDriver()</code> is opening and booting up Firefox. We don't want to open and close Firefox after every individual test. We can reuse the window for each one.


#### Opening a Page
Let's break our first test of logging into the admin down piece by piece.

````Python
def test_admin_login(self):
    # Create a superuser
    Player.objects.create_superuser('superuser', 'superuser@test.com', 'mypassword')

    # let's open the admin login page
    self.selenium.get("{}{}".format(self.live_server_url, reverse('admin:index')))
````

First, we'll create a new superuser that we'll use to log into the admin and open up the admin page. <code>self.live_server_url is</code> a variable that <code>LiveServerTestCase</code> gives us so we know the right address and port to access our running server at.

Let's run this, we should see Firefox pop up for a second and load the admin login page.

#### Loggin In
Next, let's fill out the form and submit it.

````Python
# let's fill out the form with our superuser's username and password
self.selenium.find_element_by_name('username').send_keys('superuser')
password_input = self.selenium.find_element_by_name('password')
password_input.send_keys('mypassword')

# Submit the form
password_input.send_keys(Keys.RETURN)
````
Selenium gives us utilities to find elements by their name as well as to imitate pressing keys on a keyboard. Here we find the form inputs for the username and password field then enter our admin user's username and password.

Afterwards, we imitate pressing the return key so that our form is submitted to the server.

Run the tests again and you should see the forms being filled out then submitted by our test!

#### Checking It Worked
Lastly, we need to check that our form submitted and the page redirected to the main admin page.

````Python
# sleep for half a second to let the page load
sleep(.5)

# We check to see if 'Site administration' is now on the page, this means we logged in successfully
body = self.selenium.find_element_by_tag_name('body')
self.assertIn('Site administration', body.text)
````
The first thing we do is <code>sleep</code> our test for half a second. When writing selenium tests, "phantom" bugs can crop up after selenium navigates from one page to the next. By sleeping here for a very short period of time we can avoid trying to access the page before it has fully reloaded.

Next we check that in the body of our html page we see the 'Site administration' text, which shows up in the header once we're logged in.

Run your test one more time to see it fully pass.

#### Create a Card
Let's walk through one more example before you try some on your own. This time, let's go through the admin page for our Card model and create a new card. If you don't have the Card model registered with the admin for some reason, set that up now.

The first thing we'll need our selenium test to do again, is to log into the admin. This is probably something we'll need to do often, so let's just make a helper method out of our first test.

````Python
def admin_login(self):
    # Create a superuser
    Player.objects.create_superuser('superuser', 'superuser@test.com', 'mypassword')

    # let's open the admin login page
    self.selenium.get("{}{}".format(self.live_server_url, reverse('admin:index')))

    # let's fill out the form with our superuser's username and password
    self.selenium.find_element_by_name('username').send_keys('superuser')
    password_input = self.selenium.find_element_by_name('password')
    password_input.send_keys('mypassword')

    # Submit the form
    password_input.send_keys(Keys.RETURN)
````
Now we can just reuse this in any of our tests.

#### Navigate
Once we're logged in, we can now navigate our way to the 'Add Card' page.

````Python
def test_admin_create_card(self):
    self.admin_login()

    # We can check that our Card model is registered with the admin and we can click on it
    # Get the 2nd one, since the first is the header
    self.selenium.find_elements_by_link_text('Cards')[1].click()

    # Let's click to add a new card
    self.selenium.find_element_by_link_text('Add card').click()
````
We use the <code>find_elements_by_link_text</code> methods to find the proper links and click our way through to the page using <code>click()</code>.

Run the test and check that you get to the Add Card screen. Feel free to include <code>sleep(3)</code> to have the test pause so you can see the state of your browser at any point during the test.


#### Fill out Form
Next we'll fill out the form. Filling out the card rank looks just the same as when we filled out the login form, but suit is actually a dropdown.

````Python
# Let's fill out the card form
self.selenium.find_element_by_name('rank').send_keys("ace")
suit_dropdown = self.selenium.find_element_by_name('suit')
for option in suit_dropdown.find_elements_by_tag_name('option'):
    if option.text == "heart":
        option.click()
````
Here we loop over all of the options of the dropdown and click the right one when it matches "heart".

Run your test again and see that the form is filled out.

#### Copy & Check
Lastly we need to submit the form and check that it submitted and saved properly.

````Python
# Click save to create the new card
self.selenium.find_element_by_css_selector("input[value='Save']").click()

sleep(.5)

# Check to see we get the card was added success message
body = self.selenium.find_element_by_tag_name('body')
self.assertIn('The card "ace of hearts" was added successfully', body.text)
````

This time we find the save button using a css selector, which is similar to how you would in jQuery. Once we find it, we then click it.

Afterwards, we check that the admin success message shows up on our page.

## Mission: Part X
You've now seen two examples all the way through. Let's try creating some of these selenium tests on our own.

* Test your application's login page.
* Register and test that you can add a new Player through the admin.
* Test that you can edit an existing player in the admin.
* Test your application's register page works.


#### Django, Javascript & Testing
Now that we're revisiting our playing cards application and we've learned about javascript, let's implement a new feature that's also tested.

Our WAR game would make a lot more sense if we could interact with it using javascript and keep playing war without having the page reload.

Learning how to unit test javascript code isn't something we're going to tackle right now. All it involves is learning a new testing framework for javascript, but what we can do is use Selenium to at least create integration tests that our javascript is working correctly.

## Mission: Part XI
The goal is to take our WAR page and create a new version that uses javascript, but is also tested with selenium.

* Create a new url, view, and template for our new interactive war game.
* We'll want to create a new javascript file where our code will go.
* Have the deck of cards get split in half, with half of the cards assigned to the user and half assigned to the computer player. Make sure you randomize the cards passed to each player.
* Have a button on your war game page, which when clicked, will get a card from both player's decks. It will then make an AJAX call to the server to save a win, loss, or tie for the logged in user based on the two new cards.
* This way a user can play through a whole deck of cards with the computer. When the deck is empty, there should be a message displayed on the page and the button to play again should be disabled.
* Write a selenium test, which will test out multiple things: a. clicking the button shows new cards, b. after new cards are shown the database correctly has been updated with a win/loss/tie, and c. the proper message shows and button gets disabled when there are no cards left in the player's deck.
* Just as we did earlier, the rest of today and tonight will be spent implementing integration and selenium tests for your application.

Think about the major flows in your application that you can test end to end using integration and selenium tests.

By the time you've implemented these the test coverage on your project should start to be getting pretty high.

Again, if you've gotten to the point where you've written a lot of integration and selenium tests, feel free to add a new feature with tests.

## Test Driven Development
##### Upgrade our Test Suite
Before we jump into test driven development we're going to learn a new testing tool called factories.

Before we jump into factories, let's organize our test file a bit, now that we've got so many.

* Let's create a test package in our cards application (should have an __init__.py). Django's testing framework doesn't just look for a <code>tests.py</code>. It can also look for a package.
* First, let's move our <code>test_utils.py</code> file to our test folder and just call it utils.py.
* Then let's create an empty file called <code>factories.py</code>, which will contain our factory code we'll write shortly.
* Finally, let's create separate test files for each of our <code>FormTestCase</code>'s in tests.py. We have to prefix each file with <code>test_</code> since that's what Django's test runner looks for. For example, your <code>FormTestCase</code> should go in a file named <code>test_forms.py</code>
* Once we've made all of those files, move each TestCase into it's appropriate file and make sure you add all the appropriate imports.
* Then run your test suite again and make sure nothing broke!

#### Factories
When writing tests there's often a lot of state that we need to build up to create the proper scenarios with data in our database.

Often times the code we write to build up state is not very pythonic and is not very DRY.

This is where factories come in! It helps us abstract away some of that code so that we can easily create data for us to use in our tests without having to write ugly code.

Factories are a general concept in testing, but they're not built into python. We'll use a library called <code>factory_boy</code>, which is based on Ruby's <code>factory_girl</code> library.

#### Factory example
n our tests, there are multiple places where we have to set up WarGame's in our database to test various functions. Let's create a factory that will do this for us.

* Let's get factory boy installed: <code>pip install factory_boy</code>
* Now let's set up our first factory in <code>factories.py</code>

````Python
class WarGameFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'cards.WarGame'
````

All we need to do, to set up the most basic factory is set the model to the appropriate Django model and inherit from <code>DjangoModelFactory</code>.

* To use our factory to create a new <code>WarGame</code> is call it like so <code>WarGameFactory(player=player, result=WarGame.LOSS)</code>. This, however, does not save us much typing over just creating them individually.
* We can use a method on the factory to create multiple at the same time: <code>WarGameFactory.create_batch(num_to_create, player=user, result=WarGame.LOSS)</code>

Let's set up our <code>test_get_losses</code> to use our new factory and remove the repetitive code.

````Python
def test_get_losses(self):
    user = Player.objects.create_user(username='test-user', email='test@test.com', password='password')
    WarGameFactory.create_batch(3, player=user, result=WarGame.LOSS)
    self.assertEqual(user.get_losses(), 3)
````
This is much cleaner than we had before! Run your tests to make sure nothing has broke.

## Mission: Part XII
* Find the couple other places in our test suite where we could use our new factory and refactor the code!

Note: we may be able to remove helper functions we had created to do some of this.

* Once you're done with that, try implementing a <code>PlayerFactory</code> to create default users for our tests. Check out the example in [factory boy's documentation]. Use the new factory as appropriate around the test suite.

## Test Driven Development (TDD)
Some developers and companies subscribe to a method of development where the tests are actually written before starting to code functionality.

The process is as follows:

* Think about the specification and architecture of a feature as well as the functions necessary for that feature.
* Create tests for that code, which assert what the input and output of those functions would be.
* See all of your tests are failing (since there's no code yet).
* One by one, see the tests start passing while you're implementing the new feature.
* Once the tests are all passing, you're finished!

#### Why TDD?
TDD helps lead to beautifully designed code. It causes the developer to really think hard up front about the specification of what they're building.

It also means that a developer is likely to split their functionality out into many small testable functions so that they can easily write unit tests.

This is great for reusability, organization, and readability. It also means that the code base will be close to 100% covered by tests with a tests-first mentality.

#### Simple TDD Example
Let's say we want to actually add our player's full record to their profile. We want to show it in the format wins-losses-ties.

First, we know we'll want to create a function on our <code>Player</code> model that creates this nicely formatted string for us.

Second, we know we already have methods for <code>get_wins</code> and <code>get_losses</code>. Likely we'll want to make a third method to get the number of ties.

#### TDD Failing Tests
So let's set up our failing tests!

First, let's create a test for our future <code>get_ties</code> method on our <code>Player</code> model

````Python
def test_get_ties(self):
    user = Player.objects.create_user(username='test-user', email='test@test.com', password='password')
    WarGameFactory.create_batch(4, player=user, result=WarGame.TIE)
    self.assertEqual(user.get_ties(), 4)
````

If we run our tests, this obviously fails.

Next, let's create our failing test for our other function, which will print out the nicely formatted record. Let's decide on calling this method <code>get_record_display</code>

````Python
def test_get_record_display(self):
    user = Player.objects.create_user(username='test-user', email='test@test.com', password='password')
    WarGameFactory.create_batch(2, player=user, result=WarGame.WIN)
    WarGameFactory.create_batch(3, player=user, result=WarGame.LOSS)
    WarGameFactory.create_batch(4, player=user, result=WarGame.TIE)
    self.assertEqual(user.get_record_display(), "2-3-4")
````
Run our tests again, obviously we now have two failing tests. Time to implement!

#### TDD Passing Tests
Now that we have our failing tests in place, let's implement the feature.

````Python
def get_ties(self):
    return WarGame.objects.filter(player=self, result=WarGame.TIE).count()

def get_record_display(self):
    return "{}-{}-{}".format(self.get_wins(), self.get_losses(), self.get_ties())
````
These methods are fairly simple to implement, but since we had our tests in place we can check their correctness by just running our tests again.

Run your tests again and check that the build passes!

## Mission: Part XIII
Now that we successfully created the methods needed to display a player's record, using TDD put this information into their profile template. Modify the profile integration test so that it is failing first, then implement the code.

Let's create a larger feature in our application using TDD.

* We want to show a leaderboard for our application.
* It's up to you to decide your own algorithm for the ranking. Obviously wins should matter most, but ties could rank the player higher as well.
* Think of the view you'll need to create, the methods you'll need to create to make this ranked list, and what html you want to display on the page. This will dictate your tests, then your actual implementation.

## Continuous Integration
Previously we talked about how continuous integration helps improve the velocity of your team and overall quality of your product.

Now that we've implemented tests, we're now ready to set up CI!

We're going to set up CI using codeship.io for our playing cards application.

1. Sign up for a free account with the github login on codeship.io
2. Push your repository to your personal github if you have not yet.

#### CI Setup
1. Add a test_settings.py file in the same folder as your settings.py This has database settings for codeship.io to work.

````Python
import os

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "test",
        "USER": os.environ.get('PG_USER'),
        "PASSWORD": os.environ.get('PG_PASSWORD'),
        "HOST": "127.0.0.1",
        "PORT": "",
    }
}
````
2. <code>pip freeze -r requirements.txt > requirements.txt</code> so that you have the latest.
3. Make sure all of your work is now committed up to your repository.
4. Create a new project on codeship.io and pick your personal playing-cards repository from github.
5. Select the option to create your own custom commands from the dropdown.

1. Set these as your setup commands

````bash
cd war
cp war/test_settings.py local_settings.py
pip install -r requirements.txt
# Sync your DB for django projects
python manage.py syncdb --noinput
# Run migrations for your django project
python manage.py migrate --noinput
````

2.Set these as your test commands

````bash
coverage run --source='.' manage.py test
coverage report -m
````

3. Save and cross your fingers that everything works.


#### Pull Request Passes!
Hopefully mostly everyone now has their build passing on codeship.io. As you start working on your repository and making more commits, codeship will rerun your test suite everytime you push a commit to github.

It will notify you and your team if someone has broken the build.

Also, if you make a pull request it will warn users not to merge in the pull request if the tests are broken. This is super valuable!

#### Make It Fail
Now that we have Codeship set up on our repository, let's walk through making a pull request and seeing how Codeship integrates with Github.

* Let's create a new branch by logging into github called new-test.
* Locally, let's pull down that new branch: <code>git fetch</code>.
* Now let's switch over to it: <code>git checkout new-test</code>
* Let's put in a failing test case
````Python
def test_failing_case(self):
    a = 2
    b = 3
    self.assertEqual(a * b, 5)
````
* Now let's commit and push this failing test back up to github, then make a pull request.
* If Codeship is set up properly, we should see that our branch is now failing on our pull request and you received an email!

#### Make it Pass Again
Let's make our pull request pass again and fix the build.

* Let's fix our test by changing <code>5</code> to <code>6</code>
* Commit this change into git and push it back up to our branch.
* We should see the pull request now has a passing build and we should receive an email that the build has been fixed from Codeship!


#### Regroup
Now that we've seen how to set up codeship and have a week's long worth of testing experience, let's get back into teams and set up a real test suite for our project.

* Get Codeship set up for your team project. Make sure everyone is added as a team member to one central codeship account.
* Compare the tests you've written so far for your project with your teammates. Using pull requests, merge in the best parts of everyone's test suite into your repository's develop branch.
* Be sure to code review and make sure that your teammate's pull request is passing the build on codeship before merging in.
* Make sure to spend some serious time looking over each other's tests and make sure you get codeship passing.
* You should be aiming for 80%+ testing coverage with your combined testing suite.

## Mission: Part XIV
Now that everyone's been through a trial running on being part of a team, collaborating on github, and writing tests let's create a new project together!

For the rest of the day and homework this weekend you'll be working with the same teams on a new project.

* You will have to abide by the same rules: Use pull requests, don't merge your own pull request, and do code reviews.
* You will have to write tests for your code. Your project should have 80%+ code coverage.
* You will need to use and setup Codeship so that you can tell if a teammate's pull request has broken the build.
* You should follow TDD and think about your tests, as well as write them, before you start working on your feature.

[XKCD API docs]: http://xkcd.com/json.html
[Gravatar docs]: https://en.gravatar.com/site/implement/profiles/json/
[factory boy's documentation]: http://factoryboy.readthedocs.org/en/latest/orms.html#factory.django.DjangoOptions
