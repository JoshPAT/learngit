#!/usr/bin/env python
# -*- coding: utf-8 -*-

#my stupid code
"""
a = [ m * n for m in range(1000,316,-1) for n in range(1000,316,-1)]
b = 0
for x in a:
	if str(x)[:3] == str(x)[5:2:-1]:
		if x > b:
			b = x
print b
"""
#much cooler code
print max([x*y for x in range(356,1000) for y in range(356,1000) if str(x*y) == str(x*y)[::-1]])
