# https://projecteuler.net/problem=7
def nthPrime(n):
	primes = [3]
	number = 3
	count = 2
	while(True):
		number += 2
		if all(number % x != 0 for x in primes):
			primes.append(number)
			count += 1
		if count==n :
			return number

print(nthPrime(10001))