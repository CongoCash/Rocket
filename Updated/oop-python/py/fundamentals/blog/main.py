"""
To run this program, make sure you are on the blog/ level (where main.py is) in your command line
(in Pycharm you can get to your terminal by click on the box at the bottom left of your window). Then run

python main.py YOUR NAME HERE

If you get an index out of range error it's because you haven't supplied your name
as an argument when running the program.

"""



# Sys allows for command line interaction (i.e. when you run a program on the command line)
# An example of using this in the terminal would look like python main.py name
# The sys.argv[0] is the name of the program so now the string name is sys.argv[1]
import sys

# Import the 'Author' class from author.py
from author import Author

def blog_manager(user, blog_posts, authors):

	# Ask for input from the user which we can check against later. Convert to lowercase to check for fewer cases
	action = raw_input('Would you like to (A)dd a blog post, (S)ee existing posts or (Q)uit? ').lower()

	if action == 'a':
		is_author = raw_input('Are you the author of this post? (y/n) ').lower()
		if is_author == 'y':
			author = user
		else:
			author_name = raw_input('What is the name of the author? ')
			author = Author(author_name)
			authors.append(author)
		title = raw_input('What is the title of the blog post? ')
		published_date = raw_input('When was this published? ')
		b = author.write_blog_post(title, published_date)
		blog_posts.append(b)

		print 'Congratulations! You added post {} for {}'.format(b, author)

		blog_manager(user, blog_posts, authors)
	elif action == 's':
		print blog_posts
		blog_manager(user, blog_posts, authors)
	elif action == 'q':
		print 'Thanks for using the blog!'
	else:
		print 'Sorry, I do not understand what you want.'
		blog_manager(user, blog_posts, authors)

# Script starts here
print 'Hey! Welcome to the blog, {}'.format(sys.argv[1])

# Instantiate a new author with the passed in name from the command line
user = Author(sys.argv[1])

# Empty list for the blog posts
blog_posts = []

# This is casting 'authors' as a list to be passed into the blog_manager
authors = [user]

# Now call the function blog_manager called above
blog_manager(user, blog_posts, authors)
