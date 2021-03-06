#!/usr/bin/env python 2.7.8
# -*- coding: utf-8 -*-
'''
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
'''
#define sum of the divisors
import math
def get_sum_div(number):
	div =[1]
	for i in range(2,int(math.sqrt(number))+1):
		if i not in div and number%i ==0 :
			div.append(i)
			if i * i !=number:
				div.append(number/i)
	if sum(div) > number:
		return True
	else:
		return False
#find all the aboundant numbers
nonabun = filter(get_sum_div, range(1,28124))
nonabun_sum =[]
for x in nonabun:
	for y in nonabun:
		nonabun_sum.append(x+y)

nonabun_sum =set(nonabun_sum)

#add all the non-abundunt numbers
i = range(1, 28124)
d = []
for n in i:
    if n not in nonabun_sum:
        d.append(n)
        
print(sum(d)) 
