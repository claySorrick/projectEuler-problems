# https://projecteuler.net/problem=9

def pythagoreanTriplet(target):
	a, b, c = 3, 4, 5
	i = 1;
	while(True):
		a, b, c = a * i, b * i, c * i
		print(a,b,c)
		if(a + b + c >= target):
			return (a,b,c)
		i += 1

print(pythagoreanTriplet(1000))