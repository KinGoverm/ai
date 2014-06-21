from math import sqrt
from tree import Node

def calculateAvg(list):

	s = 0

	for object in list:
		s += object

	return s/len(list)

		
def calculateVariance(list):

	avg=calculateAvg(list)
	s = 0

	for object in list:
		s += ( object - avg)^2

	return 	s/len(list)

def makeTree(node):


	axises = [] 
	if len(node.data) == 1 or len(node.data) == 0:
		return
	for instance in node.data:
		if type(instance) is int:
			return
		for i in range(len(instance)):
			if len(axises) <= i :
				axises.append([])
			axises[i].append(instance[i])
	
	# calculate The best axis
	maxVariance=0			
	bestAxisIndex = 0
	for index,axis in enumerate(axises):
		variance = calculateVariance(axis)
		if variance > maxVariance:
			bestAxisIndex = index

	bestAxis = axises[ bestAxisIndex ]
	
	# calculate split point on the best axis
	sortedBestAxis = sorted( bestAxis )
	median = sortedBestAxis[ len(sortedBestAxis)/2 ]
	
	splitPointIndex = bestAxis.index(median)
	splitPoint = node.data [ splitPointIndex ]
	
	
	rightNode=[]
	leftNode=[]

	for instance in node.data:
		if instance != splitPoint:
			if instance[bestAxisIndex] > splitPoint[bestAxisIndex]:
				rightNode.append(instance)
			else:
				leftNode.append(instance)


	# make tree
	
	splitPoint.append(bestAxisIndex)

	node.data = splitPoint
	
	if len(rightNode) == 1:
		rightNode = rightNode[0]
	if len(leftNode) == 1:
		leftNode = leftNode[0]

	node.right = Node(rightNode)
	node.left = Node(leftNode)
	node.right.parent = node
	node.left.parent = node

	makeTree(node.right)
	makeTree(node.left)



	


f = open('dataset/dataset.txt')
lines = f.readlines()
f.close()


array=[]
allInstances=[]

for line in lines:
	words = line.split()
	
	insideList = []

	insideList.append(int(words[1]))
	insideList.append(int(words[2]))
	insideList.append(int(words[3])*20)
	insideList.append(int(words[4]))
	insideList.append(int(words[5])*10)

	dic={}
	dic[words[0]] = insideList

	allInstances.append(insideList)

	array.append(dic)







MinDistance = 101
closestID = 'None'


# we have 5 dimensions
# for every instance in list we should have a node in tree
# first we insert all instances to the root and in every iteration we will break it down to the left and right child

root = Node ( allInstances )
makeTree(root)

inp = raw_input('Please enter your rating from 100 :\n')
inp = int(inp)

inst = [inp,inp,inp,inp,inp]

target = root.search_tree(inst)

print 

for index,obj in enumerate(allInstances):
	if obj == target:
		print "Closest movie id to your rating is : ",index+1
		if len(target) == 6:
			target = target[:5]
		print "and rating for this movie is : ",target
		print "According to documention probably this is not the best answer , improvements will be considered in next phase"
		break

print 
print "results after improvements"
print 

bestTarget = root.bestSearchTree(inst)

for index,obj in enumerate(allInstances):
	if obj == bestTarget.data:
		print "Closest movie id to your rating is : ",index+1
		if len(bestTarget.data) == 6:
			bestTarget.data = bestTarget.data[:5]
		print "and rating for this movie is : ",bestTarget.data
		break


inp = raw_input('Do you want to see the entire tree? \n *trust me,you do not wanna see the entire tree!*  (y,n) \n')

if inp =='y':
	
	print "Complete Tree :"
	print "format: l => left node , r => right node"
	print 
	root.print_tree()





