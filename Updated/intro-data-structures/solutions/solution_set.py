class Set(object):
	def __init__(self):
		self.set = {}

	def add(self, item):
		# SOLUTION START
		self.set[item] = True
		# SOLUTION END

	def contains(self, item):
		# SOLUTION START
		if len(self.set) == 0:
			print 'Add items to the set!'

		# Built in keyerror if key does not exist
		if self.set[item]:
			return self.set[item]
		# SOLUTION END

	def remove(self, item):
		# SOLUTION START
		if self.set[item]:
			del self.set[item]
		# SOLUTION END
