# https://projecteuler.net/problem=5
def smallestPositiveNumEvenlyDivisible():
	check_list = [11, 13, 14, 16, 17, 18, 19, 20]
	step = 20
	for num in range(step, 999999999, step):
		if all(num % n == 0 for n in check_list):
			print(num)
	# for i in range(end,1,-1):
		
		
	
# print("smallest positive number evenly divisible by all "
		# + "of the numbers from 1 to 20 = %d" % smallestPositiveNumEvenlyDivisible(10))
smallestPositiveNumEvenlyDivisible()