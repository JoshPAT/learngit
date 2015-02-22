

#Find the difference between the sum of the squares of the 
#first one hundred natural numbers and the square of the sum.
def squarex(x):
	return x * x
m = reduce(lambda x,y: x+y, map(squarex,range(1,101)))
n = squarex(reduce(lambda x,y: x+y, range(1,101)))
print m-n
