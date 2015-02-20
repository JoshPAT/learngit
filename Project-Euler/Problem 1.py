# -*- coding: utf-8 -*-
#Problem 1
sum = 0
for x in range(1000):
	if (x%3 == 0)or(x%5 ==0):
		sum += x
		print x
print sum