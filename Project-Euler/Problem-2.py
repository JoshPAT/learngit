# -*- coding: utf-8 -*-

#Recursive Way
def fn1(x):
    if x == 1:
        return 1
    elif x == 2:
        return 2
    else:
        return fn1(x-2) + fn1(x-1)

from itertools import count
def Sumfn1():
    sum = 0
    for i in count(1):
        temp = fn1(i)
        if temp > 4000000:
            break
        if temp % 2 ==0:
            sum += temp
    print sum


Sumfn1()
