#!/usr/bin/env python 2.7.8
# -*- coding: utf-8 -*-
import string
with open('p022_names.txt') as f:
	matrix =[i.strip('"') for i in f.read().split(',')]
	matrix.sort()

dictx = {'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8,'I':9,'J':10,'K':11,'L':12,'M':13,'N':14,'O':15,'P':16,'Q':17,'R':18,'S':19,'T':20,'U':21,'V':22,'W':23,'X':24,'Y':25,'Z':26}
sums = 0
for n in range(len(matrix)):
	prod = 0
	for l in matrix[n]:
		 prod += dictx[l]
	sums += prod * (n+1)

print sums


valuehash = dict(zip([x for x in string.letters[26:]],range(1,27)))
namescores = [sum([valuehash[x] for x in matrix[i]])*(i+1) for i in range(len(matrix))]
print sum(namescores)
