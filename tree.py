class Node:
	def __init__(self,data):
		
		self.left = None
		self.right = None
		self.data = data

	def print_tree(self):

		if self.left:
			self.left.print_tree()

		print self.data
		print

		if self.right:
			self.right.print_tree()
