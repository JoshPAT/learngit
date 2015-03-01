#!/usr/bin/env python 2.7.8
# -*- coding: utf-8 -*-
"""
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""
import logging
L=[0,0,]

for n in range(2,10000):
	div =0
	for i in range(1,int(n*0.5)+1):
		if n%i ==0:
			div = i + div
	L.append(div)

sum1 =0
for i in range(2,10000):
	if L[i] > 10000:
		continue
	else:
		if  L[L[i]] == i:
			if L[i] !=i:
				print i
				sum1 += i 
print sum1

import math

def get_divisors_sum(n):
    divisors = []
    divisors.append(1)
    end = int(math.sqrt(n))
    for i in range(2, end):
        if i not in divisors and n % i == 0:
            divisors.append(i)
            divisors.append(n / i)
    return sum(divisors)

amicable_nums = set()
for n in range(2, 10000):
    dsum = get_divisors_sum(n)
    if n == dsum:
        continue
    
    if n == get_divisors_sum(dsum):
        amicable_nums.add(n)
        amicable_nums.add(dsum)

print sum(amicable_nums)