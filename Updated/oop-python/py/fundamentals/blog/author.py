# Don't use import *
from blog_post import BlogPost

class Author(object):
	def __init__(self, name):
		self.name = name
		self.blog_posts = []

	def write_blog_post(self, title, published_date):
		b = BlogPost(title=title, published_date=published_date)
		self.blog_posts.append(b)
		return b.title

	# Official string representation of class
	def __repr__(self):
		return self.name