#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""

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
# n/log(n) = 10000 => n ≈ 150000
a = filter(is_prime,range(1,150000))

print a[10000]