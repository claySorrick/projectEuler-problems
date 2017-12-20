# https://projecteuler.net/problem=1

def multiplesThreeFive(end):
	if(end<=0):
		return 0
	sum = 0
	for i in range(1,end):
		if(i % 3 == 0):
			print("3  %d" % i)
			sum += i
		elif(i % 5 == 0):
			print("5  %d" % i)
			sum += i
	return sum
	
print("sum of numbers div 3 or 5 = %d" % multiplesThreeFive(1000))