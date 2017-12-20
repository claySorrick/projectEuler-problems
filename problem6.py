# https://projecteuler.net/problem=6
def sumSquareDifference():
	sumOfSquares, squareOfSum = 0, 0
	for i in range(1,101):
		sumOfSquares += i * i
		squareOfSum += i
	squareOfSum = squareOfSum * squareOfSum
	print("squareOfSum minus the sumOfSquares = " 
		+ "(%d - %d) = %d" % (squareOfSum, sumOfSquares, (squareOfSum - sumOfSquares)))
		

sumSquareDifference()

# r = range(1, 101)  
# a = sum(r)  
# print (a * a - sum(i*i for i in r))  