#Problem-10.py

#Summation of primes
#introduce a better algorithm
"""
import math
def is_prime(x):
	if x == 1:
		return False 
	if x == 2:
		return True
	for i in range(2,int(math.sqrt(x))+1):
		if x%i == 0:
			return False
	return True
"""
def is_prime(n):
    #return true if n is 2 or 3
    if n <= 3:
        return n >= 2
    #return false if n is divisible by 2 or 3
    if n % 2 == 0 or n % 3 == 0:
        return False
    #uses the 6k+-1 algorithm
    for i in range(5, int(n ** 0.5) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True

print reduce(lambda x,y: x+y ,filter(is_prime,range(1,2000000)))

