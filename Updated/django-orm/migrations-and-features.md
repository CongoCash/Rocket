Django - Features and Overview
==============================

First, let's finish off our Blog model. Let's insert the one to many field into the <code>models.py</code>

````Python
class Post(models.Model):
    title = models.CharField(max_length=120)
    body = models.TextField()
    author = models.ForeignKey(Author)

    def __unicode__(self):
        return u"{}".format(self.title)
````

Now let's insert the many to many relationship into the same file.

````Python
class Tag(models.Model):
    name = models.CharField(max_length=20)
    posts = models.ManyToManyField(Post)

    def __unicode__(self):
        return u"{}".format(self.name)
````


##Django Admin Site
One of Django's more powerful features is that it comes with a built-in option for an automatic admin interface. This admin gives you a visual output of your database models, allowing you to more easily see relationships and to create new records.

Before we go any further with our model relationships, we are going to add this admin interface so you can more easily visualize the changes you are making.

###Running the Admin
1. In your terminal, go to the folder containing your Django project
2. Make sure you are in the folder that contains <code>manage.py</code>
3. Run <code>python manage.py runserver</code>
4. Open your browser and navigate to http://127.0.0.1:8000/. You’ll see a “Welcome to Django” page, in pleasant, light-blue pastel. This is Django's default page just to let you know your project is running successfully
5. Now navigate to http://127.0.0.1:8000/admin/. You should see the admin login screen:

![admin login img]

If you run into issues, make sure that you have added 'django.contrib.admin' to your INSTALLED_APPS setting. The admin has four dependencies - django.contrib.auth, django.contrib.contenttypes, django.contrib.messages and django.contrib.sessions. If these applications are not in your INSTALLED_APPS list, add them.

````Python
INSTALLED_APPS = (
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "YOUR APP",
)
````

Also, add django.contrib.messages.context_processors.messages to TEMPLATE_CONTEXT_PROCESSORS as well as django.contrib.auth.middleware.AuthenticationMiddleware and django.contrib.messages.middleware.MessageMiddleware to MIDDLEWARE_CLASSES. (These are all active by default, so you only need to do this if you’ve manually tweaked the settings.)

###Adding Your Apps to the Admin
Of course, we don't just want to see Django's built-in models, but also the models we created

1. Open the admin.py file inside your app
2. Add the following code:


````Python
from django.contrib import admin
from your_app.models import YourModel

admin.site.register(YourModel)
````

3. Refresh your admin view and click on one of your models. You'll now be at the "change list" page for that model. It will display all the database records of that model. You can edit your existing records or add new ones. The form is automatically generated by Django based on the fields on your model.

##Mission I
The docs will become your best friend over the next couple of months. Getting used to reading it, navigating it and finding what you need will be an important skill for you to have. For this exercise, it will be on you to figure out how to implement each bullet point using the [admin documentation].

1. Register all of your models in your application in the admin. Create a new instance of each using the admin then check they were created using your shell.
2. Create a custom admin for your Post model. Have your admin list page only show the fields: title, body and author (no id field).
3. Create a custom admin for your Author model. Have your admin detail page only show the name field for editing (hide the twitter field).
4. For your Post model, set up a list filter for the author field, so you can search quickly for posts by a specific author only.
5. For your Tag model, have the posts many to many field use the "filter horizontal" UI widget instead of the normal multi-select box.
6. Set up an inline admin for your Post model, which will show all comments for that Post on the detail page.
If things are still fuzzy to you, follow the admin portion of the Django Tutorial for more of a guide.


##Django Migrations
Working on your homework, it was very likely that you made a mistake. You ran <code>makemigrations</code>, and afterward realized you wanted to change something about the way you defined your model. If you make changes in your models file but don't update your DB, your DB won't reflect the changes.

Our <code>makemigrations</code> and <code>migrate</code> commands work for not only creating new tables, but also when we need to change our existing models and underlying database tables.

This functionality "Migrations" is a way of tracking changes in your app and applying them to your database. They serve a lot of great purposes:

* Making DB changes
* Allowing you to work on a team
* Helping you revert DB changes


###Inspecting the Migration
So what happened when we ran <code>python manage.py makemigrations</code> and <code>python manage.py migrate</code>? If we look in our app directory, we should see a migration folder. This folder holds the record of all migrations for models in this application.

The migrations are numbered to it easier for us to see what order they were ran in. This means you could be working on this project with another person, and they would be able to run your code and it would create the necessary database tables for them.

Running <code>python manage.py makemigrations</code> is the command that actually makes this new migration file in our folder.

Running <code>python manage.py migrate</code> is the command that has Django actually make the changes in the migration to our database.

````
/your_project
	/your_app
		/migrations
			0001_initial.py
			0002_blog.py
			__init__.py
````

###Understanding Migration Files
If you look at your initial migration file, you should see something, maybe a little scary, that looks like this.

````Python
class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False,
                                        auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=120)),
                ('twitter', models.CharField(max_length=40, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]

````

Don't freak out. This file can be broken up into a few simple parts:

The <code>dependencies</code> are other migrations that need to be ran before this migration can be run. Since this migration was the first for our application there are none.

The <code>operations</code> are all of the Create, Alter, or Delete related SQL commands we need to run to change the database to be in sync with our models.

````Python
class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
    ]
````


###Order of Operations
1. You make a change to one of your models
2. You run <code>python manage.py makemigrations app_name</code> -- this creates your migration files. That is all it does. It creates the file in the migrations directory. To actually apply the migration to your database, you run...
3.<code>python manage.py migrate app_name</code>

Note: Here we've actually specified the app_name. If you don't specify the app_name you make migrations or run migrations for every application in your project. Best practice is to be explicit.

##Mission Part II
We've already ran migrations yesterday. Let's try a few more and look at the files that are being made to see again what's happening.

* Add a publish_date field to your Post model. Create and run migrations. Check out the migration file created. Inspect the table in your psql shell and notice the new column was added.
* Revert your migration for publish_date. Search for and read the django documentation on how to revert your migration. It should just be one command you have to run.
* Add a "blurb" field to your Post model. Create and run migrations for it.
* Create a datamigration, which will fill in our blurb field with the first 100 characters of the body of the post, plus a elipsis. Data migrations are used to prepopulate values in our database tables, especially when we're adding a new field. Read [Django migration docs]!

##Mission Part III
Let's practice database design, creating models, and using those models to save data as well as query to get that data back.

Build a World Cup project. Start a new Django project following the instructions from earlier. Your application will need to keep track of all of the teams in the tournament.

Here's the requirements for your application. It will be up to you to do the database design and create the models needed:

* It will need to keep track of all teams in the tournament as well as the players on those teams.
* It should keep track of the different groups each team is assigned to.
* It should be able to store win and loss records for different match ups during the tournament.
* Bonus: Have your application work for multiple World Cup tournaments

After this is done, insert information into the database for your different models. Also register your models in the admin so you can see, visually, the data you're creating.

Using the Django ORM, craft some querysets to get interesting information out of your database. Here are some example ideas:

1. Get all players on teams that have no losses.
2. Get all players on teams in a specific group.
3. Get the "winner" of each group.
4. Get the win/loss ratio for all teams.
5. Get the team with the most wins.

##Mission Part IV
If you've finished the World Cup project, take the Building Manager and/or Movie exercises and create real Django models out of them.

You know the drill. Do some database design, create the models, create and run your migrations, insert real data, then create some interesting queries.

It is <strong>EXTREMELY</strong> important you have a solid grasp on databases, relationships, and the Django ORM to build upon.

##Weekend Mission
<strong>Read the Django every line of the following sections of the Django docs. Particularly</strong> [Django models], [Django queries], [Django querysets].

After that, let's take our blog application and add some new functionality to it.
* First, we want to allow Users to sign up and view our blog posts. A User will have a name, email, and username.
* Let's allow our users to comment on our blog posts. We'll need to make a Comment table which has the text of the comment and relates to a blog post as well as the user who wrote it.
* Lastly, let's allow our users to "thumbs up" our posts as a rating system. We only want to allow a user to vote on a blog post once. We'll need a Vote (intermediary) table, which is tied to the user and tied to the blog post.

Next, let's write some queries using Django's ORM. You should first populate your User, Comment, and Vote tables with some data first for testing.

* Write a function, which takes a blog post id and returns all of the comments for that blog post.
* Write a function, which takes a blog post id and returns the amount of votes for that blog post.
* Write a function, which takes a user id and gets all comments by that user.
* Write a function, which returns all tags for blog posts that have been voted on by the user with a pk of 1.
* Write a function, which returns all users that have commented on a blog post written by the author with the name 'Dr. Seuss'.

Next, let's practice database design, creating models, and using those models to save data as well as query to get that data back.

Build a World Cup project. Start a new Django project following the instructions from earlier. Your application will need to keep track of all of the teams in the tournament.

Here's the requirements for your application. It will be up to you to do the database design and create the models needed:

* It will need to keep track of all teams in the tournament as well as the players on those teams.
* It should keep track of the different groups each team is assigned to.
* It should be able to store win and loss records for different match ups during the tournament.
* Bonus: Have your application work for multiple World Cup tournaments

Insert information into the database for your different models. Also register your models in the admin so you can see, visually, the data you're creating.

Using the Django ORM, craft some querysets to get interesting information out of your database. Here are some example ideas:

1. Get all players on teams that have no losses.
2. Get all players on teams in a specific group.
3. Get the "winner" of each group.
4. Get the win/loss ratio for all teams.
5. Get the team with the most wins.


[admin login img]: img/admin_login.png
[admin documentation]: https://docs.djangoproject.com/en/dev/ref/contrib/admin/
[Django migration docs]: https://docs.djangoproject.com/en/dev/topics/migrations/#data-migrations
[Django models]: https://docs.djangoproject.com/en/1.7/topics/db/models/
[Django queries]: https://docs.djangoproject.com/en/1.7/topics/db/queries/
[Django querysets]: https://docs.djangoproject.com/en/1.7/ref/models/querysets/