# https://projecteuler.net/problem=8

def adjacentDigitGreatestProduct(length, input):
	saveIndex = 0
	maxProduct = 0
	for i in range(len(input) - length):
		tempProduct = 1;
		for j in range(length):
			tempProduct *= int(input[i+j])
		if(tempProduct > maxProduct):
			print(tempProduct)
			maxProduct = tempProduct
			saveIndex = i
	print(input[saveIndex:(saveIndex + length)])
	return maxProduct
			
print("greatest product of 13 adjacent digits = "
	+ str(adjacentDigitGreatestProduct(13, input)))

print(9 * 9 + 12 * 12 )
print(15 * 15)