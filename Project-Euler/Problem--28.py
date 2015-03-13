#!/usr/bin/env python 2.7.8
# -*- coding: utf-8 -*-

#Calculate that the 1001 * 1001 would be 501 
# n means one round, step means the gap from each number to anothter

sums = 1
n = 2
step = 2 * (n-1) 
while n <= 501:
	for x in range((2*n-1)**2,(2*n-3)**2, -step):
		sums += x 
	n += 1 
	step = 2*(n-1) 

print sums 




