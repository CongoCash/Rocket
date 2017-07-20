
class Stack(object):

	# Variables declared when object instantiated
	def __init__(self):
		self.stack = {}
		self.size = 0

	def push(self, item):
		self.stack[self.size] = item
		self.size += 1

	def pop(self):
		if len(self.stack) > 0:
			self.size -= 1
			top_element = self	.stack[self.size]
			del self.stack[self.size]
			return top_element
		else:
			return None

	def view_size(self):
		return self.size


