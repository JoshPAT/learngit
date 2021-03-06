#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
The sequence of triangle numbers is generated by adding the natural numbers. 
So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. 
The first ten terms would be:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

Let us list the factors of the first seven triangle numbers:

 1: 1
 3: 1,3
 6: 1,2,3,6
10: 1,2,5,10
15: 1,3,5,15
21: 1,3,7,21
28: 1,2,4,7,14,28
We can see that 28 is the first triangle number to have over five divisors.

What is the value of the first triangle number to have over five hundred divisors?
"""
import time
# define a func to count the divisors:
start = time.time()
def divcount(n):
	count = 0
	if n==1:
		return 1
	for i in range(1,int(n**0.5) + 1):
		if n % i == 0:
			count += 1
	return count*2

n , i = 1 , 1
while divcount(n) < 500:
	i += 1
	n += i 


elapsed = (time.time() - start)
print n,elapsed