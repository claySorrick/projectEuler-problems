# https://projecteuler.net/problem=4

def threeDigitPalindromeProd():
	lrg = (0, 0, 0)
	for i in range(100, 1000):
		for j in range(i, 1000):
			palin = False
			sum = i * j
			st = str(sum)
			length = len(st)
			for k in range(0,int(length/2)):
				if(st[k] != st[length-k-1]):
					palin = False
					break
				palin = True
			if(palin):
				if(sum > lrg[2]):
					lrg = (i, j, sum)
	return lrg
print("largest palindrome made from product of two 3 digit numbers. "
	+ "%d * %d = %d" % threeDigitPalindromeProd())