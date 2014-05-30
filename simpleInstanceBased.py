from math import sqrt

f = open('dataset/dataset.txt')
lines = f.readlines()
f.close()


array=[]


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

	array.append(dic)



#print array


inp = raw_input('Please enter your rating from 100 :\n')
inp = int(inp)



MinDistance = 101
closestID = 'None'

for obj in array:	
	s = 0

	for i in obj.values()[0]:
		s += abs ( (i - inp)*(i - inp) )

	dist = sqrt(s)
	if dist < MinDistance:
		MinDistance = dist
		closestID = obj.keys()[0]



print "closest movie id to your rating is : ",closestID 
print "and distance from this instance is : ", MinDistance
#print "and rating for this movie is : ", dic[str(closestID)] 

