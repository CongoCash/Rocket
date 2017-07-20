class Queue(object):
	def __init__(self):
		self.start = -1
		self.end = -1
		self.queue = {}

	def enqueue(self, item):
		self.end += 1
		self.queue[self.end] = item
		print '{} has been added at index {}'.format(item, self.end)

	def dequeue(self):
		if self.queue:
			self.start += 1
			result = self.queue[self.start]
			del self.queue[self.start]
			return result
		else:
			return None

	def size(self):
		return self.end - self.start
