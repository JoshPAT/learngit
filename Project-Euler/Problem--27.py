#!/usr/bin/env python 2.7.8
# -*- coding: utf-8 -*-

def is_prime(n):
    #return true if n is 2 or 3
    if n <= 0:
        return False
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

max_length = 0
for a in range(-1000,1000): 
    for b in range(-1000,1000):
        i = 0
        n = i**2 + a*i + b
        while is_prime(n):
            i +=1
            n = i**2 + a*i + b           
            if max_length < i:
                max_length = i
                max_a = a
                max_b = b
            if max_length == i:
                if abs(a*b) > abs(max_a*max_b):
                    max_length = i
                    max_a = a
                    max_b = b

print max_a,max_b,(max_a*max_b),max_length
