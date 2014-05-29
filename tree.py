class Node:
	def __init__(self,data):
		
		self.left = None
		self.right = None
		self.data = data

	def print_tree(self):
	
		if self.left or self.right:
			print self.data

		if self.left:
			print 'l',self.left.data
		
		if self.right:
			print 'r',self.right.data
		
		if self.left:
			self.left.print_tree()

		if self.right:
			self.right.print_tree()
