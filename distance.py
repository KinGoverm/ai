from math import sqrt
s=0
for i in range(5):
	inp1 = raw_input('')
	inp1 = int(inp1)

	inp2 = raw_input('')
	inp2 = int(inp2)

	s += (inp2-inp1)*(inp2-inp1) 

print sqrt(s)
