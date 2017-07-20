class LinkedList(object):
	def __init__(self):
		self.current_node = None

	def add_to_tail(self, value):
		new_node = Node(value)
		new_node.next = self.current_node
		self.current_node = new_node

	def size(self):
		current = self.current_node
		count = 0
		while current != None:
			count += 1
			current = current.next

		return count

	def remove_head(self):
		current = self.current_node
		self.current_node = current.next

	def contains(self, target):
		current = self.current_node
		found = False
		while current != None:
			if current.value == target:
				found = True
				break # Stop the loop if you find what you need
			current = current.next

		return found

	def print_ll(self):
		node = self.current_node
		while node:
			print node.value
			node = node.next


class Node(object):
	def __init__(self, value):
		self.value = value
		self.next = None

	def get_next(self):
		return self.next