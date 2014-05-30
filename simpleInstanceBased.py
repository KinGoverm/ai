from math import sqrt

f = open('dataset/dataset.txt')
lines = f.readlines()
f.close()


dic={}

for line in lines:
	words = line.split()
	
	insideList = []

	insideList.append(int(words[1]))
	insideList.append(int(words[2]))
	insideList.append(int(words[3])*20)
	insideList.append(int(words[4]))
	insideList.append(int(words[5])*10)

	
	dic[words[0]] = insideList






inp = raw_input('Please enter your rating from 100 :\n')
inp = int(inp)



MinDistance = 10000
closestID = 'None'


for id in dic:	
	s = 0
	obj = dic[id]
	
	for i in obj:
		s += abs ( (i - inp)*(i - inp) )

	dist = sqrt(s)

	if dist < MinDistance:
		MinDistance = dist
		closestID = id
		rating = obj
	


print "closest movie id to your rating is : ",closestID 
print "and rating for this movie is : ", rating

