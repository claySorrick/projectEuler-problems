# https://projecteuler.net/problem=3

def largestPrimeFactor(num):
	lrg = 1
	while(lrg<num):
		if(num % lrg == 0):
			print(lrg)
			num = num / lrg
		lrg += 1;
	return lrg
	
print("largest prime factor of %d = %d" 
	% (600851475143, largestPrimeFactor(600851475143)))