#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. 
Although it has not been proved yet (Collatz Problem), 
it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?
"""
#奇偶归一猜想

"""very stupid newbie python code
def collatz(n):
	if n !=1:
		print "%d ->" % n,
		if n%2 == 0:
			collatz(n/2)
		if (n - 1)%2 == 0:
			collatz(3*n+1)
	else:
		print "1"
		print counter +1
"""
#one yr advance python code
"""
def collatzcounter(n):
	counter = 1
	while n >1:
		counter += 1
		#print "%d ->" % n,
		if n%2 == 0:
			n = n/2
		elif (n - 1)%2 == 0:
			n = 3*n+1
	#print "1"
	return counter

print collatzcounter(2)

big = 0
i = 1
while i<1000000:
	i  += 2
	big = max(big, collatzcounter(i))

print big
"""
#a much faster but elusive python code

limit = 1000000
collatz_length = [0] * limit 
collatz_length[1] = 1
max_length = [0,0]


for i in range(1,limit):
	n = i
	r = 0 #number recorded
	TO_ADD =[]
	#part similar to collatz func
	while n > limit - 1 or collatz_length[n] < 1:# if cached before then bigger than 1
		TO_ADD.append(n) # add number to lists eg.[3,10,5,16,8,4,2]
		if n%2 == 0: n = n/2
		else: n = 3*n +1
		r += 1  #
	#here is where optimation comes
	for j in range(r):# in 7
		m = TO_ADD[j] #eg.[3,10,5,16,8,4,2]
		if m < limit: 
			new_length = collatz_length[n] + r - j # （当前cached length）+  - j是位移差
			collatz_length[m] = new_length
			if new_length > max_length[1]: max_length =[i, new_length]

print max_length

#very effecient and understandable code!!!

dict={}
dict[1]=0
longest=0
for i in range (2,1000000):
		n=i
		count=0
		while (dict.has_key(n) ==False):
			if (n%2==0):
				n=n/2
				count+=1
			elif (n%2!=0):
				n= 3*n +1
				count+=1
		
		dict[i] = dict[n]  + count 
		
		if (dict[i]>longest): 
			longest = dict[i]
			number=i

print [number,longest]













