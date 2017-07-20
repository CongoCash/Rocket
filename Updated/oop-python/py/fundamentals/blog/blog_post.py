class BlogPost(object):
	def __init__(self, title, published_date, author=None, content=None,):
		self.title = title
		self.content = content
		self.published_date = published_date
		self.author = author

	def change_author(self, old_author, new_author):
		self.author = new_author
		old_author.blog_posts.remove(self)
		new_author.blog_posts.append(self)

	# Official string representation of class
	def __repr__(self):
		return self.title