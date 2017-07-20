# Introduction to Databases: Queries and Relationships

There are multiple ways to store data in modern development. For the purpose of this bootcamp we'll be focusing on PostgreSQL and relational databases.

* Why PostgreSQL? The three major relational databases used are MySQL, PostgreSQL, and Oracle.
* PostgreSQL has built in replication, a large number of data types, many extensions, and rapid development.
* A relational database is one that has relations from data in one table to another. For example, we'd store categories for our blog and we'd relate our blog posts to those categories.
* NoSQL databases are meant to store more unstructured data in vasts amount with less consistency. NoSQL databases are known to be easier for scaling.
* Some examples of NoSQL databases are Mongo, Couch, and Hadoop.
* Ultimately the Relational vs NoSQL debate comes down to using the right tool for the job. Both have their place in development.

###Creating a Database
First, let's create a database locally that you can use.

* Type <code>psql</code> in your terminal.
* If you get an error message that you couldn't connect to the server then we need to start PostgreSQL, run <code>postgres -D /usr/local/var/postgres</code>
* Type <code>psql</code> again, you should get an error that a database doesn't exist.
* Let's create our test database for today, typically you'll create different databases for different applications and projects.
* Run <code>psql postgres</code>, this will take us inside of PostgreSQL's shell. <code>postgres</code> is a database installed on every setup of PostgreSQL
* Now that we're inside the shell, let's create our new database. Run <code>create database blog;</code>.
* Then let's switch to our new database. Run <code>\connect blog</code>. If we were just on our command line we could use <code>psql blog</code>

###Tables and Columns
* A database is made up of a collection of tables where we store data.
* Tables are made up of columns, where we store individual pieces of data (numbers, strings, dates, etc). Every new record we store in the table can be visualized as a row. Database tables, can very much be thought of visually like a spreadsheet.
* In the following examples, we're going to try to create database tables that you may have in a blog application.

###Column Types
PostgreSQL has a wide variety of different column types, much more than other relational databases. For starters, let's stick to a list of the basics.

* boolean - true or false values
* varchar(x) - a string of varying length up to x characters long
* integer - an integer value
* date - a specific calendar date (year, month, day)
* timestamp - a date and time
* text - a variable length, usually larger, string

###Creating a Table
````SQL
	CREATE TABLE author (
  id       serial PRIMARY KEY,
  name     varchar(120) NOT NULL,
  twitter  varchar(40)
);
````
* We've created our name field as a varchar with up to 120 characters. We've created our twitter field up to 40 characters.
* Note, we said that our name field is <code>NOT NULL</code> meaning it has to have a value, while the twitter field we're saying can be empty.
* Also note that we created an id field, which we set to be <code>PRIMARY KEY</code>. Every table has to have a <code>PRIMARY KEY</code> field, which is unique for every record.
* Often times this unique field will just be an id with the type serial. This means for every new record in the database, the <code>id</code> field will auto-increment by 1, meaning you do not have to explicitly give it a value.


###Inserting Data
Now that we have an author's table, let's insert a few authors into it.

````SQL
INSERT INTO author (name, twitter) VALUES ('Dr. Seuss', '@TheDoctor');
INSERT INTO author (name, twitter) VALUES ('George R. Martin', '@YourFavoriteCharactersDead');
INSERT INTO author (name, twitter) VALUES ('Edgar Allan Poe', '@Poestories');
````
* Notice the syntax, we specify the name of the table and the name of the columns we're INSERTING data INTO first.
* Then we specify the VALUES we're placing in those columns for that row. Note the ordering of values has to match the ordering of column names.
* You can see that we did not have to specify the <code>id</code> of each row. It automatically made these id's 1, 2, and 3 for us.
* To check that our entries are now in the database, run <code>select * from author;</code>. We'll cover more about reading data shortly.

###Updating Data
Once we have data in the database, we can also edit and update it. Let's take our Edgar Allan Poe author and update his twitter handle to '@PoeKnows'. The SQL command would be


````SQL
UPDATE author SET twitter = '@PoeKnows' WHERE id=3;
````


There is 3 parts to this update SQL statement.
* 1. We specify the table we're UPDATING.
* 2. We SET the field equal to the new value that we're changing
* 3. We specify WHERE the id is equal to 3, which we know is Edgar Allan Poe.
* Run the select command again in your psql shell to see that we did indeed change his twitter handle.

###Deleting Data
We can also delete records from the database in a similar fashion to updating.
````SQL
DELETE FROM author WHERE id=3;
````
* Notice, we specify the table we're DELETING FROM and WHERE the record's id is 3.
* If you try this out and check with our SELECT statement, you'll notice Edgar Allan Poe is no longer in our table.


###Querying Data
As we saw in the previous examples, we are able to read data from the database using <code>SELECT</code>

````SQL
SELECT * FROM author;
SELECT name, twitter FROM author;
````
* When we use <code>*</code> our <code>SELECT</code> statement will return all of the columns of the table.
* Instead of using <code>*</code> we can instead specify the exact columns we'd like to get.
* This is often good practice for performance if we're trying to pull data from a table with many columns and many rows.

###Querying with Parameters
Instead of getting all of the records in table, we can create <code>WHERE</code> clauses that have logic to limit our results.

````SQL
INSERT INTO author (name, twitter) VALUES ('Edgar Allan Poe', '@Poestories');
INSERT INTO author (name) VALUES ('Mark Twain');

SELECT * FROM author WHERE id > 1;
SELECT * FROM author WHERE name = 'Mark Twain';
SELECT name FROM author WHERE twitter IS NOT NULL;
SELECT name, twitter FROM author WHERE LENGTH(name) < 11;
````
* First let's add back Edgar Allan Poe as well as Mark Twain so we can practice more queries.
* Notice, we don't pass in a twitter handle for Mark Twain, he's not into social media.
* Our queries can use common logic operations >, <, =.
* We can also check if a field is NULL or not. NULL is PostgreSQL's version of Python's None.
* We can also use some builtin functions in PostgreSQL, like LENGTH, to get authors where their name is less than 11 characters long.

###Limiting Queries
When we have tables in our database with many rows, we may want to limit back how many we get a time.

````SQL
SELECT * FROM author LIMIT 1;
SELECT twitter FROM author WHERE twitter IS NOT NULL LIMIT 2;
````
* Using the <code>LIMIT</code> statement in PostgreSQL we're able to specify how many records we want at a time.
* We can say to the database, only give us one row back.
* We can also combine the <code>LIMIT</code> statement with other PostgreSQL SQL statements as well, such as <code>WHERE</code>.

###Sorting Queries
Often times we'd like to sort our results back from the database based on one or more columns. It's usually more efficient to do this with our SQL query, rather than with python.

````SQL
SELECT * FROM author;
SELECT * FROM author ORDER BY name;
SELECT * FROM author ORDER BY name ASC;
SELECT * FROM author ORDER BY name DESC;
SELECT id FROM author ORDER BY id DESC;
````
* By default if no <code>ORDER BY</code> is set the database usually returns the records to us by the order they were created. However this is not always guaranteed.
* Ascending order, <code>ASC</code>, means in alphabetical order when dealing with strings or from lowest to highest if applied to integers. Descending, <code>DESC</code>, means the opposite.
* If you use <code>ORDER BY</code>, but don't specify ASC or <code>DESC</code> it will assume an ascending order.

###Functions
PostgreSQL comes with a whole slew of functions that you can run in queries in the database.

Often it is much faster to run these functions in the database, rather than getting the data and then running them in Python.

````SQL
SELECT 2 + 2 AS addition;
SELECT 4 / 2 AS division;

SELECT upper(name) FROM author;
SELECT length(twitter) AS twitter_length, name, twitter from author ORDER BY twitter_length;
````
* We can run, for example, basic math in our SQL queries.
* We can also manipulate strings, just as we would in python. This third query will return us all of our authors' names, uppercased.
* Using <code>AS</code> we can rename what we'd like our columns to be called when returned, which can be especially useful for when using functions.
* We can then also use that new value to ORDER our query's results.

Let's try a few more advanced cases of functions.

````SQL
SELECT AVG(length(name)) from author;
SELECT MAX(length(twitter)) from author;

SELECT 'Name: ' || name AS display_name from author;
SELECT CONCAT(name, ' - ', twitter) from author;
````

* We can chain our calls and use the built in AVG and MAX functions to figure out the average author name length and the length of the longest twitter handle.
* We can also append arbitrary strings together using <code>||</code>
* If your values may be <code>NULL</code> it is often a good idea to use <code>CONCAT</code> instead, which can handle different situations better.


###Group By
Often times we'll want to logically group our records into different categories. This makes it easy to run our aggregate methods, like AVG and MAX on specific groups, not just for every record. The data that is used for this query is found [here] and will be used in the later exercises.

````SQL
SELECT continent, AVG(population) AS avg_pop FROM country GROUP BY continent;
SELECT continent, AVG(population) AS avg_pop FROM country GROUP BY continent HAVING AVG(population) > 0;
````

* This first query will return us the average population of every continent. The database will <code>GROUP</code> every record together, based on the value of its continent column, then do the math to find the average.
* Our second query uses the <code>HAVING</code> clause to specify that we only want results where the average population is greater than 0. <code>HAVING</code> is only used when we're using <code>GROUP BY</code>.

###Relationships
Now that we've got the fundamentals of PostgreSQL and SQL syntax, let's learn about the real reason we're using a relational database.

* Let's say we want to make a blog post table in our blog database.
* We'd like that blog post table to store the author for every blog post.
* Our first instinct may be to store the author's name in a column and their twitter handle in another column on the table for every blog post. This way, when we have a blog post we now have access to that author.
* But what would happen if Dr. Seuss changed his twitter handle? We'd have to update his twitter handle on every single blog post where he's the author. Also, thinking back to our python principles, this is not very dry.
* What we need to do is keep our author table and be able to relate our blog post table to our author table. This way, there is only one single record for an author that contains the proper and up to date information.

How do we relate a blog post record in our blog post table to a record in the author table?

* Well we know every table is supposed to have a <code>PRIMARY KEY</code>. This key is supposed to be unique for every single record we have in the table.
* Primary keys are never supposed to change once they're created. This is a contract we have with our database.
* This means we can safely store this key with our blog post, to always have a reference to the author, even though the author's data in its own table may change over time.

###One to Many
Let's create the new post table.

````SQL
CREATE TABLE post (
    id          serial PRIMARY KEY,
    title       varchar(120) NOT NULL,
    body        text,
    author_id   integer references author
);
````
* First, we've given our post table an id that's a primary key, a title, and a body.
* Next, we've added an author_id integer column where we'll store the blog author's primary key.
* Now, we need to tell PostgreSQL that this author_id actually <code>references</code> our author table. We do this by just specifying it on our author_id field.
* This constraint tells PostgreSQL that we want to create a concrete relationship from this author_id field to our author table. PostgreSQL knows that the primary key field of the author table is id and links them together appropriately.

Let's save some blog posts in our new table.

````SQL
INSERT INTO post (title, body, author_id) VALUES ('First!', 'My blog post.', 1);
INSERT INTO post (title, body, author_id) VALUES ('Second!', 'My second blog post.', 1);
INSERT INTO post (title, body, author_id) VALUES ('Best Blog Post', 'The best post.', 2);

INSERT INTO post (title, body, author_id) VALUES ('Will not work', 'Nice try.', 100);

````

* Put in the first 3 blog posts into your new table. We'll create two blog posts for author with the id 1, Dr. Seuss, and one for George R. Martin.
* Feel free to <code>SELECT * FROM author;</code> again to jog your memory.
* Now try to run this last statement. Notice PostgreSQL gives us an error, because it knows there is no author with the id 100. We made a contract with PostgreSQL by adding our <code>FOREIGN KEY CONSTRAINT</code> which it will not let us break.
* This is great! It means that if we have a blog post, we should always have an author we can go reference and PostgreSQL will error on us if we try to do something wrong.

###One to Many Explained
In this example, we created a One to Many relationship, which is important to understand the difference, since we'll be talking about another one shortly.

Here's how you should think about:

* A blog post has one author.
* An author can have many blog posts.
From this explanation we can see that we have one author to many blog posts. Let's revisit this in a bit.


###Queries with Joins
Let's see how we can query across our two blog tables.

````SQL
SELECT * FROM post, author WHERE post.author_id = author.id;
SELECT * FROM post INNER JOIN author ON (post.author_id = author.id);

SELECT post.title, author.name as author_name, author.twitter as author_twitter
    FROM post, author
    WHERE post.author_id = author.id;
````

* These two queries above, both get the same results.
* Basically, we're saying get us every post, and also get us the author info for each post as well.
* We can specify, which fields we actually want from each table as we see in the 3rd query. This is usually good practice as well as renaming the variable so our output is more explicit.

###Queries with Outer Joins
Let's see how we can query across our two blog tables.

````SQL
SELECT * FROM author LEFT OUTER JOIN post ON (author.id = post.author_id);
SELECT author.name as author_name, author.twitter, post.body as post_body
    FROM author
    LEFT OUTER JOIN post
    ON (author.id = post.author_id);

````

* We can also use an <code>OUTER JOIN</code>, where the main table we're using, author, in this example may not necessarily have a corresponding row in the joined table.
* If you notice in our results, some of our author's have NULL values in the columns for post.
* Again, we can rewrite this so we take only the columns we want and rename them so that it is more readable.

###Many to Many Relationships
Let's add tags to our posts.

````SQL
CREATE TABLE tag(
    id serial PRIMARY KEY,
    name varchar(20) NOT NULL
);
INSERT INTO tag (name) VALUES ('food');
INSERT INTO tag (name) VALUES ('literature');
INSERT INTO tag (name) VALUES ('poetry');
````

* First we need to make a table called tag, which will store all of the different tags for our blog posts.
* Secondly, let's populate it with some data to work with.
* How do we go about relating our tags to our blog posts? A blog post can have many tags and a tag can have many blog posts so we can't store an ID on either table like we did for post -> author.

We can create another table, which will store our relationships between posts and tags.

````SQL
CREATE TABLE post_tag(
    post_id integer references post,
    tag_id integer references tag,
    PRIMARY KEY (post_id, tag_id)
);
INSERT INTO post_tag (post_id, tag_id) VALUES (1, 3);
INSERT INTO post_tag (post_id, tag_id) VALUES (1, 2);
INSERT INTO post_tag (post_id, tag_id) VALUES (3, 2);

INSERT INTO post_tag (post_id, tag_id) VALUES (3, 10);
INSERT INTO post_tag (post_id, tag_id) VALUES (15, 1);
````


* We created a table which stores a foreign key to both the post table and to the tag table. Our table, post_tag is an intermediary table, which helps us store many to many relationships.
* We can insert values into this table by passing the ids of our other two tables.
* Our last two statements refer to tag ids or post ids that do not exist. PostgreSQL does not let us put this information in our database, just like we saw with the other example.

###Queries With Joins

````SQL

SELECT * FROM tag INNER JOIN post_tag ON (tag.id = post_tag.tag_id) WHERE post_tag.post_id = 1;
````
* First, let's write a query that will get us all of our tags for our post with id 1.
* We use an inner join on our post_tag many to many table, and specify <code>WHERE</code> post_id = 1
* We should get 2 tags back, which we tied to this post in our post_tag table on the previous query.

Let's get all of the tags for any blog post written by Dr. Seuss, whose author id is 1.

````SQL
SELECT tag.id as tag_id, tag.name as tag_name, post.title as post_title
    FROM tag
    INNER JOIN post_tag
    ON (tag.id = post_tag.tag_id)
    INNER JOIN post
    ON (post_tag.post_id = post.id)
    WHERE post.author_id = 1;
````

* This is as complicated as we'll take it for now, but we can actually <code>JOIN</code> across many tables.
* We can verbalize this as: let's get all tags, where the tag's id matches our post_tag's tag_id field, where post_tag's post_id matches the post's id on our post table, where our post table's author id is 1.

###Resources:
* [Visualize joins]
* [Official PostgreSQL Tutorials]


##Your Mission
* First, let's create a database for our world data. Run <code>create database world;</code>
* Let's load up the database, first download the data from [here].
* Next we need to load our new world database with the data, exit out of the psql shell then run <code>psql world < ~/Downloads/dbsamples-0.1/world/world.sql</code>
* Please note, your Download path to the file may be different than specified above. Just change it so that it points to where your world.sql file was downloaded to.

For the rest of the following exercises, make sure you save the queries you are running in a file for reference.

* First, make sure to run <code>\d</code> and <code>\dt</code> to inspect the available tables. Notice we have tables for city, country, and countrylanguages.
* Add a record to the country table: code: 'LIL', name: 'Lilliput', continent: 'Europe', population: 150. There will be other columns you need to make up data for. <code>SELECT * FROM country WHERE code='LIL';</code> should return the record.
* Update our 'Lilliput' record to fill in some of the various columns with made up data that are currently empty, such as life expectancy, indep year, capital, head of state, etc.
* Add a countrylanguage record for this new country. The language is 'Lilliputian', and should have the same Country Code as the Lilliput record. It should also be the official language and 99.5% of people speak it. Again, check your work with a <code>SELECT</code> statement.

After that, create queries to get the following sets of information. Make sure you save the queries you are running in a file for reference.

* The code, name, and surface area for all countries in Oceania.
* The capital id and population of every country with a population greater than 10 million.
* The name, district and population of every city in Italy.
* The name of each language, together with the country code, where the percentage is less than 25%.

Once that has been completed, create queries to get the following sets of information from the previous exercise, now sorted. Make sure you save the queries you are running in a file for reference.

* The code, name, and surface area for all countries in Oceania - sorted by surface area in descending order.
* The capital city and population of every country with a population greater than 10 million - sorted by population in ascending order.
* The name, district and population of every city in Italy - sorted first by district in ascending order and then population in descending order.
* The name of each language, together with the country code, where the percentage is less than 25% - sorted by language in ascending order, country code in ascending order and percentage in descending order.

####Function exercises

* Write a query that will return the average population of all countries as well as the average life expectancy.
* Write a query that will return the city with the largest name. Hint: You will need to use an ORDER BY and a Limit 1 clause in your query.
* Write a query that will return the country code for the country that has the highest percentage of it's population speaking Spanish. Hint: Use the countrylanguage table and a WHERE clause.
* Create a query that will return values from the Name, GNP and GNPOld columns for all records where the GNP value is greater than zero. The results should include an output column named ‘delta_percent’ that displays the difference between the GNP and GNPOld values as a percentage of the GNPOld value.

####Group By Exercises

* Create and execute an SQL statement that will return the average percentage that each language is used in countries in which it is spoken.
* Next, make it so that the results should only show languages that are spoken on average by more than 20% of the population and should be sorted in descending order of average percentage.
* Finally, round all of the average percentages to only 2 decimal places.

####Joins Exercises
Write a query that will return the following for all cities in Asia.

* The name of the city
* The district that it is in
* The name of the country that it is in
* The population of the city as a value
* The population of the city as a percentage of the population of the country to 1 decimal place

####Outer Joins Exercises
Write a query that will return values for the language names and country name for any countries in Antarctica.

Make sure that there is at least one output record per country.

####Queries with Joins Exercises
We'll use our blog database to try to find these results.

* Write a query that gets all tags for posts whose title is 'First!'.
* Write a query that gets all posts that have the tag with the id 2.
* Write a query that gets all posts that have the tag 'poetry'.
* Hardest: Write a query that returns all tags for blog posts written by an author whose twitter handle's length is less than 15.


####Query Project!
Let's create a database of movies.

* We'll need a genre table, which stores the names of different genres.
* We should have an actor's table, which stores their first and last names.
* We should also have a director's table, which stores their first and last names.
* And we'll need a movie table, which stores the name of the movie, how long it is, the date it came out (try using a PostgreSQL date field), and how much its budget was.
* A movie will have one director. It will have many actors and it will have many genres.

Once you've created your database with your tables and relationships populate it with data from random movies from imdb.com. Try to get at least 10 movies in there.

Next try to construct the SQL queries below

* Get all movies that happened in the past 5 years.
* Get all movies who has the 'Action' genre (or a similar genre you put in your database)
* Get a list of all of the directors and the average budget for their movies.
* Get a list of actors for the oldest movie in your database.

Get creative and try to play around with some of your own questions / queries.

[here]: http://pgfoundry.org/frs/download.php/527/world-1.0.tar.gz
[Visualize joins]: http://blog.codinghorror.com/a-visual-explanation-of-sql-joins/
[Official PostgreSQL Tutorials]: http://www.postgresql.org/docs/8.0/static/tutorial.html