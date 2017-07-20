class LinkedList(object):
	def __init__(self):
		self.current_node = None

	def add_to_tail(self, value):
		new_node = Node(value)
		new_node.next = self.current_node
		self.current_node = new_node

	def remove_head(self):
		pass

	def contains(self, target):
		pass

	def print_ll(self):
		node = self.current_node
		while node:
			print node.value
			node = node.next

class Node(object):
	def __init__(self, value):
		self.value = value
		self.next = None
