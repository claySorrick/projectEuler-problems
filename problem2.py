# https://projecteuler.net/problem=2

def sumEvenFibonacci():
	prev, cur = 0, 1
	total = 0
	while(True):
		prev, cur = cur, cur + prev
		if(cur >= 4000000):
			break
		if(cur % 2 == 0):
			total += cur
		
	return total
	
print("sum of even numbers in Fibonacci = %d" % sumEvenFibonacci())