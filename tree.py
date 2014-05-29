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

	
	def search_tree(self,instance):

		if len(self.data) == 6:
			splitIndex = self.data[5]
			if instance[splitIndex] > self.data[splitIndex]:
				if self.right and len(self.right.data) :
					return self.right.search_tree(instance)
				else:
					return self.data

			else:
				if self.left and len(self.left.data):
					return self.left.search_tree(instance)
				else:
					return self.data
		else:
			return self.data


