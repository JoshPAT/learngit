#!/usr/bin/env python
# -*- coding: utf-8 -*-
import math
"""
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
"""
#Solutions to Get a Prime!
"""
1.Divide Trial (whether x is a prime)
    (1) try from 2 to x - 1 . Difficulty: *
    (2) try from 2 to x/2 . Difficulty: **
    (3) try from 2 to root(x) . Difficulty: ***
    (4) first try 2, then try prime number in root(x) Difficulty: ****
2.Filter
  Use sieve of Eratosthenes!
"""
n=600851475143
i=2
while i*i < n:
    while n % i == 0:
        n = n /i
        print n
    i = i + 1

print n


