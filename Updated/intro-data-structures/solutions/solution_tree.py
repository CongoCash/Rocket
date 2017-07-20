class Tree(object):
	def __init__(self, value):
		self.value = value
		self.children = []

	def add_child(self, value):
		"""
		Is instance checks if the value passed in is an instance of 'Tree'
		If this is true, simply append the tree, otherwise, make a new instance
		of a tree and append to children array
		"""
		if isinstance(value, Tree):
			self.children.append(value)


		child = Tree(value)
		self.children.append(child)

	def contains(self, target):
		found = False
		def subroutine(node):
			if node.value == target:
				found = True
				return

			for child in node.children:
				subroutine(child)

		subroutine(self)
		return found