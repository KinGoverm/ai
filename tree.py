from math import sqrt

class Node:
	def __init__(self,data):
		
		self.parent = None
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

	def distance(self,instance):
		s = 0
		
		for i in range(5):
			s += abs ( (self.data[i] - instance[i])*(self.data[i] - instance[i]) )
			
		dist = sqrt(s)
		return dist

		
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


	def selfSearchTree(self,instance):

		if len(self.data) == 6:
			splitIndex = self.data[5]
			if instance[splitIndex] > self.data[splitIndex]:
				if self.right and len(self.right.data) :
					return self.right.selfSearchTree(instance)
				else:
					return self

			else:
				if self.left and len(self.left.data):
					return self.left.selfSearchTree(instance)
				else:
					return self
		else:
			return self

	def bestSearchTree(self,instance):

		node = self.selfSearchTree(instance)

		siblingNodes = [node.parent,node.parent.left,node.parent.right,node.parent.parent,node.parent.parent.left,node.parent.parent.right]

		MinDistance = 10000
		for node in siblingNodes:
			if node.data:
				if MinDistance > node.distance(instance):
					MinDistance = node.distance(instance)
					NearestNode = node

		return NearestNode
		
